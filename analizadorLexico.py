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
    'LLAVEEDER',
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
    'COMBINADO_OPERARIT_SUMA',
    'COMBINADO_OPERARIT_RESTA',
    'COMBINADO_OPERARIT_MULTIPLICACION',
    'COMBINADO_OPERARIT_DIVISION',
    'COMBINADO_OPERARIT_MODULO',
    'COMBINADO_OPERARIT_EXPONENCIACION',
    'OPERCOMBINADO_CAD',
    'OPERCOMPARACION',
    'OPER_INCREMENTO',
    'OPER_DECREMENTO',
    'OPERLOGICO_OR',
    'OPERLOGICO_XOR',
    'OPERLOGICO_OREXCLUSIVO',
    'OPERLOGICO_NOT',
    'OPERASIG_ARRAY',
    #
    'INICIO',
    'FIN',
    'OPERLOG_AND',
    #ESENCIALES
    'CADENA',
    'ENTERO',
    'REAL',
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

t_DOLAR = r'$'
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
t_EXPONENCIACION = r'**'
t_COMBINADO_OPERARIT_SUMA = r'+='
t_COMBINADO_OPERARIT_RESTA = r'-='
t_COMBINADO_OPERARIT_MULTIPLICACION = r'*='
t_COMBINADO_OPERARIT_DIVISION = r'/='
t_COMBINADO_OPERARIT_MODULO = r'%='
t_COMBINADO_OPERARIT_EXPONENCIACION = r'**='
t_OPERCOMBINADO_CAD = r'\.='
t_OPERCOMPARACION = r'=='
t_OPER_INCREMENTO = r'++'
t_OPER_DECREMENTO = r'--'
t_OPERLOGICO_OR = r'or'
t_OPERLOGICO_XOR =r'xor'
t_OPERLOGICO_OREXCLUSIVO =r'\|\|' #||
t_OPERLOGICO_NOT = r'!'
t_OPERASIG_ARRAY = r'=>'
#.
#.
#Cindy