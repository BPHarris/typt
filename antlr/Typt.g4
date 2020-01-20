/// Typt.g4 -- The grammar specification for Typt

// References:
//  - The following was used to handle INDENT/DEDENT in Python like
//    grammars:
//    https://github.com/antlr/grammars-v4/blob/master/python3-py/Python3.g4
//  - The Python Language Reference:
//    https://docs.python.org/3.3/reference/grammar.html

grammar Typt;

tokens { INDENT, DEDENT }

/* Lexer imports and preamble */
@lexer::header {
from antlr4.Token import CommonToken
import re
import importlib

# Allow languages to extend the lexer and parser, by loading the parser dynamically
module_path = __name__[:-5]
language_name = __name__.split('.')[-1]
language_name = language_name[:-5]  # Remove Lexer from name
LanguageParser = getattr(importlib.import_module('{}Parser'.format(module_path)), '{}Parser'.format(language_name))
}

/* Lexer members -- handle INDENT/DEDENT */
@lexer::members {
@property
def tokens(self):
    try:
        return self._tokens
    except AttributeError:
        self._tokens = []
        return self._tokens

@property
def indents(self):
    try:
        return self._indents
    except AttributeError:
        self._indents = []
        return self._indents

@property
def opened(self):
    try:
        return self._opened
    except AttributeError:
        self._opened = 0
        return self._opened

@opened.setter
def opened(self, value):
    self._opened = value

@property
def last_token(self):
    try:
        return self._last_token
    except AttributeError:
        self._last_token = None
        return self._last_token

@last_token.setter
def last_token(self, value):
    self._last_token = value

def reset(self):
    super().reset()
    self.tokens = []
    self.indents = []
    self.opened = 0
    self.last_token = None

def emitToken(self, t):
    """Name non-PEP8 as name is fixed by antlr."""
    super().emitToken(t)
    self.tokens.append(t)

def nextToken(self):
    """Name non-PEP8 as name is fixed by antlr."""
    if self._input.LA(1) == Token.EOF and self.indents:
        for i in range(len(self.tokens)-1,-1,-1):
            if self.tokens[i].type == Token.EOF:
                self.tokens.pop(i)
    
        self.emitToken(self.common_token(LanguageParser.NEWLINE, '\n'))
    
        # Handle dedents
        while self.indents:
            self.emitToken(self.create_dedent())
            self.indents.pop()
    
        self.emitToken(self.common_token(LanguageParser.EOF, "<EOF>"))
    
    next = super().nextToken()
    if next.channel == Token.DEFAULT_CHANNEL:
        self.last_token = next
    
    return next if not self.tokens else self.tokens.pop(0)

def create_dedent(self):
    """Return a new DEDENT token at the current line."""
    dedent = self.common_token(LanguageParser.DEDENT, "")
    dedent.line = self.last_token.line
    return dedent

def common_token(self, type, text, indent=0):
    """Create a common token of the the given type."""
    stop = self.getCharIndex() - 1 - indent
    start = (stop - len(text) + 1) if text else stop
    return CommonToken(self._tokenFactorySourcePair, type, super().DEFAULT_TOKEN_CHANNEL, start, stop)

@staticmethod
def get_indentation_count(spaces):
    count = 0
    for ch in spaces:
        if ch == '\t':
            count += 8 - (count % 8)
        else:
            count += 1
    return count

def at_start_of_line(self):
    """Get the token at the begining of the current line."""
    return Lexer.column.fget(self) == 0 and Lexer.line.fget(self) == 1

}

/*****************************************************************************/

/* Global TODO */
// TODO: Add list, tuple, dict, set, etc. defs as atoms i.e. [1, 2, 3] is an atom
// TODO: Multi-line comments
// TODO: Sequences (i.e. 'print(); print()'), worth it?
// TODO: Omit return type (i.e. no '-> type') as short-hand for '-> None'
// TODO: Required/default parameters (i.e. 'arg : type' and 'arg : type = VALUE')

/*****************************************************************************/


/* Parser Rules */
program: (NEWLINE | using)* (NEWLINE | stmt)* EOF;


