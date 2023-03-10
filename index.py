from SintacticalAnalyzer import sintacticalAnalyzer
from LexycalAnalyzer import lexycalAnalyzer
import os
try:
  dir_path = os.path.dirname(os.path.realpath(__file__))
  file = open(dir_path+'/'+"fuente.txt", "r")
  data = file.read()
  try:
    lexycalAnalyzer.input(data)  
    print('TOKEN - LEXEME - LINEA')
    while True:
      tok = lexycalAnalyzer.token()
      if not tok: break
      print('(',tok.type, ',',tok.value, ',',tok.lineno,')')

    sintacticalAnalyzer.parse(data)
    print("Analsis Sintáctico Correcto")
    print("Código Objeto Generado: objeto.ino")
  except Exception as e:
    print(e)
    print("Analisis Sintáctico Incorrecto")
    
except IndexError:
  print("Error reading file")