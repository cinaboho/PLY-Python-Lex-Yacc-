import ply.yacc as yacc
from analizadorLexico import tokens

def p_sentencias(p):
    '''sentencias : valor
    '''
def p_valor(p):
    '''valor : BOOLEANO
             | CADENA
             | ENTERO
             | FLOTANTE
             | VARIABLE
    '''

def p_error(p):
    print("Syntax error")

parser = yacc.yacc()

while True:
    try:
        s = input("calc >")
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)