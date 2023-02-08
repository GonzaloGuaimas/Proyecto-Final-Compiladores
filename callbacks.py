def cb_p_librerias(p):
  list_p = list(p)
  result = "".join(["#include <"]+list_p[3:4]+[".h>"]+["\n"])
  return result

def cb_p_variable(p):
  list_p = list(p)
  valor = ''
  if (list_p[1] == 'entero'):
    valor = 'int'
  elif (list_p[1] == 'texto'):
    valor = 'String'
  elif (list_p[1] == 'decimal'):
    valor = 'decimal'
  elif (list_p[1] == 'lógico'):
    valor = 'bool'

  result = "".join([valor]+[" "]+[list_p[3]]+[";"]+["\n"])
  return result

def cb_p_asignacion(p):
  list_p = list(p)
  result = "".join([list_p[1]]+[" := "]+[str(list_p[3])]+[";"]+["\n"])
  return result

def cb_p_condicional(p):
  result = "".join(["if ("]+[") "]+ ["{"]+["\n"]+["}"]+["\n"])
  return result

def cb_p_procedimiento(p):
  list_p = list(p)
  result = "".join([list_p[6]]+[" "]+[list_p[1]]+["()"]+["{"]+["\n"]+["}"]+["\n"])
  return result

def cb_p_funcion(p):
  list_p = list(p)
  result = "".join([list_p[5]]+[list_p[2]]+["()"]+["{"]+["\n"]+["}"]+["\n"])
  return result

def cb_p_comparacion(p):
  list_p = list(p)
  result = "".join([list_p[5]]+[" "]+[list_p[3]]+["("]+[list_p[7]]+[");"]+["\n"])
  return result

def cb_p_pin(p):
   list_p = list(p)
   valor = ''
   if (list_p[3] == 'OUT'):
     valor = 'OUTPUT'
   elif (list_p[3] == 'INP'):
     valor = 'INPUT'
   result = "".join(["pinMode("]+[list_p[5]]+[" , "]+[valor]+[" );"]+["\n"])
   return result

def cb_p_reservadas(p):
  list_p = list(p)
  valor = ''
  if (list_p[1] == 'FOWARD'):
    valor = 'avanzar'
  elif (list_p[1] == 'BACKWARD'):
    valor = 'retroceder'
  elif (list_p[1] == 'LEFT'):
    valor = 'giro_izquierda'
  elif (list_p[1] == 'RIGHT'):
    valor = 'giro_derecha'
  elif (list_p[1] == 'WAIT'):
    valor = 'esperar'
  elif (list_p[1] == 'STOP'):
    valor = 'parar'
  return "".join([valor]+["()"]+[";"]+["\n"])


if __name__ == "__main__":
  res = cb_p_librerias([None, 'ADD', '<', 'nombreDeLibreria', '.txt', '>', '.', None])

  res = cb_p_variable([None, 'VAR', '<', 'entero', ':', 'MD1', '>', '.'])
  
  res = cb_p_asignacion([None, 'MD2', ':=', '3', None, None, None, None])

  res = cb_p_pin([None, 'PIN', '<', 'OUT', ':', 'MD1', '>', '.'])

  res = cb_p_reservadas([None, 'LEFT', '<', '>', None, None, None, None])

  # print(res)