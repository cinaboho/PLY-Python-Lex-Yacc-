import ply.yacc as yacc
from analizadorLexico import tokens

def p_sentencias(p):
    '''sentencias : valor
                  | suma
    '''
def p_valor(p):
    '''valor : valorNumerico
             | CADENA
             | BOOLEANO
    '''
def p_valorNumerico(p):
    '''valorNumerico : ENTERO
                     | FLOTANTE
                     | VARIABLE
    '''
def p_suma(p):
    '''suma : valorNumerico
            | valorNumerico operador suma
    '''
def p_operador(p):
    '''operador : MAS
                | MENOS
                | MULTIPLICA
                | DIVIDE
                | MODULO
                | EXPONENCIACION
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