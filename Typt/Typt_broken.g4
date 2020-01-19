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

/* Parser Rules */
// TODO: fix
// TODO: VALUE to atom
// program: (NEWLINE | using)* (NEWLINE | stmt)* EOF;
program: (NEWLINE | stmt)* EOF;

// Using
// Using is for specifing imports from Python
using
    : 'using' ':'
            NEWLINE INDENT (funcdec NEWLINE)+ DEDENT
      'from' NAME ('as' NAME)?
    ;

// Parameters
parameters : '(' (parameter_list)? ')' ;
parameter_list
    : parameter (',' parameter)*
    ;
parameter           : required_parameter | default_parameter ;
required_parameter  : NAME ':' typt_type ;
default_parameter   : NAME ':' typt_type '=' VALUE ;

// Arguments
arguments       : '(' (argument_list)? ')' ;
argument_list   : argument (',' argument)* ;
argument
    : NAME
    | test
    | NAME '=' test
    ;

// Statements
// expr_stmt: testlist_star_expr
//              (annassign
//              | augassign (yield_expr|testlist)
//              | ('=' (yield_expr|testlist_star_expr))*
//              )
//          ;
// annassign: ':' test ('=' test)?;
// testlist_star_expr: (test|star_expr) (',' (test|star_expr))* (',')?;
// augassign: ('+=' | '-=' | '*=' | '@=' | '/=' | '%=' | '&=' | '|=' | '^=' |
//             '<<=' | '>>=' | '**=' | '//=');
stmt
    : simple_stmt
    | compound_stmt 
    ;

// Simple statements
// simple_stmt
//     : small_stmt (';' small_stmt)* (';')? NEWLINE
//     ;
simple_stmt
    : small_stmt NEWLINE
    ;

small_stmt
    : expr_stmt
    | var_dec_stmt
    | del_stmt
    | pass_stmt
    | flow_stmt
    | import_stmt
    ;

expr_stmt
    : test (',' test)* (',')? (anassign | augassign) test
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
    : typt_type NAME
    | typt_type NAME '=' test
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
return_stmt     : 'return' (testlist)?;

import_stmt
    : 'from' import_from 'import' import_name
    ;
import_from
    : NAME
    | ('../')+ NAME ('/' NAME)*
    ;
import_name
    : NAME
    | NAME 'as' NAME
    ;

// Compound statements
compound_stmt
    : if_stmt
    | while_stmt
    | for_stmt
    | funcdef
    | classdef
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
for_stmt    // TODO: Hmm
    : 'for' exprlist 'in' testlist ':' suite
      ('else' ':' suite)?
    ;

funcdef
    : funcdec ':' suite
    ;
funcdec
    : 'def' NAME parameters '->' typt_type
    ;

classdef
    : classdec ':' suite
    ;
classdec
    : 'class' NAME ('(' NAME? ')')?
    ;

suite
    : simple_stmt
    | NEWLINE INDENT stmt+ DEDENT
    ;

/*****************************************************************************/
// Expressions
// test: or_test ('if' or_test 'else' test)? ;  // For ternary operators
test        : or_test ;
or_test     : and_test ('or' and_test)* ;
and_test    : not_test ('and' not_test)* ;
not_test    : 'not' not_test | comparison ;
comparison  : expr (comp_op expr)* ;
comp_op     : '<'|'>'|'=='|'>='|'<='|'<>'|'!='|'in'|'not' 'in'|'is'|'is' 'not' ;
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
    : NAME
    | NUMBER
    | STRING+
    | '...'
    | 'None'
    | 'True'
    | 'False'
    ;
trailer: '(' (argument_list)? ')' | '[' subscriptlist ']' | '.' NAME;

// testlist_comp: (test|star_expr) ( comp_for | (',' (test|star_expr))* (',')? );

subscriptlist: subscript (',' subscript)* (',')?;
subscript: test | (test)? ':' (test)? (sliceop)?;
sliceop: ':' (test)?;

// exprlist: (expr|star_expr) (',' (expr|star_expr))* (',')?;
// testlist: test (',' test)* (',')?;
exprlist : expr (',' expr)* (',')? ;
testlist : test (',' test)* (',')? ;

