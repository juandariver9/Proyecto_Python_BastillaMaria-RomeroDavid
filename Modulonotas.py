def NotasFundamentosProgramacion():
    import json
    
    with open('Notas.json', 'r', encoding="utf8") as file:
        mijson = json.load(file)
        
    T = mijson['Notas']['Matriculados']
    tel = int(input("Digite el Telefono: "))
    
    for index, value in enumerate(T):
        if 'Telefono' in value and value['Telefono'] == tel:
            print("Digite nota de la prueba teórica (0 a 100): ")
            nota_prueba_teorica = int(input("--->"))
            nota_prueba_teorica *= 0.3

            print("Digite nota de la prueba práctica (0 a 100): ")
            nota_prueba_practica = int(input("--->"))
            nota_prueba_practica *= 0.6

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

            rbajo = "Riesgo Bajo"
            ralto = "Riesgo Alto"
            
            rendimiento = {
                "Nota_final_Fundamentos": nota_final,
                "Rendimiento_Fundamentos": rbajo if nota_final >= 60 else ralto
            }

            # Actualizar los valores en el diccionario de estudiante correspondiente
            value.update(rendimiento)
            
            break  # Salir del bucle después de encontrar el teléfono correspondiente

    # Guardar los cambios en el archivo JSON
    with open('Notas.json', 'w', encoding="utf8") as file:
        json.dump(mijson, file, indent=4)

def NotasProgramacionWeb():
    import json
    
    with open('Notas.json', 'r', encoding="utf8") as file:
        mijson = json.load(file)
        
    T = mijson['Notas']['Matriculados']
    tel = int(input("Digite el Telefono: "))
    
    for index, value in enumerate(T):
        if 'Telefono' in value and value['Telefono'] == tel:
            print("Digite nota de la prueba teórica (0 a 100): ")
            nota_prueba_teorica = int(input("--->"))
            nota_prueba_teorica *= 0.3

            print("Digite nota de la prueba práctica (0 a 100): ")
            nota_prueba_practica = int(input("--->"))
            nota_prueba_practica *= 0.6

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

            rbajo = "Riesgo Bajo"
            ralto = "Riesgo Alto"
            
            rendimiento = {
                "Nota_final_Programacion_web": nota_final,
                "Rendimiento_programacion_web": rbajo if nota_final >= 60 else ralto
            }

            value.update(rendimiento)
            
            break

    with open('Notas.json', 'w', encoding="utf8") as file:
        json.dump(mijson, file, indent=4)

def NotasProgramacionFormal():

    import json
    
    with open('Notas.json', 'r', encoding="utf8") as file:
        mijson = json.load(file)
        
    T = mijson['Notas']['Matriculados']
    tel = int(input("Digite el Telefono: "))
    
    for index, value in enumerate(T):
        if 'Telefono' in value and value['Telefono'] == tel:
            print("Digite nota de la prueba teórica (0 a 100): ")
            nota_prueba_teorica = int(input("--->"))
            nota_prueba_teorica *= 0.3

            print("Digite nota de la prueba práctica (0 a 100): ")
            nota_prueba_practica = int(input("--->"))
            nota_prueba_practica *= 0.6

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

            rbajo = "Riesgo Bajo"
            ralto = "Riesgo Alto"
            
            rendimiento = {
                "Nota_final_Programacion_formal": nota_final,
                "Rendimiento_programacion_formal": rbajo if nota_final >= 60 else ralto
            }

            value.update(rendimiento)
            
            break

    with open('Notas.json', 'w', encoding="utf8") as file:
        json.dump(mijson, file, indent=4)

def NotasFinalesBasesDeDatos():

    import json
    
    with open('Notas.json', 'r', encoding="utf8") as file:
        mijson = json.load(file)
        
    T = mijson['Notas']['Matriculados']
    tel = int(input("Digite el Telefono: "))
    
    for index, value in enumerate(T):
        if 'Telefono' in value and value['Telefono'] == tel:
            print("Digite nota de la prueba teórica (0 a 100): ")
            nota_prueba_teorica = int(input("--->"))
            nota_prueba_teorica *= 0.3

            print("Digite nota de la prueba práctica (0 a 100): ")
            nota_prueba_practica = int(input("--->"))
            nota_prueba_practica *= 0.6

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

            rbajo = "Riesgo Bajo"
            ralto = "Riesgo Alto"
            
            rendimiento = {
                "Nota_final_Bases_datos": nota_final,
                "Rendimiento_Base_datos": rbajo if nota_final >= 60 else ralto
            }

            value.update(rendimiento)
            
            break

    with open('Notas.json', 'w', encoding="utf8") as file:
        json.dump(mijson, file, indent=4) 

def NotasFinalesBackend():
    import json
    
    with open('Notas.json', 'r', encoding="utf8") as file:
        mijson = json.load(file)
        
    T = mijson['Notas']['Matriculados']
    tel = int(input("Digite el Telefono: "))
    
    for index, value in enumerate(T):
        if 'Telefono' in value and value['Telefono'] == tel:
            print("Digite nota de la prueba teórica (0 a 100): ")
            nota_prueba_teorica = int(input("--->"))
            nota_prueba_teorica *= 0.3

            print("Digite nota de la prueba práctica (0 a 100): ")
            nota_prueba_practica = int(input("--->"))
            nota_prueba_practica *= 0.6

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

            rbajo = "Riesgo Bajo"
            ralto = "Riesgo Alto"
            
            rendimiento = {
                "Nota_final_Backend": nota_final,
                "Rendimiento_Backend": rbajo if nota_final >= 60 else ralto
            }

            value.update(rendimiento)
            
            break

    with open('Notas.json', 'w', encoding="utf8") as file:
        json.dump(mijson, file, indent=4) 




