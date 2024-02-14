import json

def MainCamperAñadir():
    with open('inscritos.json', 'r', encoding="utf8") as file:
        mijson = json.load(file)
    
    def mainCamper():
        estado = "Inscrito"
        nuevo_id = max([inscripcion["id"] for inscripcion in mijson['datos']['inscripciones']], default=0) + 1
        
        nueva_inscripcion = {}
        nueva_inscripcion['id'] = nuevo_id
        nueva_inscripcion['Identificacion'] = int(input("Escriba el número de identificación: "))
        nueva_inscripcion['Nombre'] = input("Escriba el nombre: ")
        nueva_inscripcion['Apellido1'] = input("Escriba el apellido 1: ")
        nueva_inscripcion['Apellido2'] = input("Escriba el apellido 2: ")
        nueva_inscripcion['Direccion'] = input("Escriba la dirección: ")
        nueva_inscripcion['Acudiente'] = input("Escriba el nombre de su acudiente (opcional): ")
        nueva_inscripcion['Celular'] = int(input("Escriba el número de celular: "))
        nueva_inscripcion['Telefono'] = int(input("Escriba el número de teléfono: "))
        nueva_inscripcion['Estado'] = estado

        mijson['datos']['inscripciones'].append(nueva_inscripcion)
        
        with open('inscritos.json', 'w', encoding="utf8") as file:
            json.dump(mijson, file, indent=2)
    
    mainCamper()

import json

def MainCamperAprobados():
    with open('inscritos.json', 'r', encoding="utf8") as file:
        mijson = json.load(file)
    
    with open('datos.json', 'r', encoding="utf8") as file:
        mijson2 = json.load(file)
    
    with open('CampAprob.json', 'r', encoding="utf8") as file:
        mijson3 = json.load(file)
    
    with open('Notas.json','r',encoding="utf8") as file:
        mijson4 = json.load(file)
    
    with open('Salones.json','r',encoding="utf8") as file:
        mijson5 = json.load(file)

    Salones = mijson5['Salones']
    listainscritos = mijson['datos']['inscripciones']
    estadoA = "Aprobado"
    estadoR = "Reprobado"
    riesgoB = "Sin riesgo"
    riesgoM = "Riesgo alto"
    y = int(input("Escriba el ID del estudiante a actualizar: "))
    
    for i, inscripcion in enumerate(listainscritos):
        if inscripcion['id'] == y:
            notapractica = int(input("Digite la nota de la prueba práctica: "))
            notateorica = int(input("Digite la nota de la prueba teórica: "))
            notafinal = (notapractica + notateorica) / 2

            aprobado1 = {
                "Nombre": inscripcion['Nombre'],
                "Apellido1": inscripcion['Apellido1'],
                "Telefono": inscripcion['Telefono'],
                "Nota_final_Fundamentos": "",
                "Rendimiento_Fundamentos": "",
                "Nota_final_Programacion_web": "",
                "Rendimiento_programacion_web": "",
                "Nota_final_Programacion_formal": "",
                "Rendimiento_programacion_formal": "",
                "Nota_final_Bases_datos": "",
                "Rendimiento_Base_datos": "",
                "Nota_final_Backend": "",
                "Rendimiento_Backend": ""
            }
            
            # Buscar un salón con menos de 33 alumnos y agregar al alumno
            for salon_numero, salon_info in Salones.items():
                if len(salon_info["Alumnos"]) < 33:
                    aprobado1["Salon"] = salon_numero
                    salon_info["Alumnos"].append(aprobado1)
                    print(f"El estudiante {inscripcion['Nombre']} se agregó al salón {salon_numero}.")
                    break
            else:
                print("No hay salones disponibles con menos de 33 alumnos.")
                # Aquí puedes agregar la lógica para manejar el caso en el que no haya salones disponibles.
            
            aprobado = {
                "Nombre": inscripcion['Nombre'],
                "Apellido1": inscripcion['Apellido1'],
                "Apellido2": inscripcion['Apellido2'],
                "Direccion": inscripcion['Direccion'],
                "Nombre Acudiente": inscripcion['Acudiente'],
                "Celular": inscripcion['Celular'],
                "Telefono": inscripcion['Telefono'],
                "Estado": estadoA if notafinal >= 60 else estadoR,
                "Fecha de inicio": input("Escriba la fecha de inicio del estudiante: "),
                "Fecha de finalizacion": input("Escriba la fecha de finalización: "),
                "Riesgo": riesgoB if notafinal >= 60 else riesgoM,
                "Trainer": salon_info["Profesor"],
                "Ruta" : salon_info["Ruta"],
                "Salon": salon_numero
            }
            # Resto del código
            mijson2['Datos']['Matriculados'].append(aprobado)
            if notafinal >= 60:
                mijson3['Datos']['Aprobados'].append(aprobado)
            mijson4['Notas']['Matriculados'].append(aprobado1)
                
            listainscritos.pop(i)
            with open('inscritos.json', 'w', encoding="utf8") as file:
                json.dump(mijson, file, indent=2)
            with open('datos.json', 'w', encoding="utf8") as file:
                json.dump(mijson2, file, indent=2)
            with open('CampAprob.json','w', encoding="utf8") as file:
                json.dump(mijson3, file, indent=2)
            with open('Notas.json', 'w', encoding="utf8") as file:
                json.dump(mijson4, file, indent=2)
            
            # Actualizar Salones.json con el nuevo alumno
            with open('Salones.json', 'w', encoding="utf8") as file:
                json.dump(mijson5, file, indent=2)
            
            break  # Break the loop after processing one entry