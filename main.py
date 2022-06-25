#Grupo 5 
import ply.yacc as yacc

from analizadorLexico import tokens

#Gabriela
def p_codigoFuente(p):
    '''codigoFuente : valor
                    | variable
                    | impresionEcho
                    | impresionPrint
                    | valores
                    | asignacion
                    | operacionesA
                    | operacionesC
                    | operacionesL
                    | condIf
                    | opCombinadas
                    | bucleDoWhile
                    | crearArreglos
                    | bucleForEach
                    | metodosArray 
                    | rellenoArreglos
                    | opLogicos
                    | operadoresA
                    | operadoresC
                    | sentencias
                    | '''

#metodos array => sort y count

def p_valor(p):
    '''valor : CADENA
            | ENTERO
            | FLOTANTE
            | BOOLEANO'''

def p_variable(p):
    '''variable : DOLAR IDENTIFICADOR'''

def p_valores(p):
    '''valores :  valor
                | variable'''

def p_operacionesV(p):
    '''operacionesV : FLOTANTE
                    | ENTERO
                    | variable'''

def p_opLog(p):
    '''opLog : BOOLEANO
                | variable'''

def p_impresionEcho(p):
    '''impresionEcho : IDENTIFICADOR CADENA PUNTOYCOMA'''

def p_asignacion(p):
    '''asignacion : variable OPERASIGNACION valor PUNTOYCOMA'''

def p_operadoresA(p):
    '''operadoresA : SUMA
                    | RESTA
                    | MULTIPLICACION
                    | DIVISION
                    | MODULO
                    | EXPONENCIACION'''

def p_operacionesA(p):
    '''operacionesA : operacionesV operadoresA operacionesV
                        | operacionesV operadoresA operacionesA'''

def p_operadoresC(p):
    '''operadoresC : OPERCOMPARACION
                    | OPERCOMPARACION OPERASIGNACION
                    | OPERLOGICO_NOT OPERASIGNACION
                    | MENORQUE MAYORQUE
                    | OPERLOGICO_NOT OPERCOMPARACION
                    | MENORQUE
                    | MAYORQUE
                    | MENORQUE OPERASIGNACION
                    | MAYORQUE OPERASIGNACION
                    | MENORQUE OPERASIGNACION MAYORQUE'''

def p_operacionesC(p):
    '''operacionesC : valores operadoresC valores'''

def p_opLogicos(p):
    '''opLogicos : OPERLOGICO_AND
                    | OPERLOGICO_OR
                    | OPERLOGICO_XOR
                    | OPERLOGICO_NOT
                    | AMPERSAND AMPERSAND
                    | OPERLOGICO_OREXCLUSIVO'''

def p_operacionesL(p):
    '''operacionesL : opLog opLogicos opLog'''

def p_sentencias(p):
    '''sentencias : operacionesL PUNTOYCOMA
                    | operacionesA PUNTOYCOMA
                    | operacionesC PUNTOYCOMA
                    | asignacion
                    | sentencias'''

def p_opCombinadas(p):
    '''opCombinadas : variable OPERASIGNACION operacionesA
                    | variable OPERASIGNACION operacionesL
                    | variable OPERASIGNACION operacionesC'''

def p_impresionPrint(p):
    '''impresionPrint : IDENTIFICADOR PARENIZQ valores PARENDER PUNTOYCOMA
                        | IDENTIFICADOR PARENIZQ operacionesL PARENDER PUNTOYCOMA
                        | IDENTIFICADOR PARENIZQ operacionesC PARENDER PUNTOYCOMA
                        | IDENTIFICADOR PARENIZQ operacionesA PARENDER PUNTOYCOMA'''

def p_retornoBool(p):
    '''retornoBool : BOOLEANO
                    | operacionesL
                    | operacionesC'''
def p_condIf(p):
    '''condIf : IDENTIFICADOR PARENIZQ retornoBool PARENDER PUNTOYCOMA
                | IDENTIFICADOR PARENIZQ retornoBool PARENDER LLAVEIZQ sentencias LLAVEDER
                | IDENTIFICADOR PARENIZQ retornoBool PARENDER LLAVEIZQ impresionPrint LLAVEDER
                | IDENTIFICADOR PARENIZQ retornoBool PARENDER LLAVEIZQ impresionEcho LLAVEDER'''

def p_bucleDoWhile(p):
    '''bucleDoWhile : IDENTIFICADOR LLAVEIZQ sentencias LLAVEDER IDENTIFICADOR PARENIZQ retornoBool PARENDER PUNTOYCOMA
                    | IDENTIFICADOR LLAVEIZQ impresionPrint LLAVEDER IDENTIFICADOR PARENIZQ retornoBool PARENDER PUNTOYCOMA
                    | IDENTIFICADOR LLAVEIZQ impresionEcho LLAVEDER IDENTIFICADOR PARENIZQ retornoBool PARENDER PUNTOYCOMA'''

def p_rellenoArray(p):     #clave => valor
    '''rellenoArray : valores OPERASIG_ARRAY valores COMA
                    | valores
                    | COMA valores OPERASIG_ARRAY valores COMA rellenoArray'''

def p_crearArreglos(p):
    '''crearArreglos : variable OPERASIGNACION IDENTIFICADOR PARENIZQ rellenoArray PARENDER PUNTOYCOMA'''

def p_bucleForEach(p):
    '''bucleForEach : variable IDENTIFICADOR variable LLAVEIZQ sentencias LLAVEDER
                    | variable IDENTIFICADOR variable OPERASIG_ARRAY variable LLAVEIZQ sentencias LLAVEDER'''

def p_metodosArray(p):
    '''metodosArray : IDENTIFICADOR PARENIZQ variable PARENDER PUNTOYCOMA
                    | IDENTIFICADOR PARENIZQ crearArreglos PARENDER PUNTOYCOMA'''
 
# -------------------


#Bucle For y Break pendiente!!!!


#Gabriela
def p_error(p):
    if p:
      print("Error de sintaxis en token", p.type)
      sintactico.errok()
        # Just discard the token and tell the parser it's okay.
    else:
        print("Error de sintaxis EOF")

# Construye el parser
sintactico = yacc.yacc()

while True:
    try:
      linea = input('vb.net>> ')
    except EOFError:
        break
    if not linea: continue
    result = sintactico.parse(linea)
    print(result)

'''linea=" "
codigo = open("source.vb")
result = sintactico.parse(codigo.read())
codigo.close()

print("Proyecto casi terminado... :)")'''
#---------------