import ply.lex as lex
# Cindy
# .
# .
reservadas = {
    #PARA ESTRUCTURAS DE CONTROL
    'if':'IF',
    'else':'ELSE',
    'do':'DO',
    'while':'WHILE',
    'end_while':'END_WHILE',
    'for':'FOR',
    'switch':'SWITCH',
    'case':'CASE',
    'end_switch':'END_SWITCH',
    'break':'BREAK',
    'continue':'CONTINUE',
    'default':'DEFAULT',
    'as':'AS',
    'rsort':'RSORT',
    'count':'COUNT',
    'array':'ARRAY',
    #PARA PALABRAS RESERVADAS
    'global':'GLOBAL',
    'static':'STATIC',
    'const':'CONST',
    'print':'PRINT',
    'function':'FUNCTION',
    'return':'RETURN',
    'class':'CLASS',
    'new':'NEW',
    'extends':'EXTENDS',
    'int':'INTEGER',
    'string':'STRING',
    'bool':'BOOLEAN',
    'float':'FLOAT',
    'null':'NULL',
    'true':'TRUE',
    'false':'FALSE'    
}

tokens = (
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
    'MAS',
    'MENOS',
    'MULTIPLICA',
    'DIVIDE',
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
    'COMENTARIO_LARGO',
    'VARIABLE',
    'OPERAMAPA',
    'OPERALOGICO_MAP',
    'OPERACIONSUM',
    'OPERAPUT',
    'ECHO',
    #VISIBILIDAD
    'PUBLIC',
    'PROTECTED',
    'PRIVATE'
) + tuple(reservadas.values())

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
t_MAS = r'\+'
t_MENOS = r'\-'
t_MULTIPLICA = r'\*'
t_DIVIDE = r'/'
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
    r'<\?php'
    return t

def t_FIN(t):
    r'\?>'
    return t
def t_ECHO(t):
    r'echo'
    return t

def t_PUBLIC(t):
    r'public'
    return t

def t_PROTECTED(t):
    r'protected'
    return t

def t_PRIVATE(t):
    r'private'
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
    r'\"(.)+\"|\'(.)+\''
    return t

t_COMENTARIO_UNA_LINEA =r'//'+'.*'
t_COMENTARIO_LARGO = r'/\*'+'.*'+'\*/'

def t_FLOTANTE(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_VARIABLE(t):
    r'\$[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reservadas.get(t.value, "VARIABLE")
    return t
#--------------

#.
#.
#Daniel

def t_OPERLOG_AND(t):
    r'(["AND" | \&\&])'

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
    print("Caracter no reconocido {t.value[0]} en línea {t.lineno}")
    t.lexer.skip(1)

validador = lex.lex()

def getTokens(lexer):
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)

# linea=" "
# codigo = open("source.vb")
# for linea in codigo:
#   validador.input(linea)
#   getTokens(validador)
# codigo.close()

# print("Análisis Léxico terminado... :)")

#-------------


