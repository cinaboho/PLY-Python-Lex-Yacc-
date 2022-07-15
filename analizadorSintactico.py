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
                  | heapCreate
                  | heapCompare
                  | heapInsert
                  | heapCurrent

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
#print();
#print("");
#print $a;
#print("Hola mundo 1");

def p_print(p):
    '''print : PRINT PARENIZQ PARENDER PUNTOYCOMA
             | PRINT PARENIZQ COMDOB  COMDOB PARENDER PUNTOYCOMA
             | PRINT ESPACIOENBLANCO varphp PUNTOYCOMA
             | PRINT PARENIZQ CADENA PARENDER PUNTOYCOMA
             | PRINT PARENIZQ COMDOB TEXTOSENCILLO varphp
             | PRINT COMDOB TEXTOSENCILLO varphp COMDOB
    '''
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
    '''bucleDoWhile : DO LLAVEIZQ operacion LLAVEDER WHILE PARENIZQ BOOLEANO PARENDER PUNTOYCOMA
                    | DO LLAVEIZQ print LLAVEDER WHILE PARENIZQ BOOLEANO PARENDER PUNTOYCOMA
                    | DO LLAVEIZQ impresionEcho LLAVEDER WHILE PARENIZQ BOOLEANO PARENDER PUNTOYCOMA
                    | DO LLAVEIZQ operacion LLAVEDER WHILE PARENIZQ BOOLEANO
    '''


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

def p_nombreFuncion(p):
    '''nombreFuncion : VARIABLE PARENIZQ PARENDER
    '''
#$var = new hola();
def p_crearHeap(p):
    '''crearHeap : varphp ESPACIOENBLANCO OPERASIGNACION ESPACIOENBLANCO NEW ESPACIOENBLANCO nombreFuncion PUNTOYCOMA
                 | nombreFuncion
    '''

def p_createFunction(p):
    '''createFunction: FUNCTION VARIABLE PARENIZQ VARIABLE_PHP PARENDER LLAVEIZQ asignacionLogica LLAVEDER 
    '''
def p_asignacionLogica(p):
    '''asignacionLogica: VARIABLE_PHP OPERALOGICO_MAP VARIABLE OPERASIGNACION VARIABLE_PHP PUNTOYCOMA
    '''
    
def p_crearInstancia(p):
    '''crearInstancia: NEW VARIABLE PARENIZQ PARENDER
    '''

def p_heapCompare(p):
    '''heapCompare: 'COMPARE' PARENIZQ VARIABLE_PHP COMA VARIABLE_PHP PARENDER
                   |'compare' PARENIZQ VARIABLE_PHP COMA VARIABLE_PHP PARENDER
    '''

def p_heapCurrent(p):
    '''heapCurrent: 'CURRENT' PARENIZQ PARENDER
                   |'current' PARENIZQ PARENDER
    '''

def p_heapCreate(p):
    '''heapCreate: VARIABLE_PHP OPERASIGNACION crearInstancia
    '''

def p_heapInsert(p):
    '''heapInsert: VARIABLE_PHP OPERALOGICO_MAP INSERT PARENIZQ ARRAY PARENIZQ VARIABLE OPERASIG_ARRAY valor PARENDER PARENDER
    '''



def p_error(p):
    print("Syntax error")

parser = yacc.yacc()
while True:
    try:
        s = input("calc>  ")
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)
    
