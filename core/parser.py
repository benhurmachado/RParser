from sly import Parser
from core.lexer import RLexer

class RParser(Parser):
    tokens = RLexer.tokens
    debugfile = 'parser.out'

    precedence = ()

    def __init__(self):
        self.env = {}

    @_('statements')
    def program(self, p):
        return ('program', p.statements)

    @_('statements statement')
    def statements(self, p):
        return p.statements + [p.statement]

    @_('statement')
    def statements(self, p):
        return [p.statement]

    @_('assign')
    def statement(self, p):
        return p.assign

    @_('print_stmt')
    def statement(self, p):
        return p.print_stmt

    @_('cat_stmt')
    def statement(self, p):
        return p.cat_stmt

    @_('if_stmt')
    def statement(self, p):
        return p.if_stmt

    @_('ID ATRIB expr')
    def assign(self, p):
        return ('assign', p.ID, p.expr)

    @_('NUMBER')
    def expr(self, p):
        return ('number', int(p.NUMBER))

    @_('STRING')
    def expr(self, p):
        return ('string', p.STRING.strip('"'))

    @_('ID')
    def expr(self, p):
        return ('var', p.ID)

    @_('PRINT "(" expr ")"')
    def print_stmt(self, p):
        return ('print', p.expr)

    @_('CAT "(" expr ")"')
    def cat_stmt(self, p):
        return ('cat', p.expr)

    @_('IF "(" condition ")" "{" statements "}"')
    def if_stmt(self, p):
        return ('if', p.condition, p.statements)

    @_('expr GT expr',
       'expr LT expr',
       'expr GE expr',
       'expr LE expr',
       'expr EQ expr',
       'expr NE expr')
    def condition(self, p):
        return ('cond', p[1], p.expr0, p.expr1)

    def error(self, p):
        if p:
            print(f"Erro de sintaxe na linha {p.lineno}: token inesperado '{p.value}'")
        else:
            print("Erro de sintaxe no fim do arquivo")
