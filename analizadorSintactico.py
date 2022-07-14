import ply.yacc as yacc
from analizadorLexico import tokens

def p_sentencias(p):
    '''sentencias : valor
                  | operacion
                  | asignacion
                  | asignacion_abreviatura_op

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
    '''asignacion : VARIABLE OPERASIGNACION valor
    '''
def p_asignacion_abreviado(p):
    '''asignacion_abreviado : MASIGUAL
                            | MENOSIGUAL
                            | ASTERISCOIGUAL
                            | BARRAIGUAL
    '''
def p_asignacion_abreviatura_op(p):
    '''asignacion_abreviatura_op : VARIABLE asignacion_abreviado valorNumerico
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