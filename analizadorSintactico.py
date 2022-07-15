import ply.yacc as yacc
from analizadorLexico import tokens
#Gabriela --Correegido Cindy
def p_sentencias(p):
    '''sentencias : valor
                  | operacion
                  | asignacion
                  | asignacion_abreviatura_op
                  | print
                  | impresionEcho
    '''
def p_valor(p):
    '''valor : valorNumerico
             | CADENA
    '''
def p_valorNumerico(p):
    '''valorNumerico : ENTERO
                     | FLOTANTE
                     | VARIABLE_PHP
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
    '''asignacion : VARIABLE_PHP OPERASIGNACION valor
    '''
def p_asignacion_abreviado(p):
    '''asignacion_abreviado : MASIGUAL
                            | MENOSIGUAL
                            | ASTERISCOIGUAL
                            | BARRAIGUAL
                            | PORCENTAJEIGUAL
                            | DOBLEASTERISCOIGUAL
    '''
def p_asignacion_abreviatura_op(p):
    '''asignacion_abreviatura_op : VARIABLE_PHP asignacion_abreviado valorNumerico
    '''
def p_print(p):
    '''print : PRINT PARENIZQ PARENDER PUNTOYCOMA
             | PRINT PARENIZQ COMDOB  COMDOB PARENDER PUNTOYCOMA
             | PRINT PARENIZQ COMDOB  valor COMDOB PARENDER PUNTOYCOMA
    '''
def p_impresionEcho(p):
    '''impresionEcho : ECHO CADENA PUNTOYCOMA'''

def p_variable_dolar(p):
    '''variable_dolar : VARIABLE_PHP'''


#Gabriela  -Corregido Cindy




def p_error(p):
    print("Syntax error")

parser = yacc.yacc()
while True:
    try:
        s = input("calc>")
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)
    