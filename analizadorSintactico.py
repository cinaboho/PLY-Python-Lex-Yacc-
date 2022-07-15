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
                  | operacion_logica
                  | condIf
                  | bucleDoWhile

    '''
def p_valor(p):
    '''valor : valorNumerico
             | CADENA
    '''

def p_varphp(p):
    '''varphp : VARIABLE_PHP'''

def p_valorNumerico(p):
    '''valorNumerico : ENTERO
                     | FLOTANTE
                     | varphp
                     | BOOLEANO

    '''
def p_operacion(p):
    '''operacion : valorNumerico
                 | valorNumerico operador operacion
                 | valorNumerico comparacion operacion
    '''
def p_operacion_logica(p):
    '''operacion_logica : varphp opLogicos varphp
    '''
def p_operador(p):
    '''operador : MAS
                | MENOS
                | MULTIPLICA
                | DIVIDE
                | MODULO
                | EXPONENCIACION
                
    '''
def p_comparacion(p):
    '''comparacion : MAYORQUE
                   | MENORQUE
                   | MENORQUE OPERASIGNACION
                   | MAYORQUE OPERASIGNACION
                   | MENORQUE OPERASIGNACION MAYORQUE
                   | MENORQUE MAYORQUE
    '''
def p_opLogicos(p) :
    '''   opLogicos : OPERLOGICO_AND
                    | OPERLOGICO_OR
                    | OPERLOGICO_XOR
                    | OPERLOGICO_NOT
                    | OPERLOGICO_OREXCLUSIVO
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

def p_condIf(p) :
    '''condIf : IF PARENIZQ BOOLEANO PARENDER PUNTOYCOMA
                | IF PARENIZQ BOOLEANO PARENDER LLAVEIZQ operacion LLAVEDER
                | IF PARENIZQ BOOLEANO PARENDER LLAVEIZQ print LLAVEDER
                | IF PARENIZQ BOOLEANO PARENDER LLAVEIZQ impresionEcho LLAVEDER'''

def p_bucleDoWhile(p):
    '''bucleDoWhile : DO LLAVEIZQ operacion LLAVEDER WHILE PARENIZQ BOOLEANO PARENDER PUNTOYCOMA
                    | DO LLAVEIZQ print LLAVEDER WHILE PARENIZQ BOOLEANO PARENDER PUNTOYCOMA
                    | DO LLAVEIZQ impresionEcho LLAVEDER WHILE PARENIZQ BOOLEANO PARENDER PUNTOYCOMA'''


#FUE PRESENTADO PERO FALTA VERIFICAR PARA CORREGIR

# def p_rellenoArray(p):  # clave => valor
#     '''rellenoArray : valores OPERASIG_ARRAY valores COMA
#                     | valores
#                     | COMA valores OPERASIG_ARRAY valores COMA rellenoArray'''


# def p_crearArreglos(p):
#     '''crearArreglos : variable OPERASIGNACION array PARENIZQ rellenoArray PARENDER PUNTOYCOMA'''


# def p_bucleForEach(p):
#     '''bucleForEach : variable IDENTIFICADOR variable LLAVEIZQ sentencias LLAVEDER
#                     | variable IDENTIFICADOR variable OPERASIG_ARRAY variable LLAVEIZQ sentencias LLAVEDER'''


# def p_metodosArray(p):
#     '''metodosArray : rsort PARENIZQ variable PARENDER PUNTOYCOMA
#                     | rsort PARENIZQ crearArreglos PARENDER PUNTOYCOMA
#                     | count PARENIZQ variable PARENDER PUNTOYCOMA
#                     | count PARENIZQ crearArreglos PARENDER PUNTOYCOMA'''

#Gabriela  -Corregido Cindy


resultadog = []


def p_error(p):
    print("Syntax error")
    resultadog.append("Syntax error".format(str(p.type), str(p.value)))


parser = yacc.yacc()


def prueba_s(data):
    global resultadog
    resultadog.clear()
    for item in data.splitlines():
        if item:
            gram = parser.parse(item)
            resultadog.append(str(gram))
    print("respuesta: ", resultadog)
    return resultadog


if __name__ == '__main__':
    while True:
        try:
            s = input(' ingresa dato >>> ')
        except EOFError:
            continue
        if not s:
            continue

        prueba_s(s)