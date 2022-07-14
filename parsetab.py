
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AMPERSAND ARRAY AS BOOLEAN BOOLEANO BREAK CADENA CASE CLASS COMA COMENTARIO_LARGO COMENTARIO_UNA_LINEA CONST CONTINUE CORCHDER CORCHIZQ COUNT DEFAULT DIVIDE DO DOSPUNTOS ECHO ELSE END_SWITCH END_WHILE ENTERO EXPONENCIACION EXTENDS FALSE FIN FLOAT FLOTANTE FOR FUNCTION GLOBAL IF INICIO INTEGER LLAVEDER LLAVEIZQ MAS MAYORQUE MENORQUE MENOS MODULO MULTIPLICA NEW NULL OPERACIONSUM OPERALOGICO_MAP OPERAMAPA OPERAPUT OPERASIGNACION OPERASIG_ARRAY OPERCOMPARACION OPERLOGICO_AND OPERLOGICO_NOT OPERLOGICO_OR OPERLOGICO_OREXCLUSIVO OPERLOGICO_XOR OPERLOG_AND PARENDER PARENIZQ PRINT PRIVATE PROTECTED PUBLIC PUNTO PUNTOYCOMA RETURN RSORT STATIC STRING SWITCH TRUE VARIABLE WHILEsentencias : valor\n                  | suma\n    valor : valorNumerico\n             | CADENA\n             | BOOLEANO\n    valorNumerico : ENTERO\n                     | FLOTANTE\n                     | VARIABLE\n    suma : valorNumerico\n            | valorNumerico operador suma\n    operador : MAS\n                | MENOS\n                | MULTIPLICA\n                | DIVIDE\n                | MODULO\n                | EXPONENCIACION\n    '
    
_lr_action_items = {'CADENA':([0,],[5,]),'BOOLEANO':([0,],[6,]),'ENTERO':([0,10,11,12,13,14,15,16,],[7,7,-11,-12,-13,-14,-15,-16,]),'FLOTANTE':([0,10,11,12,13,14,15,16,],[8,8,-11,-12,-13,-14,-15,-16,]),'VARIABLE':([0,10,11,12,13,14,15,16,],[9,9,-11,-12,-13,-14,-15,-16,]),'$end':([1,2,3,4,5,6,7,8,9,17,18,],[0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,]),'MAS':([4,7,8,9,17,],[11,-6,-7,-8,11,]),'MENOS':([4,7,8,9,17,],[12,-6,-7,-8,12,]),'MULTIPLICA':([4,7,8,9,17,],[13,-6,-7,-8,13,]),'DIVIDE':([4,7,8,9,17,],[14,-6,-7,-8,14,]),'MODULO':([4,7,8,9,17,],[15,-6,-7,-8,15,]),'EXPONENCIACION':([4,7,8,9,17,],[16,-6,-7,-8,16,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'sentencias':([0,],[1,]),'valor':([0,],[2,]),'suma':([0,10,],[3,18,]),'valorNumerico':([0,10,],[4,17,]),'operador':([4,17,],[10,10,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> sentencias","S'",1,None,None,None),
  ('sentencias -> valor','sentencias',1,'p_sentencias','analizadorSintactico.py',5),
  ('sentencias -> suma','sentencias',1,'p_sentencias','analizadorSintactico.py',6),
  ('valor -> valorNumerico','valor',1,'p_valor','analizadorSintactico.py',9),
  ('valor -> CADENA','valor',1,'p_valor','analizadorSintactico.py',10),
  ('valor -> BOOLEANO','valor',1,'p_valor','analizadorSintactico.py',11),
  ('valorNumerico -> ENTERO','valorNumerico',1,'p_valorNumerico','analizadorSintactico.py',14),
  ('valorNumerico -> FLOTANTE','valorNumerico',1,'p_valorNumerico','analizadorSintactico.py',15),
  ('valorNumerico -> VARIABLE','valorNumerico',1,'p_valorNumerico','analizadorSintactico.py',16),
  ('suma -> valorNumerico','suma',1,'p_suma','analizadorSintactico.py',19),
  ('suma -> valorNumerico operador suma','suma',3,'p_suma','analizadorSintactico.py',20),
  ('operador -> MAS','operador',1,'p_operador','analizadorSintactico.py',23),
  ('operador -> MENOS','operador',1,'p_operador','analizadorSintactico.py',24),
  ('operador -> MULTIPLICA','operador',1,'p_operador','analizadorSintactico.py',25),
  ('operador -> DIVIDE','operador',1,'p_operador','analizadorSintactico.py',26),
  ('operador -> MODULO','operador',1,'p_operador','analizadorSintactico.py',27),
  ('operador -> EXPONENCIACION','operador',1,'p_operador','analizadorSintactico.py',28),
]
