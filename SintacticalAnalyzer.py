from ply import yacc
from LexycalAnalyzer import lexycalAnalyzer, tokens, reserved
from callbacks import *
from translator import translate

is_first_pin = False
is_first_reserved = False
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
  '''SETUP : DEF_PIN PICO_OPEN TP_OUT DPUNTOS TD_ENTERO PICO_CLOSE
    | DEF_PIN PICO_OPEN TP_OUT DPUNTOS NOMBRE_VAR PICO_CLOSE
    | DEF_PIN PICO_OPEN TP_INP DPUNTOS TD_ENTERO PICO_CLOSE
    | DEF_PIN PICO_OPEN TP_INP DPUNTOS NOMBRE_VAR PICO_CLOSE'''
  is_first_pin = True if p_SETUP.counter <= 0 else False
  p_SETUP.counter += 1
  translate(p, cb_p_pin, is_first_pin=is_first_pin,is_pin=True)
  pass
p_SETUP.counter = 0

#def setup-------------------------------------------------------------
def p_LOOP(p):
  '''LOOP : BWD
    | FWD PICO_OPEN PICO_CLOSE
    | RIGHT PICO_OPEN PICO_CLOSE
    | LEFT PICO_OPEN PICO_CLOSE
    | WAIT PICO_OPEN VALOR_TIEMPO PICO_CLOSE
    | STOP PICO_OPEN PICO_CLOSE'''
  is_first_reserved = True if p_LOOP.counter <= 0 else False
  p_LOOP.counter += 1
  translate(p,cb_p_reservadas, is_first_reserved=is_first_reserved, is_reserved=True)
  pass
p_LOOP.counter = 0

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
  '''VARIABLE : TD_ENTERO DPUNTOS NOMBRE_VAR
    | TD_TEXTO DPUNTOS NOMBRE_VAR
    | TD_DECIMAL DPUNTOS NOMBRE_VAR
    | TD_LOGICO DPUNTOS NOMBRE_VAR'''
  translate(p,cb_p_variable)
  pass
def p_TIPO(p):
  '''TIPO : TD_ENTERO
    | TD_TEXTO
    | TD_DECIMAL
    | TD_LOGICO'''
  pass
def p_ASIGNACIONES(p):
  '''ASIGNACIONES : NOMBRE_VAR ASIGNAR NOMBRE_VAR
    | NOMBRE_VAR ASIGNAR VALOR_ENTERO
    | NOMBRE_VAR ASIGNAR VALOR_TEXTO
    | NOMBRE_VAR ASIGNAR DECIMAL
    | NOMBRE_VAR ASIGNAR LOGICO'''
  translate(p,cb_p_asignacion)
  pass

#Funciones--------------------------------------------------------------
def p_FUNCIONES(p):
  '''FUNCIONES : DEF_FUN NOMBRE_VAR PICO_OPEN ARGUMENTOS PICO_CLOSE DPUNTOS CUERPO RETORNO'''
  translate(p,cb_p_procedimiento)
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
  '''LIBS : ADD_LIB_EXT PICO_OPEN NOMBRE_VAR EXTENSION PICO_CLOSE PUNTO
    | ADD_LIB_EXT PICO_OPEN NOMBRE_VAR EXTENSION COMA NOMBRE_VAR EXTENSION PICO_CLOSE PUNTO''' #dos librerías
  translate(p,cb_p_librerias)
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

