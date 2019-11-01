grammar Typt;

/* Reference - https://github.com/antlr/grammars-v4/blob/master/python3-py/Python3.g4 */

tokens { INDENT, DEDENT }

@lexer::header{
    from antlr4.Token import CommonToken
    import re
    import importlib

    # Allow languages to extend the lexer and parser, by loading the parser
    # dynamically
    module_path = __name__[:-5]
    language_name = __name__.split('.')[-1]
    language_name = language_name[:-5]  # Remove Lexer from name
    LanguageParser = getattr(
        importlib.import_module('{}Parser'.format(module_path)),
        '{}Parser'.format(language_name)
    )
}

/* Parser rules */
program
    : (NEWLINE | stmt)* EOF
    ;

stmt
    : simple_stmt
    | compound_stmt
    ;

simple_stmt : '(' DEF ')';
compound_stmt : '[' RETURN ']';

/* Lexer rules */
DEF : 'def';
RETURN : 'return';
RAISE : 'raise';
FROM : 'from';
IMPORT : 'import';
AS : 'as';
GLOBAL : 'global';
NONLOCAL : 'nonlocal';
ASSERT : 'assert';
IF : 'if';
ELIF : 'elif';
ELSE : 'else';
WHILE : 'while';
FOR : 'for';
IN : 'in';
TRY : 'try';
FINALLY : 'finally';
WITH : 'with';
EXCEPT : 'except';
LAMBDA : 'lambda';
OR : 'or';
AND : 'and';
NOT : 'not';
IS : 'is';
NONE : 'None';
TRUE : 'True';
FALSE : 'False';
CLASS : 'class';
YIELD : 'yield';
DEL : 'del';
PASS : 'pass';
CONTINUE : 'continue';
BREAK : 'break';
ASYNC : 'async';
AWAIT : 'await';

NEWLINE
    : '\r'? '\n'
    | '\n'
    ;


/* Fragments */
fragment NON_ZERO_DIGIT
    : [1-9]
    ;

fragment DIGIT
    : [0-9]
    ;

fragment SPACES
    : [ \t]+
    ;

fragment COMMENT
    : '#' ~[\r\n\f]*
    ;
