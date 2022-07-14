
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AMPERSAND ARRAY AS BOOLEAN BOOLEANO BREAK CADENA CASE CLASS COMA COMENTARIO_LARGO COMENTARIO_UNA_LINEA CONST CONTINUE CORCHDER CORCHIZQ COUNT DEFAULT DIVISION DO DOSPUNTOS ECHO ELSE END_SWITCH END_WHILE ENTERO EXPONENCIACION EXTENDS FALSE FIN FLOAT FLOTANTE FOR FUNCTION GLOBAL IF INICIO INTEGER LLAVEDER LLAVEIZQ MAYORQUE MENORQUE MODULO MULTIPLICACION NEW NULL OPERACIONSUM OPERALOGICO_MAP OPERAMAPA OPERAPUT OPERASIGNACION OPERASIG_ARRAY OPERCOMPARACION OPERLOGICO_AND OPERLOGICO_NOT OPERLOGICO_OR OPERLOGICO_OREXCLUSIVO OPERLOGICO_XOR OPERLOG_AND PARENDER PARENIZQ PRINT PRIVATE PROTECTED PUBLIC PUNTO PUNTOYCOMA RESTA RETURN RSORT STATIC STRING SUMA SWITCH TRUE VARIABLE WHILEsentencias : valor\n    valor : ENTERO\n             | FLOTANTE\n             | VARIABLE\n             | CADENA\n             | BOOLEANO\n    '
    
_lr_action_items = {'ENTERO':([0,],[3,]),'FLOTANTE':([0,],[4,]),'VARIABLE':([0,],[5,]),'CADENA':([0,],[6,]),'BOOLEANO':([0,],[7,]),'$end':([1,2,3,4,5,6,7,],[0,-1,-2,-3,-4,-5,-6,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'sentencias':([0,],[1,]),'valor':([0,],[2,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> sentencias","S'",1,None,None,None),
  ('sentencias -> valor','sentencias',1,'p_sentencias','analizadorSintactico.py',5),
  ('valor -> ENTERO','valor',1,'p_valor','analizadorSintactico.py',8),
  ('valor -> FLOTANTE','valor',1,'p_valor','analizadorSintactico.py',9),
  ('valor -> VARIABLE','valor',1,'p_valor','analizadorSintactico.py',10),
  ('valor -> CADENA','valor',1,'p_valor','analizadorSintactico.py',11),
  ('valor -> BOOLEANO','valor',1,'p_valor','analizadorSintactico.py',12),
]