using
    : 'using' ':'
        NEWLINE INDENT (func_signature NEWLINE)+ DEDENT
      'from' library_name=name ('as' library_alias=name)?
    ;


stmt
    : simple_stmt
    | compound_stmt 
    ;


argument_list       : argument (',' argument)* ;
argument            : test ;
// argument_optional   : name '=' test ;

/*****************************************************************************/


/* Parser Rules: Simple Statements (simple_stmt) */
simple_stmt
    : small_stmt NEWLINE
    ;

small_stmt
    : expr_stmt
    | var_dec_stmt
    | del_stmt
    | pass_stmt
    | flow_stmt
    // | import_stmt // TODO: How to handle imports? (import is from *.typt, using is from *.py)
    ;

expr_stmt
    : lhs=test ((anassign | augassign) rhs=test)?
    // test (',' test)* (',')? (anassign | augassign) test
    ;
anassign
    : '='
    ;
augassign
    : '+='
    | '-='
    | '*='
    | '@='
    | '/='
    | '%='
    | '&='
    | '|='
    | '^='
    | '<<='
    | '>>='
    | '**='
    | '//='
    ;

var_dec_stmt
    : lhs=name ':' typt_type
    | lhs=name ':' typt_type '=' rhs=test
    ;

del_stmt    : 'del' exprlist;
pass_stmt   : 'pass';

flow_stmt
    : break_stmt 
    | continue_stmt
    | return_stmt
    ;
break_stmt      : 'break';
continue_stmt   : 'continue';
return_stmt     : 'return' (test)?;


/*****************************************************************************/


/* Parser Rules: Compound Statements (compound_stmt) */
compound_stmt
    : if_stmt
    | while_stmt
    | for_stmt
    | func_def
    | class_def
    ;

if_stmt
    : 'if'    test ':' suite
      ('elif' test ':' suite)*
      ('else'      ':' suite)? 
    ;
while_stmt
    : 'while' test ':' suite
      ('else'      ':' suite)?
    ;
for_stmt
    : 'for' exprlist 'in' testlist ':' suite
      ('else' ':' suite)?
    ;

suite
    : simple_stmt
    | NEWLINE INDENT stmt+ DEDENT
    ;


/*****************************************************************************/


/* Parser Rules: Functions and Classes */

func_def
    : 'def' func_signature ':' suite
    ;
func_signature
    : name '(' func_parameter_list? ')' '->' typt_type
    ;
func_parameter_list
    : name ':' typt_type (',' name ':' typt_type)* ','?
    ;

// Pythonic:
//      class_def
//          : class_dec ':' suite
//          ;
class_def
    : class_dec ':' NEWLINE INDENT
            // class var decls
            (name ':' typt_type ('=' atom)? NEWLINE)*
        
            // constructor
            ('def' '__init__' '(' 'self' (',' func_parameter_list)? ')' ':' suite)?

            // methods/static methods
            // TODO: Are static methods viable with type system?
            (class_method | class_static_method)*
      DEDENT
    // The empty class
    | class_dec ':' NEWLINE INDENT
            pass_stmt NEWLINE
      DEDENT
    ;
class_dec
    : 'class' name ('(' name ')')?
    ;
class_method
    : ('def' name '(' 'self' (',' func_parameter_list)? ')' '->' typt_type ':' suite)
    ;
class_static_method
    : '@' 'staticmethod' NEWLINE
      ('def' name '(' func_parameter_list? ')' '->' typt_type ':' suite)
    ;


/*****************************************************************************/


