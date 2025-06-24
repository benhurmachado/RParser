from sly import Parser
from core.lexer import RLexer

class RParser(Parser):
    tokens = RLexer.tokens
    debugfile = 'parser.out'

    precedence = (
        ('left', 'OR'),
        ('left', 'AND'),
        ('left', 'GT', 'LT', 'GE', 'LE', 'EQ', 'NE'),
        ('left', '+', '-'),
        ('left', '*', '/'),
    )

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

    @_('for_stmt')
    def statement(self, p):
        return p.for_stmt

    @_('ID ATRIB expr')
    def assign(self, p):
        return ('assign', p.ID, p.expr)

    @_('NUMBER')
    def expr(self, p):
        return ('number', float(p.NUMBER))

    @_('STRING')
    def expr(self, p):
        return ('string', p.STRING.strip('"').strip("'"))

    @_('ID')
    def expr(self, p):
        return ('var', p.ID)

    @_('expr "+" expr')
    def expr(self, p):
        return ('add', p.expr0, p.expr1)

    @_('expr "-" expr')
    def expr(self, p):
        return ('sub', p.expr0, p.expr1)

    @_('expr "*" expr')
    def expr(self, p):
        return ('mul', p.expr0, p.expr1)

    @_('expr "/" expr')
    def expr(self, p):
        return ('div', p.expr0, p.expr1)

    @_('CAT "(" expr ")"')
    def cat_stmt(self, p):
        return ('cat', p.expr)

    @_('PRINT "(" expr ")"')
    def print_stmt(self, p):
        return ('print', p.expr)

    @_('IF "(" condition ")" "{" statements "}"')
    def if_stmt(self, p):
        return ('if', p.condition, p.statements, None)

    @_('IF "(" condition ")" "{" statements "}" ELSE "{" statements "}"')
    def if_stmt(self, p):
        return ('if-else', p.condition, p.statements0, p.statements1)

    @_('FOR "(" ID IN expr ")" "{" statements "}"')
    def for_stmt(self, p):
        return ('for', p.ID, p.expr, p.statements)

    @_('expr GT expr',
       'expr LT expr',
       'expr GE expr',
       'expr LE expr',
       'expr EQ expr',
       'expr NE expr')
    def condition(self, p):
        return ('cond', p[1], p.expr0, p.expr1)

    @_('condition AND condition')
    def condition(self, p):
        return ('and', p.condition0, p.condition1)

    @_('condition OR condition')
    def condition(self, p):
        return ('or', p.condition0, p.condition1)

    @_('ID "(" expr_list ")"')
    def expr(self, p):
        return ('vector', p.ID, p.expr_list)

    @_('expr')
    def expr_list(self, p):
        return [p.expr]

    @_('expr "," expr_list')
    def expr_list(self, p):
        return [p.expr] + p.expr_list

    def error(self, p):
        if p:
            print(f"Erro de sintaxe na linha {p.lineno}: token inesperado '{p.value}'")
        else:
            print("Erro de sintaxe no fim do arquivo")