class Pos:
    def __init__(self,index,line, col, file_name, f_text):
        self.index = index
        self.line = line
        self.col = col
        self.file_name = file_name
        self.f_text = f_text
    
    def advance(self, current_char = None):
        self.index += 1
        self.col += 1

        if current_char == '\n':
            self.line += 1
            self.col = 0

        return self
    
    def copy(self):
        return Pos(self.index,self.line, self.col, self.file_name, self.f_text)