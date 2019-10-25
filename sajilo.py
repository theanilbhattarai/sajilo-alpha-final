from sajilo import Lexer

def run(file_name,text):
    lexer = Lexer(file_name,text)
    tokens, error = lexer.make_tokens()
    return tokens, error

