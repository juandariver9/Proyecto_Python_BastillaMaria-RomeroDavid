def NotasFundamentosProgramacion():
    import json
    # Cargar datos de Notas.json
    with open('Notas.json', 'r', encoding="utf8") as file:
        notas_data = json.load(file)
    
    # Cargar datos de Salones.json
    with open('Salones.json', 'r', encoding="utf8") as file:
        salones_data = json.load(file)
    
    # Obtener la lista de alumnos con sus notas
    alumnos_notas = notas_data['Notas']['Matriculados']
    
    # Obtener el teléfono del alumno
    telefono = int(input("Digite el Telefono: "))
    
    # Buscar al alumno en la lista de notas
    for alumno_notas in alumnos_notas:
        if alumno_notas['Telefono'] == telefono:
            # Calcular la nota final del estudiante
            nota_prueba_teorica = float(input("Digite nota de la prueba teórica (0 a 100): ")) * 0.3
            nota_prueba_practica = float(input("Digite nota de la prueba práctica (0 a 100): ")) * 0.6
            
            print("Digite la cantidad de quizes realizados durante el módulo: ")
            cantidad_quizes = int(input("--->"))
            suma_quizes = 0
            for j in range(cantidad_quizes):
                nota_quiz = int(input(f"Digite nota del quiz #{j + 1} (0 a 100): "))
                suma_quizes += nota_quiz
            promedio_quizes = suma_quizes / cantidad_quizes

            print("Digite la cantidad de trabajos realizados durante el módulo: ")
            cantidad_trabajos = int(input("--->"))
            suma_trabajos = 0
            for k in range(cantidad_trabajos):
                nota_trabajo = int(input(f"Digite nota del trabajo #{k + 1} (0 a 100): "))
                suma_trabajos += nota_trabajo
            promedio_trabajos = suma_trabajos / cantidad_trabajos
            
            total_talleres = (promedio_quizes + promedio_trabajos) / 2 * 0.1
            nota_final = nota_prueba_practica + nota_prueba_teorica + total_talleres
            
            # Determinar el rendimiento del estudiante
            rendimiento = "Riesgo Bajo" if nota_final >= 60 else "Bajo rendimiento"
            
            # Actualizar las notas del alumno en Salones.json
            for salon_numero, salon_info in salones_data['Salones'].items():
                for alumno_salon in salon_info['Alumnos']:
                    if alumno_salon['Telefono'] == telefono:
                        alumno_salon['Nota_final_Fundamentos'] = nota_final
                        alumno_salon['Rendimiento_Fundamentos'] = rendimiento
                        break
            
            break  # Salir del bucle después de encontrar al alumno
    
    # Guardar los cambios en Salones.json
    with open('Salones.json', 'w', encoding="utf8") as file:
        json.dump(salones_data, file, indent=2)

def NotasProgramacionWeb():
    import json
    # Cargar datos de Notas.json
    with open('Notas.json', 'r', encoding="utf8") as file:
        notas_data = json.load(file)
    
    # Cargar datos de Salones.json
    with open('Salones.json', 'r', encoding="utf8") as file:
        salones_data = json.load(file)
    
    # Obtener la lista de alumnos con sus notas
    alumnos_notas = notas_data['Notas']['Matriculados']
    
    # Obtener el teléfono del alumno
    telefono = int(input("Digite el Telefono: "))
    
    # Buscar al alumno en la lista de notas
    for alumno_notas in alumnos_notas:
        if alumno_notas['Telefono'] == telefono:
            # Calcular la nota final del estudiante
            nota_prueba_teorica = float(input("Digite nota de la prueba teórica (0 a 100): ")) * 0.3
            nota_prueba_practica = float(input("Digite nota de la prueba práctica (0 a 100): ")) * 0.6
            
            print("Digite la cantidad de quizes realizados durante el módulo: ")
            cantidad_quizes = int(input("--->"))
            suma_quizes = 0
            for j in range(cantidad_quizes):
                nota_quiz = int(input(f"Digite nota del quiz #{j + 1} (0 a 100): "))
                suma_quizes += nota_quiz
            promedio_quizes = suma_quizes / cantidad_quizes

            print("Digite la cantidad de trabajos realizados durante el módulo: ")
            cantidad_trabajos = int(input("--->"))
            suma_trabajos = 0
            for k in range(cantidad_trabajos):
                nota_trabajo = int(input(f"Digite nota del trabajo #{k + 1} (0 a 100): "))
                suma_trabajos += nota_trabajo
            promedio_trabajos = suma_trabajos / cantidad_trabajos
            
            total_talleres = (promedio_quizes + promedio_trabajos) / 2 * 0.1
            nota_final = nota_prueba_practica + nota_prueba_teorica + total_talleres
            
            # Determinar el rendimiento del estudiante
            rendimiento = "Riesgo Bajo" if nota_final >= 60 else "Bajo rendimiento"
            
            # Actualizar las notas del alumno en Salones.json
            for salon_numero, salon_info in salones_data['Salones'].items():
                for alumno_salon in salon_info['Alumnos']:
                    if alumno_salon['Telefono'] == telefono:
                        alumno_salon['Nota_final_Programacion_web'] = nota_final
                        alumno_salon['Rendimiento_programacion_web'] = rendimiento
                        break
            
            break  # Salir del bucle después de encontrar al alumno
    
    # Guardar los cambios en Salones.json
    with open('Salones.json', 'w', encoding="utf8") as file:
        json.dump(salones_data, file, indent=2)

