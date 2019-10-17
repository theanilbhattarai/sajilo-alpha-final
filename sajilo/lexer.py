## Constants
import string
from index import Pos
from errors import *

NUMS = '0123456789'
CHARS = string.ascii_letters
ALPHANUM = NUMS + CHARS

## TOKENS
TT_INT = 'INT'
TT_FLOAT = 'FLOAT'
TT_STRING = 'STRING'
TT_IDENTIFIER = 'IDENTIFIER'
TT_KEYWORD = 'KEYWORD'
TT_PLUS = 'PLUS'
TT_MINUS = 'MINUS'
TT_MUL = 'MUL'
TT_DIV = 'DIV'
TT_POW = 'POW'
TT_EQ = 'EQ'
TT_LPAREN = 'LPAREN'
TT_RPAREN = 'RPAREN'
TT_EQUALS = 'EQUALS'
TT_NE = 'NOT EQUALS'
TT_LT = 'LESS THAN'
TT_LTE = 'LESS THAN EQUALS'
TT_GTE = 'GRT THAN EQUALS'
TT_GT = 'GRT THAN'
TT_COMMA = 'COMMA'
TT_ARROW = 'ARROW'
TT_EOF = 'EOF'

KEYWORDS = [
    'man', #let
    'ra', #and
    'athawa', #or
    'not', #not
    'yedi', #if
    'navaye', #else
    'loop', #for loop
    'lai', #in
    'jaba', #while
    'vidhi', #function
]

class Token:
    def __init__(self, type_, value = None, pos_start = None, pos_end = None):
        self.type = type_
        self.value = value 

        if pos_start:
            self.pos_start = pos_start.copy()
            self.pos_end = pos_start.copy()
            self.pos_end.advance()
        
        if pos_end:
            self.pos_end = pos_end.copy()
    
    def match(self, type_, value):
        return self.type == type_ and self.value == value
    
    def __repr__(self):
        if self.value: return f'{self.type} : {self.value}'
        return f'{self.type}'
    
## lexer class

class Lexer:
    def __init__(self, file_name, text):
        self.file_name = file_name
        self.text = text 
        self.pos = Pos(-1,0,-1,file_name, text)
        self.current_char = None
        self.advance()
    
    def advance(self):
        self.pos.advance(self.current_char)
        self.current_char = self.text[self.pos.index] if self.pos.index < len(self.text) else None
    
    def make_tokens(self):
        tokens = []

        while self.current_char != None:
            if self.current_char in '\t':
                self.advance()
            elif self.current_char in ' ':
                self.advance()
            elif self.current_char in NUMS:
                tokens.append(self.make_nums())               
            elif self.current_char in CHARS:
                tokens.append(self.make_identifier())               
            elif self.current_char == '"':
                tokens.append(self.make_strings())
            elif self.current_char == '+':
                tokens.append(Token(TT_PLUS, pos_start = self.pos))
                self.advance()
            elif self.current_char == '-':
                tokens.append(self.make_minus_or_arrow())
            elif self.current_char == '*':
                tokens.append(Token(TT_MUL, pos_start = self.pos))
                self.advance()
            elif self.current_char == '/':
                tokens.append(Token(TT_DIV, pos_start = self.pos))
                self.advance()
            elif self.current_char == '^':
                tokens.append(Token(TT_POW, pos_start = self.pos))
                self.advance()
            elif self.current_char == '(':
                tokens.append(Token(TT_LPAREN), pos_start = self.pos)
                self.advance()
            elif self.current_char == ')':
                tokens.append(Token(TT_RPAREN),pos_start = self.pos)
                self.advance()
            elif self.current_char == '!':
                token, error = self.make_not_equals()
                if error: return [], error
                tokens.append(token)
            elif self.current_char == '=':
                tokens.append(self.make_equals())
            elif self.current_char == '<':
                tokens.append(self.make_less_than())
            elif self.current_char == '>':
                tokens.append(self.make_greater_than())
            elif self.current_char == ',':
                tokens.append(Token(TT_COMMA, pos_start = self.pos))
                self.advance()
            else:
                pos_start = self.pos.copy()
                char = self.current_char
                self.advance()
                return [], IllegalCharError(pos_start, self.pos, "'" + char + "'")
        tokens.append(Token(TT_EOF, pos_start= self.pos))
        return tokens, None

    
    #make numbers
    def make_nums(self):
        num_str = ''
        dot_count = 0
        pos_start = self.pos.copy()

        while self.current_char != None and self.current_char in NUMS + '.':
            if self.current_char == '.':
                if dot_count == 1: break
                dot_count += 1
            num_str += self.current_char
            self.advance()
        if dot_count == 0:
            return Token(TT_INT, int(num_str), pos_start, self.pos)
        else:
            return Token(TT_FLOAT, float(num_str), pos_start, self.pos)
        

    #make identifier
    def make_identifier(self):
        id_str = ''
        pos_start = self.pos.copy()

        while self.current_char != None and self.current_char in ALPHANUM + '_':
            id_str += self.current_char
            self.advance()
        token_type = TT_KEYWORD if id_str in KEYWORDS else TT_IDENTIFIER
        return Token(token_type, id_str, pos_start, self.pos)

    #make strings char by char
    def make_strings(self):
        string = ''
        pos_start = self.pos.copy()
        escape_char = False
        self.advance()

        escape_chars = {
            'n' : '\n',
            't' : '\t',  
        }

        while self.current_char != None and (self.current_char != "'" or escape_char):
            if escape_char:
                string += escape_chars.get(self.current_char, self.current_char)
            else:
                if self.current_char == '\\':
                    escape_char = True
                else:
                    string += self.current_char
            self.advance()
            escape_char = False
        
        self.advance()
        return Token(TT_STRING, string, pos_start, self.pos)

    ##make minus or arrow
    def make_minus_or_arrow(self):
        token_type = TT_MINUS
        pos_start = self.pos.copy()
        self.advance()

        if self.current_char == '>':
            self.advance()
            token_type = TT_ARROW
        
        return Token(token_type, pos_start=pos_start, pos_end = self.pos)

    def make_not_equals(self):
        pos_start = self.pos.copy()
        
        #move one step
        self.advance()
        # because not equals looks like '!='
        if self.current_char == '=':
            self.advance()
            return Token(TT_NE, pos_start=pos_start, pos_end = self.pos), None
        
    
    def make_equals(self):
        token_type = TT_EQ

        pos_start = self.pos.copy()

        self.advance()

        if self.current_char == '=':
            self.advance()
            token_type = TT_EQUALS
        return Token(token_type, pos_start = pos_start, pos_end = self.pos)
    
    def make_less_than(self):
        token_type = TT_LT

        pos_start = self.pos.copy()
        if self.current_char == '=':
            self.advance()
            token_type = TT_LTE
        return Token(token_type, pos_start = pos_start, pos_end = self.pos)
    
    def make_greater_than(self):
        token_type = TT_GT 
        pos_start = self.pos.copy()

        self.advance()

        if self.current_char == '=':
            self.advance()
            token_type = TT_GTE
        return Token(token_type, pos_start = pos_start, pos_end = self.pos)
    
    


