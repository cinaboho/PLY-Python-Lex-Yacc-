#Grupo 5

#Gabriela 
import ply.yacc as yacc

from analizadorLexico import tokens

def p_codigoFuente(p):
    '''codigoFuente : valor'''

def p_valor(p):
    '''valor : CADENA
            | ENTERO
            | FLOTANTE
            | BOOLEANO'''


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

#---------------