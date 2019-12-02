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
@lexer::header{
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
program: (NEWLINE | stmt)* EOF;

// Parameters
parameters : '(' (parameter_list)? ')' ;

parameter_list
    : named_parameter       (',' named_parameter)*      (',' default_parameter)*
    | default_parameter     (',' default_parameter)*
    ;

named_parameter     : 'name : Type' ;
default_parameter   : 'name : Type = value' ;


// Statements
stmt: '(' 'def' ')' NEWLINE | 'if' 'test' ':' suite ;

simple_stmt
    : small_stmt (';' small_stmt)* (';')? NEWLINE
    ;

small_stmt
    : expr_stmt
    // | del_stmt
    // | pass_stmt
    // // | flow_stmt
    // // | import_stmt
    // // | global_stmt
    // // | nonlocal_stmt
    // // | assert_stmt
    ;

expr_stmt : ;

// compound_stmt
//     : if_stmt
//     | while_stmt
//     | for_stmt
//     // | try_stmt
//     // | with_stmt
//     | funcdef
//     | classdef
//     // | decorated
//     // | async_stmt
//     ;

suite
    : simple_stmt
    | NEWLINE INDENT stmt+ DEDENT
    ;

/* Type system parser rules */
base_types
    : 'Bool'
    | 'Int'
    | 'Float'
    | 'String'
    | 'Dynamic'
    ;

// type
//     : base_types
//     | CLASS_NAME
//     | 'List(' type ')' | 'Tuple(' type ')' | 'Set(' type ')' | 'Dict(' type ')'
//     | 'Object(' CLASS_NAME '){' LABEL ':' type '}'
//     | 'Class(' CLASS_NAME '){' LABEL ':' type '}'
//     | 'Function(' parameter_type ',' type ')'
//     ;

// parameter_type
//     : 'Arb'
//     | 'Pos(' type ')'
//     | 'Named(' LABEL ':' type ')'
//     ;

/* Lexer Rules */
DEF : 'def';

NUMBER  : INTEGER;

INTEGER
    : DECIMAL_INTEGER
    | OCT_INTEGER
    | HEX_INTEGER
    | BIN_INTEGER
    ;

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


// Python rules
DECIMAL_INTEGER : NON_ZERO_DIGIT DIGIT*
                | '0'+ ;
OCT_INTEGER     : '0' [oO] OCT_DIGIT+ ;
HEX_INTEGER     : '0' [xX] HEX_DIGIT+ ;
BIN_INTEGER     : '0' [bB] BIN_DIGIT+ ;

// Skipable characters
SKIP_           : ( SPACES | COMMENT | LINE_JOINING ) -> skip ;

// Unknown character
UNKNOWN_CHAR    : . ;

/* Fragments */
// Numeric fragments
fragment NON_ZERO_DIGIT : [1-9] ;           // NON_ZERO_DIGIT   ::= '1' ... '9'
fragment DIGIT          : [0-9] ;           // DIGIT            ::= '0' ... '9'
fragment OCT_DIGIT      : [0-7] ;           // OCT_DIGIT        ::= '1' ... '7'
fragment HEX_DIGIT      : [0-9a-fA-F] ;     // HEX_DIGIT        ::= digit | 'a' ... 'f' | 'A' ... 'F'
fragment BIN_DIGIT      : [01] ;            // BIN_DIGIT        ::= '0' | '1'

// Floating point fragments
fragment INT_PART   : DIGIT+ ;              // INT_PART ::= digit+
fragment FRACTION   : DIGIT+ ;              // FRACTION ::= digit+
fragment EXPONENT   : [eE] [+-]? DIGIT+ ;   // EXPONENT ::= ("e" | "E") ["+" | "-"]? digit+

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
