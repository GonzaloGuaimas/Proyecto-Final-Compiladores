from ply import yacc
from LexycalAnalyzer import lexycalAnalyzer, tokens, reserved

def t_NOMBRE_VAR(t):
  r'[a-zA-Z][a-zA-Z0-9_]+'
  t.type = reserved.get(t.value,'NOMBRE_VAR') # Check for reserved words
  return t

def t_error(t):
  print("Se encontró un error en %s" % repr(t.value[0]))
  t.lexer.skip(1)
  
def t_newline(t):
  r'\n'
  t.lexer.lineno+=1

#-------------------------------------------------------------------------------------------------
def p_S(p):
  '''S : PROG_BEGIN LIBS CUERPO PROG_END'''
  pass
def p_CUERPO(p):
  '''CUERPO : SENTENCIA CUERPO 
    | empty'''
  pass
def p_SENTENTCIA(p):
  '''SENTENCIA : DEF_VBLES PUNTO
    | ASIGNACIONES PUNTO
    | SETUP PUNTO
    | LOOP PUNTO
    | FUNCIONES PUNTO
    | CONDICIONALES
    | CICLO'''
  pass

#def loops-------------------------------------------------------------
def p_SETUP(p):
  '''SETUP : DEF_PIN PICO_OPEN TIPO_PIN DPUNTOS TD_ENTERO PICO_CLOSE
    | DEF_PIN PICO_OPEN TIPO_PIN DPUNTOS NOMBRE_VAR PICO_CLOSE'''
  pass
def p_TIPO_PIN(p):
  '''TIPO_PIN : TP_OUT 
    | TP_INP'''
  pass
#def setup-------------------------------------------------------------
def p_LOOP(p):
  '''LOOP : BWD
    | FWD PICO_OPEN PICO_CLOSE
    | RIGHT PICO_OPEN PICO_CLOSE
    | LEFT PICO_OPEN PICO_CLOSE
    | WAIT PICO_OPEN VALOR_TIEMPO PICO_CLOSE
    | STOP PICO_OPEN PICO_CLOSE'''
  pass
def p_VALOR_TIEMPO(p):
  '''VALOR_TIEMPO : NOMBRE_VAR
    | VALOR_ENTERO
    | DECIMAL'''
  pass
#definición de Variables----------------------------------------------
def p_DEF_VBLES(p):
  '''DEF_VBLES : DEF_VAR PICO_OPEN VARIABLE PICO_CLOSE'''
  pass
def p_VARIABLE(p):
  '''VARIABLE : TIPO DPUNTOS NOMBRE_VAR'''
  pass
def p_TIPO(p):
  '''TIPO : TD_ENTERO
    | TD_TEXTO
    | TD_DECIMAL
    | TD_LOGICO'''
  pass
#asignaciones-----------------------------------------------------------
def p_ASIGNACIONES(p):
  '''ASIGNACIONES : NOMBRE_VAR ASIGNAR ASIGN_LDERECHO'''
  pass
def p_ASIGN_LDERECHO(p):
  '''ASIGN_LDERECHO : NOMBRE_VAR 
    | VALOR_ENTERO
    | VALOR_TEXTO
    | DECIMAL
    | LOGICO'''
  pass
#Funciones--------------------------------------------------------------
def p_FUNCIONES(p):
  '''FUNCIONES : DEF_FUN NOMBRE_VAR PICO_OPEN ARGUMENTOS PICO_CLOSE DPUNTOS CUERPO RETORNO'''
  pass
def p_ARGUMENTOS(p):
  '''ARGUMENTOS : TIPO DPUNTOS NOMBRE_VAR COMA ARGUMENTOS
    | TIPO DPUNTOS NOMBRE_VAR'''
  pass
#Condicionales
def p_CONDICIONALES(p):
  '''CONDICIONALES : IF CONDICION BEGIN CUERPO END ELSE BEGIN CUERPO END
    | IF CONDICION BEGIN CUERPO END'''
  pass
#Ciclos
def p_CICLO(p):
  '''CICLO : WHILE CONDICION BEGIN CUERPO END'''
  pass
def p_CONDICION(p):
  '''CONDICION : PICO_OPEN NOMBRE_VAR OPERADOR NOMBRE_VAR PICO_CLOSE'''
  pass
#Producciones Librerías------------------------------------------------
def p_LIBS(p):
  '''LIBS : ADD_LIB_EXT PICO_OPEN LIBRERIA PICO_CLOSE PUNTO'''
  pass
def p_LIBRERIA(p):
  '''LIBRERIA : NOMBRE_VAR EXTENSION 
    | NOMBRE_VAR EXTENSION COMA LIBRERIA'''
  pass
def p_empty(p):
  '''empty : '''
  pass

def p_error(p):
  print("Error sintáctico en la línea: " + str(p.lineno)
              + ". No se esperaba el token: " + str(p.value))        
  raise Exception('syntax', 'error')

lexycalAnalyzer.lineno = 0
sintacticalAnalyzer = yacc.yacc()