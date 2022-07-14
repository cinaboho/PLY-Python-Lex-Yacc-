import ply.yacc as yacc
from analizadorLexico import tokens

def p_sentencias(p):
    '''sentencias : valor
                  | operacion

    '''
def p_valor(p):
    '''valor : valorNumerico
             | CADENA
    '''
def p_valorNumerico(p):
    '''valorNumerico : ENTERO
                     | FLOTANTE
                     | VARIABLE
                     | BOOLEANO
    '''
def p_operacion(p):
    '''operacion : valorNumerico
            | valorNumerico operador operacion
    '''
def p_operador(p):
    '''operador : MAS
                | MENOS
                | MULTIPLICA
                | DIVIDE
                | MODULO
                | EXPONENCIACION
    '''
def p_asignacion(p):
    '''asignacion : VARIABLE OPERASIGNACION VALOR
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