def Listainscritos ():
    import json
    x=open("inscritos.json" , 'r')
    mijson= json.load (x)
    listains=mijson[ "datos"]["inscripciones"]
    print(" Por favor de enter para mostrar Campers en estado inscrito")
    enter=input("")
    print(listains)
    for i in listains:
        print("holiiiii1")
        for llave,valor in i.items():
            print("holiiiii2")
            print (f"{llave}: {valor}")
        print("-------------------------\n")
    with open('Inscritos.json', 'w', encoding="utf8") as x:
        json.dump(mijson, x, indent=4)






def ListaAprobaronExamen():
    import json
    
    with open("datos.json", 'r') as x:
        data = json.load(x)
    
    listaaprobaron = [camper for camper in data["Datos"]["Matriculados"] if camper["Estado"] == "Aprobado"]
    print(" Por favor de enter para mostrar Campers en estado inscrito")
    enter=input("")


    for camper in listaaprobaron:
        for llave, valor in camper.items():
            print (f"{llave}: {valor}")
        print("-------------------------\n")
    with open('datos.json', 'w', encoding="utf8") as x:
            json.dump(data, x, indent=4)









def listatrainerscampus():
    import json
    x=open("datos.json", 'r')
    data = json.load(x)

    listatrainers= data["Datos"]["Trainer_Principales"]
    print(" Por favor de enter para mostrar Campers en estado inscrito")
    enter=input("")

    for trainers in listatrainers:
        for llave, valor in trainers.items():
            print (f"{llave}: {valor}")
        print("-------------------------\n")
    with open('datos.json', 'w', encoding="utf8") as x:
            json.dump(data, x , indent=4)
    




def bajo_rendimiento():
    import json
    with open('Notas.json', 'r', encoding="utf8") as file:
        mijson = json.load(file)

    T = mijson['Notas']['Matriculados']
    
    aprobado = None  # Initialize aprobado outside the loop

    for index, value in enumerate(T):
        if 'Rendimiento_Fundamentos' in value and value['Rendimiento_Fundamentos'] == "Bajo rendimiento" or 'Rendimiento_programacion_web' in value and value['Rendimiento_programacion_web'] == "Bajo rendimiento" or 'Rendimiento_programacion_formal' in value and value['Rendimiento_programacion_formal'] == "Bajo rendimiento"or 'Rendimiento_Base_datos' in value and value['Rendimiento_Base_datos'] == "Bajo rendimiento" or 'Rendimiento_Backend' in value and value['Rendimiento_Backend'] == "Bajo rendimiento":
            aprobado = {
                "Nombre": value['Nombre'],
                "Apellido1": value['Apellido1'],
                "Telefono": value['Telefono'],
                "Nota_final_Fundamentos": value['Nota_final_Fundamentos'],
                "Rendimiento_Fundamentos": value['Rendimiento_Fundamentos'],
                "Nota_final_Programacion_web": value['Nota_final_Programacion_web'],
                "Rendimiento_programacion_web": value['Rendimiento_programacion_web'],
                "Nota_final_Programacion_formal": value['Nota_final_Programacion_formal'],
                "Rendimiento_programacion_formal": value['Rendimiento_programacion_formal'],
                "Nota_final_Bases_datos": value['Nota_final_Bases_datos'],
                "Rendimiento_Base_datos": value['Rendimiento_Base_datos'],
                "Nota_final_Backend": value['Nota_final_Backend'],
                "Rendimiento_Backend": value['Rendimiento_Backend'],
            }
           

    if aprobado:
        
        print(" Por favor de enter para mostrar Campers en estado inscrito")
        enter=input("")
        # Print the information in a structured way
        for key, val in aprobado.items():
            print(f"{key}: {val}")
        print("-----------------------------------")
        

    with open('Notas.json', 'w', encoding="utf8") as file:
        json.dump(mijson, file, indent=4)




