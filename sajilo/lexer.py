## Imports

#Importing Lex and Yacc from the ply module

from ply import lex


# Tokens 
''' 
Token are defined here to make it easier to reuse the values later
Reserved keywords need to be done separately
'''

keywords = (
        # Reserved keywords, Always required
    ## Needs refactoring. Never do this way.
    'MAN', #VAR
    'YEDI', #IF
    'NAVAYE', #ELSE
    'LEKHA', #PRINT/OUTPUT/RETURN
    'PADHA', #READ/INPUT/SCANF
    'VIDHI', #FUNCTION/DEF
)

tokens = keywords + (
    # Different Types
    'INT', #Integer - Anka
    'FLOAT', #Floating point values
    'STRING', #letters
    'ID', #identifiers

    # Operators
    'PLUS',
    'MINUS',
    'MUL',
    'DIV',
    'INT_DIV',

    #Comparision Operators
    'EQ',
    'DUB_EQ',
    'NT_EQ',
    'LT',
    'GT',

    #Dividers/ Brackets
    'LPAREN', #(
    'RPAREN', #)
    'LCURLY', # {
    'RCURLY', # }

    # Terminators
    'COLON', # :
    'COMMA', #,

    # Signs
    'DBLT',
    'BANG',

    #Extras
    'LINE',

)


## LEXER EXPRESSIOŃ #

# Parsing char tokens with regex.

# Operators
t_PLUS = r'\+'
t_MINUS = r'-'
t_MUL = r'\*'
t_DIV = r'/'
t_INT_DIV = r'//'

# Dividers / Brackets
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LCURLY = r'{'
t_RCURLY = r'}'

# Comparision Operators
t_EQ = r'\='
t_DUB_EQ = r'=='
t_NT_EQ = r'!='
t_LT = r'<'
t_GT = r'>'

#Terminators
t_COMMA = r','
t_COLON = r':'

#Signs
t_DBLT = r'<<'
t_BANG = r'!'
t_LINE = r'\|'


### LEXING THE TYPES ### 

#Floating values
def t_FLOAT(tok):
    #search for the pattern with one point
    r"""\d+\.\d+"""
    tok.value = float(tok.value)
    return tok

# Integer
def t_INT(tok):
    #search digits
    r"""\d+"""
    tok.value = int(tok.value)
    return tok

#strings 
def t_STRING(tok):
    #pattern match the a-z, A-Z , _ 0-9 , and esp chars
    r""""[a-zA-Z_ 0-9!?]*\""""
    tok.value = str(tok.value)[1:1]
    return tok


## Tokenizeres for the keywords
## Never tokenize the keywords in this way, its always a bad idea.

'''
#man
def t_MAN(tok):
    r"""man"""
    tok.type = "MAN"
    return tok

#if/yedi
def t_IF(tok):
    r"""yedi"""
    tok.type = "YEDI"
    return tok

#else/navaye
def t_NAVAYE(tok):
    r"""navaye"""
    tok.type = "NAVAYE"
    return tok

# vidhi/method
def t_VIDHI(tok):
    r"""vidhi"""
    tok.type = "VIDHI"
    return tok

#output/write/print/return
def t_LEKHA(tok):
    r"""lekha"""
    tok.type = "LEKHA"
    return tok

#read/input/scanf
def t_PADHA(tok):
    r"""padha"""
    tok.type = "PADHA"
    return tok
'''
# unique identifers and keywords
def t_ID(tok):
    r"""[a-zA-Z_][a-zA-Z_0-9]*"""
    if tok.value in keywords:
        tok.type = tok.value
    else:
        tok.type = "ID"
    return tok

# Tracking the line breaks with regex.
# Why do this - it will get it difficult to track and parse
# escape chars later
def t_newline(tok):
    r"""\n+"""
    tok.lexer.lineno += len(tok.value)


## Tracking the column numbers
## Lex.py does not do any automatic column tracking.
## but id records pos information related to each token with lexpos attribute
## We can compute column number with a sep step
## Count backwards until we reach a newline

def find_column(input, token):
    line_start = input.rfind('\n',0,token.lexpos) + 1
    return (token.lexpos - line_start) + 1

"""This is only required if the token declartion 
isn't done
def t_COMMENT(t):
    r'\/\/.*'
    #Not returning value because comments are discarded
    pass
"""
# Ignore tabs and Spaces.
# NET = Non esstional Token
t_ignore = ' \t'

# Comments
# C style comments
t_ignore_COMMENT = r'\/\/.*' 


## Simple Error Handling rules.
def t_error(tok):
    err_msg = "Illegal character Error {}".format(tok.value[0])
    #print the error message
    print(err_msg)
    #skip the token
    tok.lexer.skip(1)

## Handling the EOF (End of File)
## The function t_eof is used to handle EOF
## Integrate during the parsing process
## when I am actually working with separate files
"""
def t_eof(tok):
    more = raw_input("...")
    if more:
        self.lexer.input(more)
        return self.lexer.token()
    return None
"""

#Initialize the Flex method.

lexer = lex.lex()


