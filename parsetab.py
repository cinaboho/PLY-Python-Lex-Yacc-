
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AMPERSAND ARRAY AS ASTERISCOIGUAL BARRAIGUAL BOOLEAN BOOLEANO BREAK CADENA CASE CLASS COMA COMDOB COMENTARIO_LARGO COMENTARIO_UNA_LINEA COMPARE CONST CONTINUE CORCHDER CORCHIZQ COUNT CURRENT DEFAULT DIVIDE DO DOBLEASTERISCOIGUAL DOSPUNTOS ECHO ELSE EMPTY END_SWITCH END_WHILE ENTERO ESPACIOENBLANCO EXPONENCIACION EXTENDS FALSE FIN FLOAT FLOTANTE FOR FUNCTION GLOBAL IF IGUAL INICIO INTEGER LIST LLAVEDER LLAVEIZQ MAS MASIGUAL MAYORQUE MENORQUE MENOS MENOSIGUAL MODULO MULTIPLICA NEW NOMBRE NULL OPEN_TAG_WITH_ECHO OPERACIONSUM OPERALOGICO_MAP OPERAMAPA OPERAPUT OPERASIG_ARRAY OPERCOMPARACION OPERLOGICO_AND OPERLOGICO_NOT OPERLOGICO_OR OPERLOGICO_OREXCLUSIVO OPERLOGICO_XOR PARENDER PARENIZQ PORCENTAJEIGUAL PRINT PRIVATE PROTECTED PUBLIC PUNTO PUNTOYCOMA RETURN RSORT STATIC STRING SWITCH TEXTOSENCILLO TRUE VARIABLE_PHP WHILEsentencias : valor\n                  | operacion\n                  | asignacion\n                  | asignacion_abreviatura_op\n                  | print\n                  | impresionEcho\n                  | operacion_logica\n                  | condIf\n                  | bucleDoWhile\n                  | rellenoArray\n                  | inicio\n                  | fin\n                  | comentario_largo\n                  | lista\n                  | asignarvalores\n    inicio : INICIO\n    fin : FIN\n    comentario_largo : COMENTARIO_LARGO\n    valor : valorNumerico\n             | CADENAvarphp : VARIABLE_PHPvalorNumerico : ENTERO\n                     | FLOTANTE\n                     | varphp\n                     | BOOLEANO\n    operacion : valorNumerico PUNTOYCOMA\n                 | valorNumerico operador operacion\n                 | valorNumerico comparacion operacion\n    operacion_logica : varphp opLogicos varphp\n    operador : MAS\n                | MENOS\n                | MULTIPLICA\n                | DIVIDE\n                | MODULO\n                | EXPONENCIACION\n    comparacion : MAYORQUE\n                   | MENORQUE\n                   | MENORQUE IGUAL\n                   | MAYORQUE IGUAL\n                   | MENORQUE IGUAL MAYORQUE\n                   | MENORQUE MAYORQUE\n       opLogicos : OPERLOGICO_AND\n                    | OPERLOGICO_OR\n                    | OPERLOGICO_XOR\n                    | OPERLOGICO_NOT\n                    | OPERLOGICO_OREXCLUSIVO\n    asignacion : VARIABLE_PHP IGUAL valor PUNTOYCOMA\n    asignacion_abreviado : MASIGUAL\n                            | MENOSIGUAL\n                            | ASTERISCOIGUAL\n                            | BARRAIGUAL\n                            | PORCENTAJEIGUAL\n                            | DOBLEASTERISCOIGUAL\n    asignacion_abreviatura_op : VARIABLE_PHP asignacion_abreviado valorNumerico PUNTOYCOMA\n    print : PRINT PARENIZQ PARENDER PUNTOYCOMA\n                | PRINT PARENIZQ COMDOB COMDOB PARENDER PUNTOYCOMA\n                | PRINT PARENIZQ CADENA PARENDER PUNTOYCOMAimpresionEcho : ECHO CADENA PUNTOYCOMAcondIf : IF PARENIZQ BOOLEAN PARENDER PUNTOYCOMA\n                | IF PARENIZQ BOOLEAN PARENDER LLAVEIZQ operacion LLAVEDER\n                | IF PARENIZQ BOOLEAN PARENDER LLAVEIZQ print LLAVEDER\n                | IF PARENIZQ BOOLEAN PARENDER LLAVEIZQ impresionEcho LLAVEDER\n    bucleDoWhile : DO LLAVEIZQ operacion LLAVEDER WHILE PARENIZQ valor PARENDER PUNTOYCOMA\n                    | DO LLAVEIZQ print LLAVEDER WHILE PARENIZQ valor PARENDER PUNTOYCOMA\n                    | DO LLAVEIZQ impresionEcho LLAVEDER WHILE PARENIZQ valor PARENDER PUNTOYCOMA\n                    | DO LLAVEIZQ operacion LLAVEDER WHILE PARENIZQ valor\n    rellenoArray : valor OPERASIG_ARRAY valor PUNTOYCOMA\n    defnombreFuncion : NOMBRE PARENIZQ PARENDER\n    asignarvalores : asignarvalores COMA valor\n                       | valor\n    lista : PARENDER asignarvalores PARENIZQ\n             | PARENDER\n             | PARENIZQ\n    '
    
