from core.lexer import RLexer
from core.parser import RParser

if __name__ == '__main__':
    lexer = RLexer()
    parser = RParser()
    debug_token_list = False
    
    while True:
        try:
            text = input('(RParser) >> ')
        except EOFError:
            break
        if text:
            token_list = lexer.tokenize(text)
            if debug_token_list:            
                for token in token_list:
                    print('type=%r, value=%r' % (token.type, token.value))
            parser.parse(token_list)