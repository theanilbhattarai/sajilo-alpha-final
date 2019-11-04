
def token_append(self,token_type):
    tokens.append(Token(token_type, pos_start = self.pos))
    self.advance
def default_parse(self):
            pos_start = self.pos.copy()
            char = self.current_char
            self.advance()
            return [], IllegalCharError(pos_start, self.pos, "'" + char + "'")

parse_actions = {
    '\t' : lambda : self.advance(),
    ' ' : lambda : self.advance(),
    '"' : lambda : tokens.append(self.make_string()),
    '-' : lambda : tokens.append(self.make_minus_or_arrow()),
    '!' : lambda : tokens.append(self.make_not_equals()),
    '=' : lambda : tokens.append(self.make_equals()),
    '<' : lambda : tokens. append(self.make_less_than()),
    '>' : lambda : tokens.append(self.make_greater_than()),
    "+" : lambda : self.token_append(tokens,TT_PLUS),
    '/' : lambda : self.token_append(tokens,TT_DIV),
    ',' : lambda : self.token_append(tokens,TT_COMMA),
    '*' : lambda : self.token_append(tokens,TT_MUL),
    '^' : lambda : self.token_append(tokens, TT_POW),

}

parse_actions.get(current_char, self.default_parse)()