// test_nocond: or_test | lambdef_nocond;
// lambdef_nocond: 'lambda' (parameter_list)? ':' test_nocond;

// comp_iter: comp_for | comp_if;
// comp_for: 'for' exprlist 'in' or_test (comp_iter)?;
// comp_if: 'if' test_nocond (comp_iter)?;

/*****************************************************************************/

/* Type system parser rules */
typt_type
    : base_types
    | 'List[' typt_type ']'
    | 'Tuple(' typt_type ')'
    | 'Set(' typt_type ')'
    | 'Dict{' typt_type '}'
    | NAME                                      // Class/typedef
    | 'Function' typed_parameters_noassign      // Function
    ;

base_types
    : 'Bool'
    | 'Int'
    | 'Float'
    | 'String'
    ;

typed_parameters_noassign
    : '(' (typed_parameter_list_noassign)? ')'
    ;
typed_parameter_list_noassign
    : typt_type (',' typt_type)*
    ;

// parameter_type
//     : 'Arb'
//     | 'Pos(' typt_type ')'
//     | 'Named(' NAME ':' typt_type ')'
//     ;

/* Lexer Rules */
VALUE
    : NAME
    | NUMBER
    | STRING
    | BOOLEAN
    | NONE
    ;

NUMBER
    : INTEGER
    | FLOAT_NUMBER
    ;

STRING
    : SHORT_STRING
    | LONG_STRING
    ;

BOOLEAN
    : TRUE
    | FALSE
    ;

INTEGER
    : DECIMAL_INTEGER
    | OCT_INTEGER
    | HEX_INTEGER
    | BIN_INTEGER
    ;

// Keywords
USING       : 'using';
DEF         : 'def';
RETURN      : 'return';
IMPORT      : 'import';
IF          : 'if';
ELIF        : 'elif';
ELSE        : 'else';
WHILE       : 'while';
FOR         : 'for';
IN          : 'in';
OR          : 'or';
AND         : 'and';
NOT         : 'not';
IS          : 'is';
CLASS       : 'class';
DEL         : 'del';
PASS        : 'pass';
CONTINUE    : 'continue';
BREAK       : 'break';
NONE        : 'None';
TRUE        : 'True';
FALSE       : 'False';

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


// Operators
DOT         : '.';
ELLIPSIS    : '...';
STAR        : '*';
COMMA       : ',';
COLON       : ':';
SEMI_COLON  : ';';

// Arithmetic operators
AND_OP      : '&';
OR_OP       : '|';
XOR_OP      : '^';
NOT_OP      : '~';
POWER       : '**';
LEFT_SHIFT  : '<<';
RIGHT_SHIFT : '>>';
ADD         : '+';
MINUS       : '-';
DIV         : '/';
MOD         : '%';
IDIV        : '//';

// Parentheses, brackets, and braces
OPEN_PARENTHESIS    : '('   {self.opened += 1} ;
CLOSE_PARENTHESIS   : ')'   {self.opened -= 1} ;
OPEN_BRACKET        : '['   {self.opened += 1} ;
CLOSE_BRACKET       : ']'   {self.opened -= 1} ;
OPEN_BRACE          : '{'   {self.opened += 1} ;
CLOSE_BRACE         : '}'   {self.opened -= 1} ;

// Comparision operators
LESS_THAN       : '<';
GREATER_THAN    : '>';
EQUALS          : '==';
GT_EQ           : '>=';
LT_EQ           : '<=';
NOT_EQ_1        : '<>';
NOT_EQ_2        : '!=';
AT              : '@';
ARROW           : '->';

// Assignment operators
ASSIGN              : '=';
ADD_ASSIGN          : '+=';
SUB_ASSIGN          : '-=';
MULT_ASSIGN         : '*=';
AT_ASSIGN           : '@=';
DIV_ASSIGN          : '/=';
MOD_ASSIGN          : '%=';
AND_ASSIGN          : '&=';
OR_ASSIGN           : '|=';
XOR_ASSIGN          : '^=';
LEFT_SHIFT_ASSIGN   : '<<=';
RIGHT_SHIFT_ASSIGN  : '>>=';
POWER_ASSIGN        : '**=';
IDIV_ASSIGN         : '//=';

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
