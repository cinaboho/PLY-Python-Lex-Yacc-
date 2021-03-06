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
                  | rellenoArray
                  | inicio
                  | fin
                  | comentario_largo
                  | lista
                  | asignarvalores
    '''

def p_inicio(p):
    '''inicio : INICIO
    '''
def p_fin(p):
    '''fin : FIN
    '''
def p_comentario_largo(p):
    '''comentario_largo : COMENTARIO_LARGO
    '''

def p_valor(p):
    '''valor : valorNumerico
             | CADENA'''

def p_varphp(p):
    '''varphp : VARIABLE_PHP'''

def p_valorNumerico(p):
    '''valorNumerico : ENTERO
                     | FLOTANTE
                     | varphp
                     | BOOLEANO
    '''
def p_operacion(p):
    '''operacion : valorNumerico PUNTOYCOMA
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
                   | MENORQUE IGUAL
                   | MAYORQUE IGUAL
                   | MENORQUE IGUAL MAYORQUE
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
    '''asignacion : VARIABLE_PHP IGUAL valor PUNTOYCOMA
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
    '''asignacion_abreviatura_op : VARIABLE_PHP asignacion_abreviado valorNumerico PUNTOYCOMA
    '''
#print();
#print("");
#print $a;
#print("Hola mundo 1");

def p_print(p):
    '''print : PRINT PARENIZQ PARENDER PUNTOYCOMA
                | PRINT PARENIZQ COMDOB COMDOB PARENDER PUNTOYCOMA
                | PRINT PARENIZQ CADENA PARENDER PUNTOYCOMA'''

def p_impresionEcho(p):
    '''impresionEcho : ECHO CADENA PUNTOYCOMA'''

def p_condIf(p) :
    '''condIf : IF PARENIZQ BOOLEAN PARENDER PUNTOYCOMA
                | IF PARENIZQ BOOLEAN PARENDER LLAVEIZQ operacion LLAVEDER
                | IF PARENIZQ BOOLEAN PARENDER LLAVEIZQ print LLAVEDER
                | IF PARENIZQ BOOLEAN PARENDER LLAVEIZQ impresionEcho LLAVEDER
    '''
#do{$a+$b}while(True);

def p_bucleDoWhile(p):
    '''bucleDoWhile : DO LLAVEIZQ operacion LLAVEDER WHILE PARENIZQ valor PARENDER PUNTOYCOMA
                    | DO LLAVEIZQ print LLAVEDER WHILE PARENIZQ valor PARENDER PUNTOYCOMA
                    | DO LLAVEIZQ impresionEcho LLAVEDER WHILE PARENIZQ valor PARENDER PUNTOYCOMA
                    | DO LLAVEIZQ operacion LLAVEDER WHILE PARENIZQ valor
    '''
#1=>3,
def p_rellenoArray(p):  # clave => valor
    '''rellenoArray : valor OPERASIG_ARRAY valor PUNTOYCOMA
    '''
#Daniel Estructuras---Correegido Cindy

#Cindy
def p_defnombreFuncion(p):
    '''defnombreFuncion : NOMBRE PARENIZQ PARENDER
    '''
def p_asignarvalores(p):
    '''asignarvalores : asignarvalores COMA valor
                       | valor
    '''
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    else:
        p[0] = [p[1]]

#Estructuras -----Cindy
#???????????????????????? - EJEMPLOS
#$lista = list($cadena,$frase1,$frase2);
def p_lista(p):
    '''lista : PARENDER asignarvalores PARENIZQ
             | PARENDER
             | PARENIZQ
    '''

#$var = new hola();

#Daniel

#FUE PRESENTADO PERO FALTA VERIFICAR PARA CORREGIR

#def p_crearHeap(p):
 #   '''crearHeap : varphp ESPACIOENBLANCO IGUAL ESPACIOENBLANCO NEW ESPACIOENBLANCO defnombreFuncion PUNTOYCOMA
  #                  | defnombreFuncion'''

# def p_crearArreglos(p):
#     '''crearArreglos : variable IGUAL array PARENIZQ rellenoArray PARENDER PUNTOYCOMA'''




# def p_metodosArray(p):
#     '''metodosArray : rsort PARENIZQ variable PARENDER PUNTOYCOMA
#                     | rsort PARENIZQ crearArreglos PARENDER PUNTOYCOMA
#                     | count PARENIZQ variable PARENDER PUNTOYCOMA
#                     | count PARENIZQ crearArreglos PARENDER PUNTOYCOMA'''

#Gabriela  -Corregido Cindy



# def p_crearMapa(p):
#     '''crearMapa : OPERAMAPA PARENIZQ valor COMA variable COMA variable PARENDER PUNTOYCOMA
#                    | OPERAMAPA PARENIZQ valor COMA valor COMA variable PARENDER PUNTOYCOMA
#                    | OPERAMAPA PARENIZQ valor COMA variable COMA valor PARENDER PUNTOYCOMA
#     '''


# def p_sumaMapa(p):
#     '''sumaMapa : valor PARENIZQ variable OPERALOGICO_MAP OPERACIONSUM PARENDER PUNTOYCOMA'''


# def p_mapPut(p):
#     '''mapPut : valor OPERALOGICO_MAP OPERAPUT PARENIZQ variable COMA variable PARENDER PUNTOYCOMA '''

#Daniel

resultado_gramatica = []


def p_error(p):
    print("Syntax error")
    resultado_gramatica.append('Syntax error')


parser = yacc.yacc()


def prueba_s(data):
    global resultado_gramatica
    resultado_gramatica.clear()

    for item in data.splitlines():
        if item:
            gram = parser.parse(item)
            resultado_gramatica.append(str(gram))

    print("result: ", resultado_gramatica)
    return resultado_gramatica


if __name__ == '__main__':
    while True:
        try:
            s = input(' ingresa dato >>> ')
        except EOFError:
            continue
        if not s: continue

        # gram = parser.parse(s)
        # print("Resultado ", gram)

        prueba_s(s)
