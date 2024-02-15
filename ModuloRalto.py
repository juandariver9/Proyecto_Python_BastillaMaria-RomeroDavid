def Riesgo_rendimiento():
    import json
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
Riesgo_rendimiento()
