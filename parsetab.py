
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AMPERSAND ARRAY AS BOOLEAN BOOLEANO BREAK CADENA CASE CLASS COMA COMENTARIO_LARGO COMENTARIO_UNA_LINEA CONST CONTINUE CORCHDER CORCHIZQ COUNT DEFAULT DIVIDE DO DOSPUNTOS ECHO ELSE END_SWITCH END_WHILE ENTERO EXPONENCIACION EXTENDS FALSE FIN FLOAT FLOTANTE FOR FUNCTION GLOBAL IF INICIO INTEGER LLAVEDER LLAVEIZQ MAS MAYORQUE MENORQUE MENOS MODULO MULTIPLICA NEW NULL OPERACIONSUM OPERALOGICO_MAP OPERAMAPA OPERAPUT OPERASIGNACION OPERASIG_ARRAY OPERCOMPARACION OPERLOGICO_AND OPERLOGICO_NOT OPERLOGICO_OR OPERLOGICO_OREXCLUSIVO OPERLOGICO_XOR OPERLOG_AND PARENDER PARENIZQ PRINT PRIVATE PROTECTED PUBLIC PUNTO PUNTOYCOMA RETURN RSORT STATIC STRING SWITCH TRUE VARIABLE WHILEsentencias : valor\n                  | operacion\n                  | asignacion\n\n    valor : valorNumerico\n             | CADENA\n    valorNumerico : ENTERO\n                     | FLOTANTE\n                     | VARIABLE\n                     | BOOLEANO\n    operacion : valorNumerico\n            | valorNumerico operador operacion\n    operador : MAS\n                | MENOS\n                | MULTIPLICA\n                | DIVIDE\n                | MODULO\n                | EXPONENCIACION\n    asignacion : VARIABLE OPERASIGNACION valor\n    '
    
_lr_action_items = {'CADENA':([0,18,],[6,6,]),'VARIABLE':([0,11,12,13,14,15,16,17,18,],[7,21,-12,-13,-14,-15,-16,-17,21,]),'ENTERO':([0,11,12,13,14,15,16,17,18,],[8,8,-12,-13,-14,-15,-16,-17,8,]),'FLOTANTE':([0,11,12,13,14,15,16,17,18,],[9,9,-12,-13,-14,-15,-16,-17,9,]),'BOOLEANO':([0,11,12,13,14,15,16,17,18,],[10,10,-12,-13,-14,-15,-16,-17,10,]),'$end':([1,2,3,4,5,6,7,8,9,10,19,20,21,22,23,],[0,-1,-2,-3,-4,-5,-8,-6,-7,-9,-10,-11,-8,-18,-4,]),'MAS':([5,7,8,9,10,19,21,],[12,-8,-6,-7,-9,12,-8,]),'MENOS':([5,7,8,9,10,19,21,],[13,-8,-6,-7,-9,13,-8,]),'MULTIPLICA':([5,7,8,9,10,19,21,],[14,-8,-6,-7,-9,14,-8,]),'DIVIDE':([5,7,8,9,10,19,21,],[15,-8,-6,-7,-9,15,-8,]),'MODULO':([5,7,8,9,10,19,21,],[16,-8,-6,-7,-9,16,-8,]),'EXPONENCIACION':([5,7,8,9,10,19,21,],[17,-8,-6,-7,-9,17,-8,]),'OPERASIGNACION':([7,],[18,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'sentencias':([0,],[1,]),'valor':([0,18,],[2,22,]),'operacion':([0,11,],[3,20,]),'asignacion':([0,],[4,]),'valorNumerico':([0,11,18,],[5,19,23,]),'operador':([5,19,],[11,11,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> sentencias","S'",1,None,None,None),
  ('sentencias -> valor','sentencias',1,'p_sentencias','analizadorSintactico.py',5),
  ('sentencias -> operacion','sentencias',1,'p_sentencias','analizadorSintactico.py',6),
  ('sentencias -> asignacion','sentencias',1,'p_sentencias','analizadorSintactico.py',7),
  ('valor -> valorNumerico','valor',1,'p_valor','analizadorSintactico.py',11),
  ('valor -> CADENA','valor',1,'p_valor','analizadorSintactico.py',12),
  ('valorNumerico -> ENTERO','valorNumerico',1,'p_valorNumerico','analizadorSintactico.py',15),
  ('valorNumerico -> FLOTANTE','valorNumerico',1,'p_valorNumerico','analizadorSintactico.py',16),
  ('valorNumerico -> VARIABLE','valorNumerico',1,'p_valorNumerico','analizadorSintactico.py',17),
  ('valorNumerico -> BOOLEANO','valorNumerico',1,'p_valorNumerico','analizadorSintactico.py',18),
  ('operacion -> valorNumerico','operacion',1,'p_operacion','analizadorSintactico.py',21),
  ('operacion -> valorNumerico operador operacion','operacion',3,'p_operacion','analizadorSintactico.py',22),
  ('operador -> MAS','operador',1,'p_operador','analizadorSintactico.py',25),
  ('operador -> MENOS','operador',1,'p_operador','analizadorSintactico.py',26),
  ('operador -> MULTIPLICA','operador',1,'p_operador','analizadorSintactico.py',27),
  ('operador -> DIVIDE','operador',1,'p_operador','analizadorSintactico.py',28),
  ('operador -> MODULO','operador',1,'p_operador','analizadorSintactico.py',29),
  ('operador -> EXPONENCIACION','operador',1,'p_operador','analizadorSintactico.py',30),
  ('asignacion -> VARIABLE OPERASIGNACION valor','asignacion',3,'p_asignacion','analizadorSintactico.py',33),
]
