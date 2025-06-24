from sly import Lexer

class RLexer(Lexer):
    tokens = {
        ID, NUMBER, STRING,
        IF, ELSE, FOR, IN,
        PRINT, CAT,
        ATRIB, GT, LT, GE, LE, EQ, NE,
        AND, OR
    }
    literals = { '(', ')', '{', '}', '+', '-', '*', '/', ',' }

    ignore = ' \t'
    ignore_comment = r'#.*'

    ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
    ID['if'] = IF
    ID['else'] = ELSE
    ID['for'] = FOR
    ID['in'] = IN
    ID['print'] = PRINT
    ID['cat'] = CAT

    ATRIB = r'<-'
    GE = r'>='
    LE = r'<='
    EQ = r'=='
    NE = r'!='
    GT = r'>'
    LT = r'<'
    AND = r'&&'
    OR = r'\|\|'

    NUMBER = r'\d+(\.\d+)?([eE][+-]?\d+)?'

    STRING = r'\".*?\"|\'.*?\''

    @_(r'\n+')
    def newline(self, t):
        self.lineno += t.value.count('\n')

    def error(self, t):
        print(f"Caractere ilegal: {t.value[0]} na linha {self.lineno}")
        self.index += 1