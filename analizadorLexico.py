from turtle import update
import ply.lex as lex
import re
import codecs
import os
import sys
# Cindy
# .
# .
tokens = [
    'DOLAR',
    'PUNTOYCOMA',
    'PUNTO',
    'COMA',
    'DOSPUNTOS',
    'PARENIZQ',
    'PARENDER',
    'LLAVEIZQ',
    'LLAVEDER',
    'CORCHIZQ',
    'CORCHDER',
    'AMPERSAND',
    'OPERASIGNACION',
    'SUMA',
    'RESTA',
    'MULTIPLICACION',
    'DIVISION',
    'MODULO',
    'EXPONENCIACION',
    'OPERCOMPARACION',
    'OPERLOGICO_OR',
    'OPERLOGICO_AND',
    'OPERLOGICO_XOR',
    'OPERLOGICO_OREXCLUSIVO',
    'OPERLOGICO_NOT',
    'OPERASIG_ARRAY',
    'BOOLEANO',
    'MAYORQUE',
    'MENORQUE',
    #
    'INICIO',
    'FIN',
    'OPERLOG_AND',
    #ESENCIALES
    'CADENA',
    'ENTERO',
    'FLOTANTE',
    'COMENTARIO_UNA_LINEA',
    'COMENTARIO_ABIERTO',
    'COMENTARIO_CERRADO',
    'IDENTIFICADOR'

]

reservadas = {
    #PARA ESTRUCTURAS DE CONTROL
'IF':'if',
'ELSE':'else',
'DO':'do',
'WHILE':'while',
'END_WHILE':'end_while',
'FOR':'for',
'SWITCH':'switch',
'CASE':'case',
'END_SWITCH':'end_switch',
'BREAK':'break',
'CONTINUE':'continue',
'DEFAULT':'default',
'AS':'as',
'RSORT':'rsort',
'COUNT':'count',
'ARRAY':'array',
    #PARA PALABRAS RESERVADAS
'ECHO':'echo',
'GLOBAL':'global',
'STATIC':'static',
'CONST':'const',
'PRINT':'print',
'FUNCTION':'function',
'RETURN':'return',
'CLASS':'class',
'PUBLIC':'public',
'PROTECTED':'protected',
'PRIVATE':'private',
'NEW':'new',
'EXTENDS':'extends'

}

tokens = tokens+list(reservadas.values())

t_DOLAR = r'\$'
t_PUNTOYCOMA = r';'
t_PUNTO = r'\.'
t_COMA = r','
t_DOSPUNTOS = r':'
t_PARENIZQ = r'\('
t_PARENDER = r'\)'
t_LLAVEIZQ = r'\{'
t_LLAVEDER = r'\}'
t_CORCHIZQ = r'\['
t_CORCHDER = r'\]'
t_AMPERSAND = r'&'
t_OPERASIGNACION = r'='
t_SUMA = r'\+'
t_RESTA = r'\-'
t_MULTIPLICACION = r'\*'
t_DIVISION = r'/'
t_MODULO = r'%'
t_EXPONENCIACION = r'\*\*'
t_OPERCOMPARACION = r'=='
t_OPERLOGICO_OR = r'or'
t_OPERLOGICO_XOR =r'xor'
t_OPERLOGICO_OREXCLUSIVO =r'\|\|' #||
t_OPERLOGICO_NOT = r'!'
t_OPERASIG_ARRAY = r'=>'

def t_INICIO(t):
    r'(<\?php){1}'
    return t

def t_FIN(t):
    r'(\?>){1}'
    return t

#.
#.
#Cindy

#Gabriela
t_OPERLOGICO_AND = r'AND'
t_MAYORQUE=r'>'
t_MENORQUE = r'<'

def t_BOOLEANO(t):
    r'(True|False)'
    return t

def t_CADENA(t):
    r'".+"'
    t.type = reservadas.get(t.value, "CADENA")
    return t

t_COMENTARIO_UNA_LINEA =r'//'
t_COMENTARIO_ABIERTO = r'/\*'
t_COMENTARIO_CERRADO = r'\*/'

def t_FLOTANTE(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

#--------------

#.
#.
#Daniel

def t_OPERLOG_AND(t):
    r'(["AND" | \&\&])'

def t_IDENTIFICADOR(t):
    r'([a-zA-Z_][a-zA-Z0-9_]*)'
    t.type = reservadas.get(t.value, "IDENTIFICADOR")
    return t

def t_ENTERO(t):
    r'\d+'
    t.value = int(t.value)
    return t
#.
#.
#Daniel

#Gabriela 
def t_contadorLineas(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print(f"Caracter no reconocido {t.value[0]} en línea {t.lineno}")
    t.lexer.skip(1)

lexer = lex.lex()

def getTokens(lexer):
    while True:
        tok = lexer.token()
        if not tok:
            break 
        print(tok)

linea=" "
codigo = open("source.vb")
for linea in codigo:
  lexer.input(linea)
  getTokens(lexer)
codigo.close()

print("Análisis Léxico terminado... :)")

#-------------