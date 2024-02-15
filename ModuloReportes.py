def Listainscritos ():
    import json
    x=open("inscritos.json" , 'r')
    mijson= json.load (x)
    listains=mijson[ "datos"]["inscripciones"]
    print(" Por favor de enter para mostrar Campers en estado inscrito")
    enter=input("")
    for i in listains:
        for llave,valor in i.items():
            print (f"{llave}: {valor}")
        print("-------------------------\n")
    with open('Inscritos.json', 'w', encoding="utf8") as x:
        json.dump(mijson, x, indent=4)



def ListaAprobaronExamen():
    import json
    
    with open("datos.json", 'r') as x:
        data = json.load(x)
    
    listaaprobaron = [camper for camper in data["Datos"]["Matriculados"] if camper["Estado"] == "Aprobado"]
    print(" Por favor de enter para mostrar Campers que aprobaron el examen inicial")
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
    print(" Por favor de enter para mostrar lista de trainers")
    enter=input("")

    for trainers in listatrainers:
        for llave, valor in trainers.items():
            print (f"{llave}: {valor}")
        print("-------------------------\n")
    with open('datos.json', 'w', encoding="utf8") as x:
            json.dump(data, x , indent=4)
    

import json

def bajo_rendimiento():
    try:
        with open('Notas.json', 'r', encoding="utf8") as file:
            mijson = json.load(file)

        estudiantes = mijson.get('Notas', {}).get('Matriculados', [])

        aprobados = []

        for estudiante in estudiantes:
            materias_rendimiento = [
                'Rendimiento_Fundamentos',
                'Rendimiento_programacion_web',
                'Rendimiento_programacion_formal',
                'Rendimiento_Base_datos',
                'Rendimiento_Backend'
            ]
            
            materias_bajo_rendimiento = [
                materia for materia in materias_rendimiento if materia in estudiante and estudiante[materia] == "Bajo rendimiento"
            ]

            if materias_bajo_rendimiento:
                aprobados.append({
                    "Nombre": estudiante['Nombre'],
                    "Apellido1": estudiante['Apellido1'],
                    "Telefono": estudiante['Telefono'],
                    "Materias_con_bajo_rendimiento": materias_bajo_rendimiento,
                })

        if aprobados:
            print("Estudiantes con bajo rendimiento:")
            for estudiante in aprobados:
                print("-----------------------------------")
                for key, val in estudiante.items():
                    if isinstance(val, list):
                        val = ', '.join(val)
                    print(f"{key}: {val}")
            print("-----------------------------------")

            with open('Notas.json', 'w', encoding="utf8") as file:
                json.dump(mijson, file, indent=4, ensure_ascii=False)

        else:
            print("No hay estudiantes con bajo rendimiento.")

    except FileNotFoundError:
        print("Archivo 'Notas.json' no encontrado.")





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

def Reporte6():
    import json

    with open('Salones.json', 'r', encoding="utf8") as file:
        mijson = json.load(file)

    # Inicializar un diccionario para almacenar resultados por módulo, ruta y entrenador
    resultados_por_modulo = {}

    # Recorrer los salones y alumnos
    for salon, datos_salon in mijson["Salones"].items():
        ruta = datos_salon["Ruta"]
        profesor = datos_salon["Profesor"]
        
        for alumno in datos_salon["Alumnos"]:
            # Verificar si la nota es mayor o igual a 60 en cada módulo
            for modulo in ["Fundamentos", "Programacion_web", "Programacion_formal", "Bases_datos", "Backend"]:
                nota_modulo = alumno[f"Nota_final_{modulo}"]
                try:
                    nota = float(nota_modulo)
                    if nota >= 60:
                        # Incrementar contador de aprobados
                        resultados_por_modulo.setdefault(modulo, {}).setdefault(ruta, {}).setdefault(profesor, {'Aprobados': 0, 'Perdidos': 0})['Aprobados'] += 1
                    else:
                        # Incrementar contador de perdidos
                        resultados_por_modulo.setdefault(modulo, {}).setdefault(ruta, {}).setdefault(profesor, {'Aprobados': 0, 'Perdidos': 0})['Perdidos'] += 1
                except ValueError:
                    # Manejar casos donde la nota no es un número válido
                    pass

    # Mostrar resultados por módulo, ruta y entrenador
    for modulo in ["Fundamentos", "Programacion_web", "Programacion_formal", "Bases_datos", "Backend"]:
        print(f"\nMódulo: {modulo}")
        for ruta in ["Java", "NodeCore", "NetCore"]:
            for profesor, resultados in resultados_por_modulo.get(modulo, {}).get(ruta, {}).items():
                aprobados = resultados['Aprobados']
                perdidos = resultados['Perdidos']
                print(f"Ruta: {ruta}, Profesor: {profesor} - Campers Aprobados: {aprobados}, Campers Perdidos: {perdidos}")

# Llamar a la función
Reporte6()