/* Parser Rules: Tests and Expressions */
test        : or_test ;
or_test     : and_test ('or' and_test)* ;
and_test    : not_test ('and' not_test)* ;
not_test    : 'not' not_test | comparison ;
comparison  : expr (comp_op expr)* ;
comp_op     : '<'|'>'|'=='|'>='|'<='|'!='|'in'|'not' 'in'|'is'|'is' 'not' ;
expr        : xor_expr ('|' xor_expr)* ;
xor_expr    : and_expr ('^' and_expr)* ;
and_expr    : shift_expr ('&' shift_expr)* ;
shift_expr  : arith_expr (('<<'|'>>') arith_expr)* ;
arith_expr  : term (('+'|'-') term)* ;
term        : factor (('*'|'@'|'/'|'%'|'//') factor)* ;
factor      : ('+'|'-'|'~') factor | power ;
power       : atom_expr ('**' factor)? ;
atom_expr   : atom trailer* ;
atom
    : name
    | NUMBER
    | STRING
    | 'None'
    | 'True'
    | 'False'
    | 'self'    // TODO: Find a better way of allowing for self.x in a function call in a method
    ;
trailer: '(' (argument_list)? ')' | '[' subscriptlist ']' | '.' name;

subscriptlist: subscript (',' subscript)* (',')?;
subscript: test | (test)? ':' (test)? (sliceop)?;
sliceop: ':' (test)?;

exprlist : expr (',' expr)* (',')? ;
testlist : test (',' test)* (',')? ;


/*****************************************************************************/

/* Special Rules */
// NOTE: needed as NAME does not work directly in parser rules, idk why
name: NAME;

/*****************************************************************************/


/* Types System Parser Rules */
typt_type
    /* Base Types */
    : none_type         = 'None'
    | bool_type         = 'Bool'
    | int_type          = 'Int'
    | float_type        = 'Float'
    | string_type       = 'String'

    /* Object Types */
    | object_base_type  = 'Object'  // TODO: Should this be exposed?
    // TODO: Object type => [l_i : B_i] for i in 1..n
    | object_type='Object' '{' (name ':' typt_type) (',' name ':' typt_type)* '}'
    
    /* Function Types */
    // TODO: Consider syntax for function typt_type
    | typt_type '->' typt_type                          // 1-argument function
    | '<' typt_type (',' typt_type)* '>' '->' typt_type // n-argument function (n in 0..inf)

    /* Other */
    | list_type     = 'List'    '[' element_type=typt_type ']'
    | tuple_type    = 'Tuple'   '(' (typt_type (',' typt_type)*)? ')'
    | set_type      = 'Set'     '(' element_type=typt_type ')'
    | dict_type     = 'Dict'    '{' key_type=typt_type ',' index_type=typt_type '}'
    ;


/*****************************************************************************/


/* Lexer Rules */
NUMBER
    : INTEGER
    | FLOAT_NUMBER
    ;

STRING
    : SHORT_STRING
    | LONG_STRING
    ;

BOOLEAN
    : 'True'
    | 'False'
    ;

INTEGER
    : DECIMAL_INTEGER
    | OCT_INTEGER
    | HEX_INTEGER
    | BIN_INTEGER
    ;

// Newlines
NEWLINE
    : ( {self.at_start_of_line()}?   SPACES
    | ( '\r'? '\n' | '\r' | '\f' ) SPACES?
    )
    {
tempt = Lexer.text.fget(self)
newline = re.sub("[^\r\n\f]+", "", tempt)
spaces = re.sub("[\r\n\f]+", "", tempt)

la_char = ""
try:
    la_char = chr(self._input.LA(1))
except ValueError:
    # Occurs on EOF
    pass

if self.opened > 0 or la_char in ('\r', '\n', '\f', '#'):
    self.skip()
else:
    indent = self.get_indentation_count(spaces)
    previous = self.indents[-1] if self.indents else 0
    self.emitToken(self.common_token(self.NEWLINE, newline, indent=indent))
    
    if indent == previous:
        self.skip()
    elif indent > previous:
        self.indents.append(indent)
        self.emitToken(self.common_token(LanguageParser.INDENT, spaces))
    else:
        while self.indents and self.indents[-1] > indent:
            self.emitToken(self.create_dedent())
            self.indents.pop()
    
    }
    ;

// Identifiers/names
NAME            :   NAME_START NAME_CONTINUE*;

// Integers
DECIMAL_INTEGER : NON_ZERO_DIGIT DIGIT*
                | '0'+ ;