_lr_action_items = {'CADENA':([0,22,23,33,34,46,54,111,112,113,],[18,18,60,18,18,18,81,18,18,18,]),'VARIABLE_PHP':([0,22,33,34,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,61,62,63,64,65,66,68,74,75,76,90,103,111,112,113,],[19,59,59,59,59,59,-30,-31,-32,-33,-34,-35,-36,-37,59,59,-48,-49,-50,-51,-52,-53,59,-42,-43,-44,-45,-46,59,-39,-38,-41,-40,59,59,59,59,]),'PRINT':([0,68,103,],[20,20,20,]),'ECHO':([0,68,103,],[23,23,23,]),'IF':([0,],[25,]),'DO':([0,],[26,]),'INICIO':([0,],[27,]),'FIN':([0,],[28,]),'COMENTARIO_LARGO':([0,],[29,]),'PARENDER':([0,18,30,31,32,54,57,58,59,81,85,94,117,118,119,],[22,-20,-22,-23,-25,79,-19,-24,-21,95,96,100,120,121,122,]),'PARENIZQ':([0,18,20,25,30,31,32,55,56,57,58,59,70,104,105,106,],[21,-20,54,67,-22,-23,-25,82,-70,-19,-24,-21,-69,111,112,113,]),'ENTERO':([0,22,33,34,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,68,74,75,76,90,103,111,112,113,],[30,30,30,30,30,30,-30,-31,-32,-33,-34,-35,-36,-37,30,30,-48,-49,-50,-51,-52,-53,30,-39,-38,-41,-40,30,30,30,30,]),'FLOTANTE':([0,22,33,34,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,68,74,75,76,90,103,111,112,113,],[31,31,31,31,31,31,-30,-31,-32,-33,-34,-35,-36,-37,31,31,-48,-49,-50,-51,-52,-53,31,-39,-38,-41,-40,31,31,31,31,]),'BOOLEANO':([0,22,33,34,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,68,74,75,76,90,103,111,112,113,],[32,32,32,32,32,32,-30,-31,-32,-33,-34,-35,-36,-37,32,32,-48,-49,-50,-51,-52,-53,32,-39,-38,-41,-40,32,32,32,32,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,21,22,24,27,28,29,30,31,32,35,57,58,59,70,72,73,82,83,84,89,91,92,93,101,102,107,114,115,116,117,123,124,125,],[0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-19,-20,-21,-73,-72,-24,-16,-17,-18,-22,-23,-25,-26,-19,-24,-21,-69,-27,-28,-71,-58,-29,-67,-47,-54,-55,-57,-59,-56,-60,-61,-62,-66,-63,-64,-65,]),'OPERASIG_ARRAY':([2,17,18,19,24,30,31,32,],[33,-19,-20,-21,-24,-22,-23,-25,]),'COMA':([2,16,17,18,19,24,30,31,32,55,56,57,58,59,70,],[-70,34,-19,-20,-21,-24,-22,-23,-25,34,-70,-19,-24,-21,-69,]),'PUNTOYCOMA':([17,18,19,24,30,31,32,57,58,59,60,69,71,77,78,79,95,96,100,120,121,122,],[35,-20,-21,-24,-22,-23,-25,-19,-24,-21,83,89,35,91,92,93,101,102,107,123,124,125,]),'MAS':([17,19,24,30,31,32,58,59,71,],[38,-21,-24,-22,-23,-25,-24,-21,38,]),'MENOS':([17,19,24,30,31,32,58,59,71,],[39,-21,-24,-22,-23,-25,-24,-21,39,]),'MULTIPLICA':([17,19,24,30,31,32,58,59,71,],[40,-21,-24,-22,-23,-25,-24,-21,40,]),'DIVIDE':([17,19,24,30,31,32,58,59,71,],[41,-21,-24,-22,-23,-25,-24,-21,41,]),'MODULO':([17,19,24,30,31,32,58,59,71,],[42,-21,-24,-22,-23,-25,-24,-21,42,]),'EXPONENCIACION':([17,19,24,30,31,32,58,59,71,],[43,-21,-24,-22,-23,-25,-24,-21,43,]),'MAYORQUE':([17,19,24,30,31,32,45,58,59,71,75,],[44,-21,-24,-22,-23,-25,76,-24,-21,44,90,]),'MENORQUE':([17,19,24,30,31,32,58,59,71,],[45,-21,-24,-22,-23,-25,-24,-21,45,]),'IGUAL':([19,44,45,],[46,74,75,]),'OPERLOGICO_AND':([19,24,],[-21,62,]),'OPERLOGICO_OR':([19,24,],[-21,63,]),'OPERLOGICO_XOR':([19,24,],[-21,64,]),'OPERLOGICO_NOT':([19,24,],[-21,65,]),'OPERLOGICO_OREXCLUSIVO':([19,24,],[-21,66,]),'MASIGUAL':([19,],[48,]),'MENOSIGUAL':([19,],[49,]),'ASTERISCOIGUAL':([19,],[50,]),'BARRAIGUAL':([19,],[51,]),'PORCENTAJEIGUAL':([19,],[52,]),'DOBLEASTERISCOIGUAL':([19,],[53,]),'LLAVEIZQ':([26,96,],[68,103,]),'LLAVEDER':([35,72,73,83,86,87,88,93,101,107,108,109,110,],[-26,-27,-28,-58,97,98,99,-55,-57,-56,114,115,116,]),'COMDOB':([54,80,],[80,94,]),'BOOLEAN':([67,],[85,]),'WHILE':([97,98,99,],[104,105,106,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'sentencias':([0,],[1,]),'valor':([0,22,33,34,46,111,112,113,],[2,56,69,70,77,117,118,119,]),'operacion':([0,36,37,68,103,],[3,72,73,86,108,]),'asignacion':([0,],[4,]),'asignacion_abreviatura_op':([0,],[5,]),'print':([0,68,103,],[6,87,109,]),'impresionEcho':([0,68,103,],[7,88,110,]),'operacion_logica':([0,],[8,]),'condIf':([0,],[9,]),'bucleDoWhile':([0,],[10,]),'rellenoArray':([0,],[11,]),'inicio':([0,],[12,]),'fin':([0,],[13,]),'comentario_largo':([0,],[14,]),'lista':([0,],[15,]),'asignarvalores':([0,22,],[16,55,]),'valorNumerico':([0,22,33,34,36,37,46,47,68,103,111,112,113,],[17,57,57,57,71,71,57,78,71,71,57,57,57,]),'varphp':([0,22,33,34,36,37,46,47,61,68,103,111,112,113,],[24,58,58,58,58,58,58,58,84,58,58,58,58,58,]),'operador':([17,71,],[36,36,]),'comparacion':([17,71,],[37,37,]),'asignacion_abreviado':([19,],[47,]),'opLogicos':([24,],[61,]),}

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
  ('sentencias -> asignacion_abreviatura_op','sentencias',1,'p_sentencias','analizadorSintactico.py',8),
  ('sentencias -> print','sentencias',1,'p_sentencias','analizadorSintactico.py',9),
  ('sentencias -> impresionEcho','sentencias',1,'p_sentencias','analizadorSintactico.py',10),
  ('sentencias -> operacion_logica','sentencias',1,'p_sentencias','analizadorSintactico.py',11),
  ('sentencias -> condIf','sentencias',1,'p_sentencias','analizadorSintactico.py',12),
  ('sentencias -> bucleDoWhile','sentencias',1,'p_sentencias','analizadorSintactico.py',13),
  ('sentencias -> rellenoArray','sentencias',1,'p_sentencias','analizadorSintactico.py',14),
  ('sentencias -> inicio','sentencias',1,'p_sentencias','analizadorSintactico.py',15),
  ('sentencias -> fin','sentencias',1,'p_sentencias','analizadorSintactico.py',16),
  ('sentencias -> comentario_largo','sentencias',1,'p_sentencias','analizadorSintactico.py',17),
  ('sentencias -> lista','sentencias',1,'p_sentencias','analizadorSintactico.py',18),
  ('sentencias -> asignarvalores','sentencias',1,'p_sentencias','analizadorSintactico.py',19),
  ('inicio -> INICIO','inicio',1,'p_inicio','analizadorSintactico.py',23),
  ('fin -> FIN','fin',1,'p_fin','analizadorSintactico.py',26),
  ('comentario_largo -> COMENTARIO_LARGO','comentario_largo',1,'p_comentario_largo','analizadorSintactico.py',29),
  ('valor -> valorNumerico','valor',1,'p_valor','analizadorSintactico.py',33),
  ('valor -> CADENA','valor',1,'p_valor','analizadorSintactico.py',34),
  ('varphp -> VARIABLE_PHP','varphp',1,'p_varphp','analizadorSintactico.py',37),
  ('valorNumerico -> ENTERO','valorNumerico',1,'p_valorNumerico','analizadorSintactico.py',40),
  ('valorNumerico -> FLOTANTE','valorNumerico',1,'p_valorNumerico','analizadorSintactico.py',41),
  ('valorNumerico -> varphp','valorNumerico',1,'p_valorNumerico','analizadorSintactico.py',42),
  ('valorNumerico -> BOOLEANO','valorNumerico',1,'p_valorNumerico','analizadorSintactico.py',43),
  ('operacion -> valorNumerico PUNTOYCOMA','operacion',2,'p_operacion','analizadorSintactico.py',46),
  ('operacion -> valorNumerico operador operacion','operacion',3,'p_operacion','analizadorSintactico.py',47),
  ('operacion -> valorNumerico comparacion operacion','operacion',3,'p_operacion','analizadorSintactico.py',48),
  ('operacion_logica -> varphp opLogicos varphp','operacion_logica',3,'p_operacion_logica','analizadorSintactico.py',51),
  ('operador -> MAS','operador',1,'p_operador','analizadorSintactico.py',54),
  ('operador -> MENOS','operador',1,'p_operador','analizadorSintactico.py',55),
  ('operador -> MULTIPLICA','operador',1,'p_operador','analizadorSintactico.py',56),
  ('operador -> DIVIDE','operador',1,'p_operador','analizadorSintactico.py',57),
  ('operador -> MODULO','operador',1,'p_operador','analizadorSintactico.py',58),
  ('operador -> EXPONENCIACION','operador',1,'p_operador','analizadorSintactico.py',59),
  ('comparacion -> MAYORQUE','comparacion',1,'p_comparacion','analizadorSintactico.py',62),
  ('comparacion -> MENORQUE','comparacion',1,'p_comparacion','analizadorSintactico.py',63),
  ('comparacion -> MENORQUE IGUAL','comparacion',2,'p_comparacion','analizadorSintactico.py',64),
  ('comparacion -> MAYORQUE IGUAL','comparacion',2,'p_comparacion','analizadorSintactico.py',65),
  ('comparacion -> MENORQUE IGUAL MAYORQUE','comparacion',3,'p_comparacion','analizadorSintactico.py',66),
  ('comparacion -> MENORQUE MAYORQUE','comparacion',2,'p_comparacion','analizadorSintactico.py',67),
  ('opLogicos -> OPERLOGICO_AND','opLogicos',1,'p_opLogicos','analizadorSintactico.py',70),
  ('opLogicos -> OPERLOGICO_OR','opLogicos',1,'p_opLogicos','analizadorSintactico.py',71),
  ('opLogicos -> OPERLOGICO_XOR','opLogicos',1,'p_opLogicos','analizadorSintactico.py',72),
  ('opLogicos -> OPERLOGICO_NOT','opLogicos',1,'p_opLogicos','analizadorSintactico.py',73),
  ('opLogicos -> OPERLOGICO_OREXCLUSIVO','opLogicos',1,'p_opLogicos','analizadorSintactico.py',74),
  ('asignacion -> VARIABLE_PHP IGUAL valor PUNTOYCOMA','asignacion',4,'p_asignacion','analizadorSintactico.py',79),
  ('asignacion_abreviado -> MASIGUAL','asignacion_abreviado',1,'p_asignacion_abreviado','analizadorSintactico.py',82),
  ('asignacion_abreviado -> MENOSIGUAL','asignacion_abreviado',1,'p_asignacion_abreviado','analizadorSintactico.py',83),
  ('asignacion_abreviado -> ASTERISCOIGUAL','asignacion_abreviado',1,'p_asignacion_abreviado','analizadorSintactico.py',84),
  ('asignacion_abreviado -> BARRAIGUAL','asignacion_abreviado',1,'p_asignacion_abreviado','analizadorSintactico.py',85),
  ('asignacion_abreviado -> PORCENTAJEIGUAL','asignacion_abreviado',1,'p_asignacion_abreviado','analizadorSintactico.py',86),
  ('asignacion_abreviado -> DOBLEASTERISCOIGUAL','asignacion_abreviado',1,'p_asignacion_abreviado','analizadorSintactico.py',87),
  ('asignacion_abreviatura_op -> VARIABLE_PHP asignacion_abreviado valorNumerico PUNTOYCOMA','asignacion_abreviatura_op',4,'p_asignacion_abreviatura_op','analizadorSintactico.py',90),
  ('print -> PRINT PARENIZQ PARENDER PUNTOYCOMA','print',4,'p_print','analizadorSintactico.py',98),
  ('print -> PRINT PARENIZQ COMDOB COMDOB PARENDER PUNTOYCOMA','print',6,'p_print','analizadorSintactico.py',99),
  ('print -> PRINT PARENIZQ CADENA PARENDER PUNTOYCOMA','print',5,'p_print','analizadorSintactico.py',100),
  ('impresionEcho -> ECHO CADENA PUNTOYCOMA','impresionEcho',3,'p_impresionEcho','analizadorSintactico.py',103),
  ('condIf -> IF PARENIZQ BOOLEAN PARENDER PUNTOYCOMA','condIf',5,'p_condIf','analizadorSintactico.py',106),
  ('condIf -> IF PARENIZQ BOOLEAN PARENDER LLAVEIZQ operacion LLAVEDER','condIf',7,'p_condIf','analizadorSintactico.py',107),
  ('condIf -> IF PARENIZQ BOOLEAN PARENDER LLAVEIZQ print LLAVEDER','condIf',7,'p_condIf','analizadorSintactico.py',108),
  ('condIf -> IF PARENIZQ BOOLEAN PARENDER LLAVEIZQ impresionEcho LLAVEDER','condIf',7,'p_condIf','analizadorSintactico.py',109),
  ('bucleDoWhile -> DO LLAVEIZQ operacion LLAVEDER WHILE PARENIZQ valor PARENDER PUNTOYCOMA','bucleDoWhile',9,'p_bucleDoWhile','analizadorSintactico.py',114),
  ('bucleDoWhile -> DO LLAVEIZQ print LLAVEDER WHILE PARENIZQ valor PARENDER PUNTOYCOMA','bucleDoWhile',9,'p_bucleDoWhile','analizadorSintactico.py',115),
  ('bucleDoWhile -> DO LLAVEIZQ impresionEcho LLAVEDER WHILE PARENIZQ valor PARENDER PUNTOYCOMA','bucleDoWhile',9,'p_bucleDoWhile','analizadorSintactico.py',116),
  ('bucleDoWhile -> DO LLAVEIZQ operacion LLAVEDER WHILE PARENIZQ valor','bucleDoWhile',7,'p_bucleDoWhile','analizadorSintactico.py',117),
  ('rellenoArray -> valor OPERASIG_ARRAY valor PUNTOYCOMA','rellenoArray',4,'p_rellenoArray','analizadorSintactico.py',121),
  ('defnombreFuncion -> NOMBRE PARENIZQ PARENDER','defnombreFuncion',3,'p_defnombreFuncion','analizadorSintactico.py',127),
  ('asignarvalores -> asignarvalores COMA valor','asignarvalores',3,'p_asignarvalores','analizadorSintactico.py',130),
  ('asignarvalores -> valor','asignarvalores',1,'p_asignarvalores','analizadorSintactico.py',131),
  ('lista -> PARENDER asignarvalores PARENIZQ','lista',3,'p_lista','analizadorSintactico.py',142),
  ('lista -> PARENDER','lista',1,'p_lista','analizadorSintactico.py',143),
  ('lista -> PARENIZQ','lista',1,'p_lista','analizadorSintactico.py',144),
]
