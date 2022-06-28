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
    'IDENTIFICADOR',
    'OPERAMAPA',    
    'OPERALOGICO_MAP',
    'OPERACIONSUM',
    'OPERAPUT'

]

reservadas = {
    #PARA ESTRUCTURAS DE CONTROL
'If':'IF',
'Else':'ELSE',
'Do':'DO',
'While':'WHILE',
'End_while':'END_WHILE',
'For':'FOR',
'Switch':'SWITCH',
'Case':'CASE',
'End_switch':'END_SWITCH',
'Break':'BREAK',
'Continue':'CONTINUE',
'Default':'DEFAULT',
'As':'AS',
'Rsort':'RSORT',
'Count':'COUNT',
'Array':'ARRAY',
    #PARA PALABRAS RESERVADAS
'Echo':'ECHO',
'Global':'GLOBAL',
'Static':'STATIC',
'Const':'CONST',
'Print':'PRINT',
'Function':'FUNCTION',
'Return':'RETURN',
'Class':'CLASS',
'Public':'PUBLIC',
'Protected':'PROTECTED',
'Private':'PRIVATE',
'New':'NEW',
'Extends':'EXTENDS'

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
t_OPERAMAPA = r'array\_map'
t_OPERALOGICO_MAP = r'\->'
t_OPERACIONSUM = r'sum\(\)'
t_OPERAPUT = r'put'

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
