import ply.lex as lex 

#Reserved words
reserved = {
  'PROG_BEGIN' : 'PROG_BEGIN',
  'PROG_END' : 'PROG_END',
  'ADD' : 'ADD_LIB_EXT',
  'entero' : 'TD_ENTERO',
  'texto' : 'TD_TEXTO',
  'decimal' : 'TD_DECIMAL',
  'logico' : 'TD_LOGICO',
  'VAR' : 'DEF_VAR',
  'FUNC' : 'DEF_FUN',
  'retorno' : 'RETORNO',
  'PIN' : 'DEF_PIN',

  'TRUE' : 'BOOL_T',
  'FALSE' : 'BOOL_F',
  'OUT' :  'TP_OUT',
  'INP' : 'TP_INP',

  'IF' : 'IF',
  'ELSE' : 'ELSE',
  'BEGIN' : 'BEGIN',
  'END' : 'END',
  'WHILE' : 'WHILE',

  'FOWARD' : 'FWD',
  'BACKWARD' : 'BWD',
  'LEFT' : 'LEFT',
  'RIGHT' : 'RIGHT',
  'WAIT' : 'WAIT',
  'STOP' : 'STOP',
  }
#Tokens
tokens = ['PUNTO',
          'PICO_OPEN',
          'PICO_CLOSE',
          'PARENT_OPEN',
          'PARENT_CLOSE',
          'COMA',
          'VALOR_ENTERO',
          'VALOR_TEXTO',
          'DECIMAL',
          'LOGICO',
          'DPUNTOS',
          'ASIGNAR',
          'OPERADOR',
          'NOMBRE_VAR',
          'EXTENSION'] + list(reserved.values())

#Reg Expr.
t_PUNTO = r'\.'
t_PICO_OPEN = r'<'
t_PICO_CLOSE = r'>'
t_PARENT_OPEN = r'\('
t_PARENT_CLOSE = r'\)'
t_COMA = r'\,'
t_VALOR_ENTERO = r'[0-9]+'
t_EXTENSION = r'\.[a-z][a-z][a-z]'
t_VALOR_TEXTO = r'\".*\"'
t_DECIMAL = r'[0-9]+\.[0-9]+'
t_ASIGNAR = r'(:=)'
t_DPUNTOS = r'\:'
t_OPERADOR = r'(\+ | - | >= | <= | == | !=)'
#Ignores
t_ignore_ESPACIOS = r'[ ]+'
t_ignore_COMENT =  r'(/\*(.|\n)*?\*/)|(//.*)'

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

lexycalAnalyzer = lex.lex()