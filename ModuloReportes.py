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




def c_y_p_asociados_Java():
    import json
    with open('Salones.json', 'r', encoding="utf8") as file:
        mijson = json.load(file)

    Salones = mijson['Salones']

    for _, salon_info in Salones.items(): 
        if salon_info["Ruta"] == "Java":
            print(f"Campers y Trainer asociados a la ruta 'Java':")
            print(f"Profesor: {salon_info['Profesor']}")
            for alumno in salon_info['Alumnos']:
                print(f"Camper: {alumno['Nombre']} {alumno['Apellido1']}")
                print("--------------------------")

    with open('Salones.json', 'w', encoding="utf8") as x:
        json.dump(mijson, x, indent=2)
        
        
def c_y_p_asociados_Net():
    import json
    with open('Salones.json', 'r', encoding="utf8") as file:
        mijson = json.load(file)

    Salones = mijson['Salones']

    for _, salon_info in Salones.items(): 
        if salon_info["Ruta"] == "NetCore":
            print(f"Campers y Trainer asociados a la ruta '.Net':")
            print(f"Profesor: {salon_info['Profesor']}")
            for alumno in salon_info['Alumnos']:
                print(f"Camper: {alumno['Nombre']} {alumno['Apellido1']}")
                print("--------------------------")

    with open('Salones.json', 'w', encoding="utf8") as x:
        json.dump(mijson, x, indent=2)
        
def c_y_p_asociados_Node():
    import json
    with open('Salones.json', 'r', encoding="utf8") as file:
        mijson = json.load(file)

    Salones = mijson['Salones']

    for _, salon_info in Salones.items(): 
        if salon_info["Ruta"] == "NodeCore":
            print(f"Campers y Trainer asociados a la ruta 'Node':")
            print(f"Profesor: {salon_info['Profesor']}")
            for alumno in salon_info['Alumnos']:
                print(f"Camper: {alumno['Nombre']} {alumno['Apellido1']}")
                print("--------------------------")

    with open('Salones.json', 'w', encoding="utf8") as x:
        json.dump(mijson, x, indent=2)

