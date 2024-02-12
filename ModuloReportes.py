def Listainscritos ():
    import json
    x=open("inscritos.json" , 'r')
    mijson= json.load (x)
    print (" Por favor de enter para mostrar Campers en estado inscrito")
    enter=input("")
    print(mijson)

Listainscritos()




def ListaAprobaronExamen():
    import json
    
    with open("datos.json", 'r') as x:
        data = json.load(x)
    
    listaaprobaron = [camper for camper in data["Datos"]["Matriculados"] if camper["Estado"] == "Aprobado"]

    print("Por favor, presiona Enter si deseas visualizar los campers que aprobaron el examen inicial")
    enter = input("")

    for camper in listaaprobaron:
        for llave, valor in camper.items():
            print (f"{llave}: {valor}")
        print("-------------------------\n")






