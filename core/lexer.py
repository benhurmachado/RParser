from sly import Lexer

class RLexer(Lexer):
    tokens = { ID, NUMBER, STRING, IF, PRINT, CAT, ATRIB, GT, LT, GE, LE, EQ, NE }
    literals = { '(', ')', '{', '}' }

    ignore = ' \t'
    ignore_comment = r'#.*'

    ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
    ID['if'] = IF
    ID['print'] = PRINT
    ID['cat'] = CAT

    ATRIB = r'<-'
    NUMBER = r'\d+'
    STRING = r'\".*?\"'

    GT = r'>'
    LT = r'<'
    GE = r'>='
    LE = r'<='
    EQ = r'=='
    NE = r'!='

    @_(r'\n+')
    def newline(self, t):
        self.lineno += len(t.value)

    def error(self, t):
        print(f"Caractere ilegal: {t.value[0]}")
        self.index += 1
