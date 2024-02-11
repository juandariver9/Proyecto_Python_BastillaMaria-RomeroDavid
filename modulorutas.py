
def Rutas():
 import json
 x= open (Rutas.json)
 mijson=json.load(x)

 print(" Por favor defina la cantidad de nuevas rutas que desea agregar")
 cantidad=int(input(""))
 for i in range (cantidad):
  Nombre=input("Digite el nombre de la nueva ruta")
  


