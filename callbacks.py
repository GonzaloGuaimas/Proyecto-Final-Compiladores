def cb_p_librerias(p):
  list_p = list(p)
  result = "".join(["#include <"]+list_p[3:4]+[".h>"]+["\n"])
  return result

def cb_p_variable(p):
  list_p = list(p)
  result = "".join([list_p[1]]+[" "]+[list_p[3]]+[";"]+["\n"])
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
   result = "".join(["pinMode("]+[list_p[5]]+[" , "]+[list_p[3]]+[" );"]+["\n"])
   return result

def cb_p_reservadas(p):
  list_p = list(p)
  return "".join([list_p[1]]+["()"]+[";"]+["\n"])


if __name__ == "__main__":
  res = cb_p_librerias([None, 'ADD', '<', 'nombreDeLibreria', '.txt', '>', '.', None])

  res = cb_p_variable([None, 'VAR', '<', 'entero', ':', 'MD1', '>', '.'])
  
  res = cb_p_asignacion([None, 'MD2', ':=', '3', None, None, None, None])

  res = cb_p_pin([None, 'PIN', '<', 'OUT', ':', 'MD1', '>', '.'])

  res = cb_p_reservadas([None, 'LEFT', '<', '>', None, None, None, None])

  # print(res)