def CampersAprobDesaprobModulo():
    import json
    
    
    
    print("Digite la ruta que desea mostrar")
    print("1 Java")
    print("2 Node")
    print("3 Net")
    Ruta = int(input("----->"))
    
    if Ruta == 1:
        #Acá deberia hacer un for para buscar todos los de ruta JAVA
        print("Desea ver en JAVA")
        print("Que filtro desea consultar: ")
        print("1. Fundamentos \t2. Programación Web")
        print("3. Programacion Formal \t4. Bases de Datos \t5. Backend")
        filtro = int(input("---->"))
        if filtro == 1:
            #Acá ya como está en ruta 
            print("Desea ver en Fundamentos")
            print("1. Aprobaron")
            print("2. Desaprobaron")
            ApDes = int(input("----->"))
            if ApDes == 1:
                print("Mostrar Aprobados")
            elif ApDes == 2:
                print("Mostrar Desaprobados")
            else:
                print("No existe esa categoria")
        elif filtro == 2:
            print("Desea ver en Programacion Web")
            print("1. Aprobaron")
            print("2. Desaprobaron")
            ApDes = int(input("----->"))
            if ApDes == 1:
                print("Mostrar Aprobados")
            elif ApDes == 2:
                print("Mostrar Desaprobados")
            else:
                print("No existe esa categoria")
        elif filtro == 3:
            print("Desea ver en Programacion Formal")
            print("1. Aprobaron")
            print("2. Desaprobaron")
            ApDes = int(input("----->"))
            if ApDes == 1:
                print("Mostrar Aprobados")
            elif ApDes == 2:
                print("Mostrar Desaprobados")
            else:
                print("No existe esa categoria")
        elif filtro == 4:
            print("Desea ver en Bases de Datos")
            print("1. Aprobaron")
            print("2. Desaprobaron")
            ApDes = int(input("----->"))
            if ApDes == 1:
                print("Mostrar Aprobados")
            elif ApDes == 2:
                print("Mostrar Desaprobados")
            else:
                print("No existe esa categoria")
        elif filtro == 5:
            print("Desea ver en Backend")
            print("1. Aprobaron")
            print("2. Desaprobaron")
            ApDes = int(input("----->"))
            if ApDes == 1:
                print("Mostrar Aprobados")
            elif ApDes == 2:
                print("Mostrar Desaprobados")
            else:
                print("No existe esa categoria")
        else:
            print("No existe ese filtro")
    elif Ruta == 2:
        print("Desea ver en NODE")
        print("Que filtro desea consultar: ")
        print("1. Fundamentos \t2. Programación Web")
        print("3. Programacion Formal \t4. Bases de Datos \t5. Backend")
        filtro = int(input("---->"))
        if filtro == 1:
            print("Desea ver en Fundamentos")
            print("1. Aprobaron")
            print("2. Desaprobaron")
            ApDes = int(input("----->"))
            if ApDes == 1:
                print("Mostrar Aprobados")
            elif ApDes == 2:
                print("Mostrar Desaprobados")
            else:
                print("No existe esa categoria")
        elif filtro == 2:
            print("Desea ver en Programacion Web")
            print("1. Aprobaron")
            print("2. Desaprobaron")
            ApDes = int(input("----->"))
            if ApDes == 1:
                print("Mostrar Aprobados")
            elif ApDes == 2:
                print("Mostrar Desaprobados")
            else:
                print("No existe esa categoria")
        elif filtro == 3:
            print("Desea ver en Programacion Formal")
            print("1. Aprobaron")
            print("2. Desaprobaron")
            ApDes = int(input("----->"))
            if ApDes == 1:
                print("Mostrar Aprobados")
            elif ApDes == 2:
                print("Mostrar Desaprobados")
            else:
                print("No existe esa categoria")
        elif filtro == 4:
            print("Desea ver en Bases de Datos")
            print("1. Aprobaron")
            print("2. Desaprobaron")
            ApDes = int(input("----->"))
            if ApDes == 1:
                print("Mostrar Aprobados")
            elif ApDes == 2:
                print("Mostrar Desaprobados")
            else:
                print("No existe esa categoria")
        elif filtro == 5:
            print("Desea ver en Backend")
            print("1. Aprobaron")
            print("2. Desaprobaron")
            ApDes = int(input("----->"))
            if ApDes == 1:
                print("Mostrar Aprobados")
            elif ApDes == 2:
                print("Mostrar Desaprobados")
            else:
                print("No existe esa categoria")
        else:
            print("No existe ese filtro")
    elif Ruta == 3:
        print("Desea ver en NET")
        print("Que filtro desea consultar: ")
        print("1. Fundamentos \t2. Programación Web")
        print("3. Programacion Formal \t4. Bases de Datos \t5. Backend")
        filtro = int(input("---->"))
        if filtro == 1:
            print("Desea ver en Fundamentos")
            print("1. Aprobaron")
            print("2. Desaprobaron")
            ApDes = int(input("----->"))
            if ApDes == 1:
                print("Mostrar Aprobados")
            elif ApDes == 2:
                print("Mostrar Desaprobados")
            else:
                print("No existe esa categoria")
        elif filtro == 2:
            print("Desea ver en Programacion Web")
            print("1. Aprobaron")
            print("2. Desaprobaron")
            ApDes = int(input("----->"))
            if ApDes == 1:
                print("Mostrar Aprobados")
            elif ApDes == 2:
                print("Mostrar Desaprobados")
            else:
                print("No existe esa categoria")
        elif filtro == 3:
            print("Desea ver en Programacion Formal")
            print("1. Aprobaron")
            print("2. Desaprobaron")
            ApDes = int(input("----->"))
            if ApDes == 1:
                print("Mostrar Aprobados")
            elif ApDes == 2:
                print("Mostrar Desaprobados")
            else:
                print("No existe esa categoria")
        elif filtro == 4:
            print("Desea ver en Bases de Datos")
            print("1. Aprobaron")
            print("2. Desaprobaron")
            ApDes = int(input("----->"))
            if ApDes == 1:
                print("Mostrar Aprobados")
            elif ApDes == 2:
                print("Mostrar Desaprobados")
            else:
                print("No existe esa categoria")
        elif filtro == 5:
            print("Desea ver en Backend")
            print("1. Aprobaron")
            print("2. Desaprobaron")
            ApDes = int(input("----->"))
            if ApDes == 1:
                print("Mostrar Aprobados")
            elif ApDes == 2:
                print("Mostrar Desaprobados")
            else:
                print("No existe esa categoria")
        else:
            print("No existe ese filtro")
    else:
        print("No existe esa categoria")