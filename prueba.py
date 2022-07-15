import ply.lex as lex
reserved = {"if" : "IF"}

tokens = ['PUNTOYCOMA',
          'VARIABLE' ] + list(reserved.values())

t_PUNTOYCOMA = r';'

def t_VARIABLE(t):
    #r'[a-zA-Z_][a-zA-Z0-9_]*'
    r'(\$[a-zA-Z_][a-zA-Z0-9_]* | [a-zA-Z_][a-zA-Z0-9_]*)'
    t.type = reserved.get(t.value, "VARIABLE")
    return t


def t_error(t):
    print("Caracter no reconocido {t.value[0]} en línea {t.lineno}")
    t.lexer.skip(1)

lexer = lex.lex()

def analizar(data):
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)


while True:
    data = input('>> ')
    analizar(data)
    if len(data)==0:
        break