def NotasProgramacionFormal():
    import json
    # Cargar datos de Notas.json
    with open('Notas.json', 'r', encoding="utf8") as file:
        notas_data = json.load(file)
    
    # Cargar datos de Salones.json
    with open('Salones.json', 'r', encoding="utf8") as file:
        salones_data = json.load(file)
    
    # Obtener la lista de alumnos con sus notas
    alumnos_notas = notas_data['Notas']['Matriculados']
    
    # Obtener el teléfono del alumno
    telefono = int(input("Digite el Telefono: "))
    
    # Buscar al alumno en la lista de notas
    for alumno_notas in alumnos_notas:
        if alumno_notas['Telefono'] == telefono:
            # Calcular la nota final del estudiante
            nota_prueba_teorica = float(input("Digite nota de la prueba teórica (0 a 100): ")) * 0.3
            nota_prueba_practica = float(input("Digite nota de la prueba práctica (0 a 100): ")) * 0.6
            
            print("Digite la cantidad de quizes realizados durante el módulo: ")
            cantidad_quizes = int(input("--->"))
            suma_quizes = 0
            for j in range(cantidad_quizes):
                nota_quiz = int(input(f"Digite nota del quiz #{j + 1} (0 a 100): "))
                suma_quizes += nota_quiz
            promedio_quizes = suma_quizes / cantidad_quizes

            print("Digite la cantidad de trabajos realizados durante el módulo: ")
            cantidad_trabajos = int(input("--->"))
            suma_trabajos = 0
            for k in range(cantidad_trabajos):
                nota_trabajo = int(input(f"Digite nota del trabajo #{k + 1} (0 a 100): "))
                suma_trabajos += nota_trabajo
            promedio_trabajos = suma_trabajos / cantidad_trabajos
            
            total_talleres = (promedio_quizes + promedio_trabajos) / 2 * 0.1
            nota_final = nota_prueba_practica + nota_prueba_teorica + total_talleres
            
            # Determinar el rendimiento del estudiante
            rendimiento = "Riesgo Bajo" if nota_final >= 60 else "Bajo rendimiento"
            
            # Actualizar las notas del alumno en Salones.json
            for salon_numero, salon_info in salones_data['Salones'].items():
                for alumno_salon in salon_info['Alumnos']:
                    if alumno_salon['Telefono'] == telefono:
                        alumno_salon['Nota_final_Programacion_formal'] = nota_final
                        alumno_salon['Rendimiento_programacion_formal'] = rendimiento
                        break
            
            break  # Salir del bucle después de encontrar al alumno
    
    # Guardar los cambios en Salones.json
    with open('Salones.json', 'w', encoding="utf8") as file:
        json.dump(salones_data, file, indent=2)

def NotasFinalesBasesDeDatos():
    import json
    # Cargar datos de Notas.json
    with open('Notas.json', 'r', encoding="utf8") as file:
        notas_data = json.load(file)
    
    # Cargar datos de Salones.json
    with open('Salones.json', 'r', encoding="utf8") as file:
        salones_data = json.load(file)
    
    # Obtener la lista de alumnos con sus notas
    alumnos_notas = notas_data['Notas']['Matriculados']
    
    # Obtener el teléfono del alumno
    telefono = int(input("Digite el Telefono: "))
    
    # Buscar al alumno en la lista de notas
    for alumno_notas in alumnos_notas:
        if alumno_notas['Telefono'] == telefono:
            # Calcular la nota final del estudiante
            nota_prueba_teorica = float(input("Digite nota de la prueba teórica (0 a 100): ")) * 0.3
            nota_prueba_practica = float(input("Digite nota de la prueba práctica (0 a 100): ")) * 0.6
            
            print("Digite la cantidad de quizes realizados durante el módulo: ")
            cantidad_quizes = int(input("--->"))
            suma_quizes = 0
            for j in range(cantidad_quizes):
                nota_quiz = int(input(f"Digite nota del quiz #{j + 1} (0 a 100): "))
                suma_quizes += nota_quiz
            promedio_quizes = suma_quizes / cantidad_quizes

            print("Digite la cantidad de trabajos realizados durante el módulo: ")
            cantidad_trabajos = int(input("--->"))
            suma_trabajos = 0
            for k in range(cantidad_trabajos):
                nota_trabajo = int(input(f"Digite nota del trabajo #{k + 1} (0 a 100): "))
                suma_trabajos += nota_trabajo
            promedio_trabajos = suma_trabajos / cantidad_trabajos
            
            total_talleres = (promedio_quizes + promedio_trabajos) / 2 * 0.1
            nota_final = nota_prueba_practica + nota_prueba_teorica + total_talleres
            
            # Determinar el rendimiento del estudiante
            rendimiento = "Riesgo Bajo" if nota_final >= 60 else "Bajo rendimiento"
            
            # Actualizar las notas del alumno en Salones.json
            for salon_numero, salon_info in salones_data['Salones'].items():
                for alumno_salon in salon_info['Alumnos']:
                    if alumno_salon['Telefono'] == telefono:
                        alumno_salon['Nota_final_Bases_datos'] = nota_final
                        alumno_salon['Rendimiento_Base_datos'] = rendimiento
                        break
            
            break  # Salir del bucle después de encontrar al alumno
    
    # Guardar los cambios en Salones.json
    with open('Salones.json', 'w', encoding="utf8") as file:
        json.dump(salones_data, file, indent=2)