OCT_INTEGER     : '0' [oO] OCT_DIGIT+ ;
HEX_INTEGER     : '0' [xX] HEX_DIGIT+ ;
BIN_INTEGER     : '0' [bB] BIN_DIGIT+ ;

// Floats
FLOAT_NUMBER
    : INT_PART '.' FRACTION             // FLOAT_NUMBER ::= INT_PART '.' FRACTION
    | (INT_PART) EXPONENT               //              |   INT_PART              EXPONENT
    | (INT_PART '.' FRACTION) EXPONENT  //              |   INT_PART '.' FRACTION EXPONENT
    ;

// Skipable characters
SKIP_           : ( SPACES | COMMENT | LINE_JOINING ) -> skip ;

// Unknown character
UNKNOWN_CHAR    : . ;

/* Fragments */
// Identifer/name fragment
fragment NAME_START     : [a-zA-Z]   | '_' ;    // NAME_START       ::= 'a' ... 'f' | 'A' ... 'F' | '_'
fragment NAME_CONTINUE  : NAME_START | DIGIT ;  // NAME_CONTINUE    ::= 'a' ... 'f' | 'A' ... 'F' | '_' | DIGIT

// Numeric fragments
fragment NON_ZERO_DIGIT : [1-9] ;           // NON_ZERO_DIGIT   ::= '1' ... '9'
fragment DIGIT          : [0-9] ;           // DIGIT            ::= '0' ... '9'
fragment OCT_DIGIT      : [0-7] ;           // OCT_DIGIT        ::= '1' ... '7'
fragment HEX_DIGIT      : [0-9a-fA-F] ;     // HEX_DIGIT        ::= DIGIT | 'a' ... 'f' | 'A' ... 'F'
fragment BIN_DIGIT      : [01] ;            // BIN_DIGIT        ::= '0' | '1'

// Floating point fragments
fragment INT_PART   : DIGIT+ ;              // INT_PART ::= DIGIT+
fragment FRACTION   : DIGIT+ ;              // FRACTION ::= DIGIT+
fragment EXPONENT   : [eE] [+-]? DIGIT+ ;   // EXPONENT ::= ("e" | "E") ["+" | "-"]? DIGIT+

// String fragments
// SHORT_STRING         ::= ' SHORT_STRING_ITEM* '
//                      |   " SHORT_STRING_ITEM* "
// SHORT_STRING_ITEM    ::= SHORT_STRING_CHAR
//                      |   STRING_ESCAPE_SEQ
// SHORT_STRING_CHAR    ::= <any char except '\', '\n', '\''>
fragment SHORT_STRING
 : '\'' ( STRING_ESCAPE_SEQ | ~[\\\r\n\f'] )* '\''
 | '"' ( STRING_ESCAPE_SEQ | ~[\\\r\n\f"] )* '"'
 ;
fragment LONG_STRING
    : '\'\'\'' (LONG_STRING_ITEM)* '\'\'\'' // LONG_STRING          ::=  ''' LONG_STRING_ITEM* '''
    | '"""'    (LONG_STRING_ITEM)* '"""'    //                      |    """ LONG_STRING_ITEM* """
    ;
fragment LONG_STRING_ITEM
    : LONG_STRING_CHAR                      // LONG_STRING_ITEM     ::= LONG_STRING_CHAR
    | STRING_ESCAPE_SEQ                     //                      |   STRING_ESCAPE_SEQ
    ;
fragment LONG_STRING_CHAR   : ~'\\' ;       // LONG_STRING_CHAR     ::=  <any character except '\'>
fragment STRING_ESCAPE_SEQ  : '\\' .        // STRING_ESCAPE_SEQ    ::= '\' <any character>
                            | '\\' NEWLINE ;

// Spaces/comments
fragment SPACES         : [ \t]+ ;          // SPACES           ::= (' ' | '\t')+
fragment COMMENT        : '#' ~[\r\n\f]* ;

// Line joining
fragment LINE_JOINING   : '\\' SPACES? ( '\r'? '\n' | '\r' | '\f' ) ;
