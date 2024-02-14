#Mostrar cuantos campers perdieron y aprobaron cada uno de los módulos teniendo en cuenta la ruta de entrenamiento 
#y el entrenador encargado.


def fundamentosaprobaron ():
    import json
    
    with open("datos.json", 'r') as x:
        data = json.load(x)
    
    listaaprobaron = [camper for camper in data["Datos"]["Matriculados"] if camper["rendimiento_fundamentos"] == "Riesgo bajo"]

    print("Por favor, presiona Enter si deseas visualizar los campers que aprobaron el modulo de fundamentos ")
    enter = input("")

    for camper in listaaprobaron:
        for llave, valor in camper.items():
            print (f"{llave}: {valor}")
        print("-------------------------\n")




def fundamentodesaprobaron():
 import json
    
 with open("datos.json", 'r') as x:
    data = json.load(x)
    
    listadesaprobaron = [camper for camper in data["Datos"]["Matriculados"] if camper["Rendimiento_fundamentos"] == "Bajo rendimiento"]

    print("Por favor, presiona Enter si deseas visualizar los campers que aprobaron el modulo de fundamentos ")
    enter = input("")

    for camper in listadesaprobaron:
        for llave, valor in camper.items():
            print (f"{llave}: {valor}")
        print("-------------------------\n")


def web_aprobaron ():
    import json
    
    with open("datos.json", 'r') as x:
        data = json.load(x)
    
    listaaprobaron = [camper for camper in data["Datos"]["Matriculados"] if camper["Rendimiento_programacin_web"] == "Riesgo bajo"]

    print("Por favor, presiona Enter si deseas visualizar los campers que aprobaron el modulo de fundamentos ")
    enter = input("")

    for camper in listaaprobaron:
        for llave, valor in camper.items():
            print (f"{llave}: {valor}")
        print("-------------------------\n")




def web_desaprobaron():
 import json
    
 with open("datos.json", 'r') as x:
    data = json.load(x)
    
    listadesaprobaron = [camper for camper in data["Datos"]["Matriculados"] if camper["Rendimiento_programacin_web"] == "Bajo rendimiento"]

    print("Por favor, presiona Enter si deseas visualizar los campers que aprobaron el modulo de fundamentos ")
    enter = input("")

    for camper in listadesaprobaron:
        for llave, valor in camper.items():
            print (f"{llave}: {valor}")
        print("-------------------------\n")



def formal_aprobaron ():
    import json
    
    with open("datos.json", 'r') as x:
        data = json.load(x)
    
    listaaprobaron = [camper for camper in data["Datos"]["Matriculados"] if camper["Rendimiento_programacion_formal"] == "Riesgo bajo"]

    print("Por favor, presiona Enter si deseas visualizar los campers que aprobaron el modulo de fundamentos ")
    enter = input("")

    for camper in listaaprobaron:
        for llave, valor in camper.items():
            print (f"{llave}: {valor}")
        print("-------------------------\n")




def formal_desaprobaron():
 import json
    
 with open("datos.json", 'r') as x:
    data = json.load(x)
    
    listadesaprobaron = [camper for camper in data["Datos"]["Matriculados"] if camper["Rendimiento_programacion_formal"] == "Bajo rendimiento"]

    print("Por favor, presiona Enter si deseas visualizar los campers que aprobaron el modulo de fundamentos ")
    enter = input("")

    for camper in listadesaprobaron:
        for llave, valor in camper.items():
            print (f"{llave}: {valor}")
        print("-------------------------\n")





def Base_aprobaron ():
    import json
    
    with open("datos.json", 'r') as x:
        data = json.load(x)
    
    listaaprobaron = [camper for camper in data["Datos"]["Matriculados"] if camper["Rendimiento_Base_datos"] == "Riesgo bajo"]

    print("Por favor, presiona Enter si deseas visualizar los campers que aprobaron el modulo de fundamentos ")
    enter = input("")

    for camper in listaaprobaron:
        for llave, valor in camper.items():
            print (f"{llave}: {valor}")
        print("-------------------------\n")




def Base_desaprobaron():
 import json
    
 with open("datos.json", 'r') as x:
    data = json.load(x)
    
    listadesaprobaron = [camper for camper in data["Datos"]["Matriculados"] if camper["Rendimiento_Base_datos"] == "Bajo rendimiento"]

    print("Por favor, presiona Enter si deseas visualizar los campers que aprobaron el modulo de fundamentos ")
    enter = input("")

    for camper in listadesaprobaron:
        for llave, valor in camper.items():
            print (f"{llave}: {valor}")
        print("-------------------------\n")





def Backend_aprobaron ():
    import json
    
    with open("datos.json", 'r') as x:
        data = json.load(x)
    
    listaaprobaron = [camper for camper in data["Datos"]["Matriculados"] if camper["Rendimiento_Backend"] == "Riesgo bajo"]

    print("Por favor, presiona Enter si deseas visualizar los campers que aprobaron el modulo de fundamentos ")
    enter = input("")

    for camper in listaaprobaron:
        for llave, valor in camper.items():
            print (f"{llave}: {valor}")
        print("-------------------------\n")




def Backend_desaprobaron():
 import json
    
 with open("datos.json", 'r') as x:
    data = json.load(x)
    
    listadesaprobaron = [camper for camper in data["Datos"]["Matriculados"] if camper["Rendimiento_Backend"] == "Bajo rendimiento"]

    print("Por favor, presiona Enter si deseas visualizar los campers que aprobaron el modulo de fundamentos ")
    enter = input("")

    for camper in listadesaprobaron:
        for llave, valor in camper.items():
            print (f"{llave}: {valor}")
        print("-------------------------\n")