def NotasFinalesBackend():
    import json
    # Cargar datos de Notas.json
    with open('Notas.json', 'r', encoding="utf8") as file:
        notas_data = json.load(file)
    
    # Cargar datos de Salones.json
    with open('Salones.json', 'r', encoding="utf8") as file:
        salones_data = json.load(file)
    
    # Obtener la lista de alumnos con sus notas
    alumnos_notas = notas_data['Notas']['Matriculados']
    
    # Obtener el teléfono del alumno
    telefono = int(input("Digite el Telefono: "))
    
    # Buscar al alumno en la lista de notas
    for alumno_notas in alumnos_notas:
        if alumno_notas['Telefono'] == telefono:
            # Calcular la nota final del estudiante
            nota_prueba_teorica = float(input("Digite nota de la prueba teórica (0 a 100): ")) * 0.3
            nota_prueba_practica = float(input("Digite nota de la prueba práctica (0 a 100): ")) * 0.6
            
            print("Digite la cantidad de quizes realizados durante el módulo: ")
            cantidad_quizes = int(input("--->"))
            suma_quizes = 0
            for j in range(cantidad_quizes):
                nota_quiz = int(input(f"Digite nota del quiz #{j + 1} (0 a 100): "))
                suma_quizes += nota_quiz
            promedio_quizes = suma_quizes / cantidad_quizes

            print("Digite la cantidad de trabajos realizados durante el módulo: ")
            cantidad_trabajos = int(input("--->"))
            suma_trabajos = 0
            for k in range(cantidad_trabajos):
                nota_trabajo = int(input(f"Digite nota del trabajo #{k + 1} (0 a 100): "))
                suma_trabajos += nota_trabajo
            promedio_trabajos = suma_trabajos / cantidad_trabajos
            
            total_talleres = (promedio_quizes + promedio_trabajos) / 2 * 0.1
            nota_final = nota_prueba_practica + nota_prueba_teorica + total_talleres
            
            # Determinar el rendimiento del estudiante
            rendimiento = "Riesgo Bajo" if nota_final >= 60 else "Bajo rendimiento"
            
            # Actualizar las notas del alumno en Salones.json
            for salon_numero, salon_info in salones_data['Salones'].items():
                for alumno_salon in salon_info['Alumnos']:
                    if alumno_salon['Telefono'] == telefono:
                        alumno_salon['Nota_final_Backend'] = nota_final
                        alumno_salon['Rendimiento_Backend'] = rendimiento
                        break
            
            break  # Salir del bucle después de encontrar al alumno
    
    # Guardar los cambios en Salones.json
    with open('Salones.json', 'w', encoding="utf8") as file:
        json.dump(salones_data, file, indent=2)

def Mostrarlistarendimiento():
    import json
    with open('Notas.json', 'r') as file:
        mijson = json.load(file)
        listacampers = mijson["Notas"]["Matriculados"]

        print("Por Favor presione alguna tecla para mostrar lista de rendimiento de campers")
        for i in listacampers:
            for llave, valor in i.items():
                print(f"{llave}: {valor}")
            print("-----------------------------")
        print("Por Favor presione alguna tecla para mostrar lista de rendimiento de campers")
        enter = input("")

    with open('Notas.json', 'w') as file:
        json.dump(mijson, file, indent=4)

def Mostrar_rendimiento():
    import json
    with open('Notas.json', 'r', encoding="utf8") as file:
        mijson = json.load(file)

    T = mijson['Notas']['Matriculados']
    tel = int(input("Digite el Telefono de camper para visualizar: "))
    
    aprobado = None  # Initialize aprobado outside the loop

    for index, value in enumerate(T):
        if 'Telefono' in value and value['Telefono'] == tel:
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
        print("Presione enter para mostrar el rendimiento del camper")
        
        # Print the information in a structured way
        for key, val in aprobado.items():
            print(f"{key}: {val}")

    with open('Notas.json', 'w', encoding="utf8") as file:
            json.dump(mijson, file, indent=4)
    enter = input("")













