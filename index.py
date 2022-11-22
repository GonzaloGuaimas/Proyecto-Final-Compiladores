from SintacticalAnalyzer import sintacticalAnalyzer
import os
try:
  dir_path = os.path.dirname(os.path.realpath(__file__))
  file = open(dir_path+'/'+"fuente.txt", "r")
  data = file.read()
  try:
    sintacticalAnalyzer.parse(data)
    print("Analsis correcto")
  except Exception as e:
    print(e)
    print("Analisis Incorrecto")
    
except IndexError:
  print("Error reading file")