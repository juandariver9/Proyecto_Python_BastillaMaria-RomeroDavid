def MainTrainersAñadir():
    import json
    try:
        with open('datos.json', 'r', encoding="utf8") as file:
            mijson = json.load(file)
    except FileNotFoundError:
        mijson = {"Datos": {"Trainers_Secundarios": []}}
    
    if 'Trainers_Secundarios' not in mijson['Datos']:
        mijson['Datos']['Trainers_Secundarios'] = []
        
    nuevo_id = max([inscripcion["id"] for inscripcion in mijson['Datos']['Trainers_Secundarios']], default=0) + 1
    nueva_inscripcion = {}
    nueva_inscripcion['id'] = nuevo_id if nuevo_id == 1 else nuevo_id
    nueva_inscripcion['Identificacion'] = int(input("Escriba el número de identificación: "))
    nueva_inscripcion['Nombre'] = str(input("Escriba el nombre: "))
    nueva_inscripcion['Apellido1'] = input("Escriba el apellido 1: ")
    nueva_inscripcion['Celular'] = int(input("Escriba el número de celular: "))
    nueva_inscripcion['Telefono'] = int(input("Escriba el número de teléfono: "))
    nueva_inscripcion['Horario'] = {
          "Clase1" : "Sin asignar",
          "Clase2" : "Sin asignar",
          "Clase3" : "Sin asignar",
          "Clase4" : "Sin asignar"
          }
    
    mijson['Datos']['Trainers_Secundarios'].append(nueva_inscripcion)
    
    with open('datos.json', 'w', encoding="utf8") as file:
        json.dump(mijson, file, indent=2)


def MainTrainersEliminar():
    import json

    tipo_entrenador = input("¿Desea eliminar un entrenador principal o secundario? (P/S): ").upper()
    
    if tipo_entrenador not in ['P', 'S']:
        print("Opción no válida. Debe ingresar 'P' para principal o 'S' para secundario.")
        return
    
    identificacion_a_eliminar = int(input("Ingrese el número de identificación del entrenador a eliminar: "))
    
    with open('datos.json', 'r', encoding="utf8") as file:
        mijson = json.load(file)
        
    eliminado = False
    
    if tipo_entrenador == 'P':
        entrenadores = mijson['Datos']['Trainer_Principales']
        for entrenador in entrenadores:
            if entrenador['id'] == identificacion_a_eliminar:
                entrenador['Identificacion'] = ''
                entrenador['Nombre'] = ''
                entrenador['Apellido1'] = ''
                entrenador['Celular'] = ''
                entrenador['Telefono'] = ''
                print("Entrenador principal eliminado exitosamente.")
                eliminado = True
                break
    else:
        entrenadores = mijson['Datos']['Trainers_Secundarios']
        
        for i, entrenador in enumerate(entrenadores):
            if entrenador['Identificacion'] == identificacion_a_eliminar:
                del mijson['Datos']['Trainers_Secundarios'][i]
                print("Entrenador secundario eliminado exitosamente.")
                eliminado = True
                break
        
    if not eliminado:
        print("No se encontró ningún entrenador con la identificación proporcionada.")
        
    with open('datos.json', 'w', encoding="utf8") as file:
        json.dump(mijson, file, indent=2)


def MainAsignarTrainers():
    def reindexar_IDs_entrenadores_secundarios(TrainersS):
        for i, trainer in enumerate(TrainersS, start=1):
            trainer['id'] = i
            
    import json

    with open('datos.json', 'r', encoding="utf8") as infile:
        mijson = json.load(infile)

    TrainersP = mijson['Datos']['Trainer_Principales']
    TrainersS = mijson['Datos']['Trainers_Secundarios']

    print("Estos son los puestos de Trainers principales que están desocupados en este momento:\n")

    for i, trainer in enumerate(TrainersP, start=1):
        if not trainer['Nombre']:
            print(f"Puesto #{i} desocupado")
        else:
            print(f"Puesto #{i} ocupado")

    añadir = int(input("En cuál de los espacios deseas añadir al trainer (1, 2 o 3): "))

    if añadir in [1, 2, 3]:
        if not TrainersP[añadir - 1]['Nombre']:
            print("Lista de entrenadores secundarios disponibles:")
            for trainer in TrainersS:
                print(f"ID: {trainer['id']}, Nombre: {trainer['Nombre']}")
            
            TS = int(input("Digite el ID del trainer secundario que desea pasar a principal: "))

            for trainer_index, trainer in enumerate(TrainersS):
                if trainer['id'] == TS:
                    TrainersP[añadir - 1]['Nombre'] = trainer['Nombre']
                    TrainersP[añadir - 1]['Apellido1'] = trainer['Apellido1']
                    TrainersP[añadir - 1]['Identificacion'] = trainer['Identificacion']
                    TrainersP[añadir - 1]['Celular'] = trainer['Celular']
                    TrainersP[añadir - 1]['Telefono'] = trainer['Telefono']
                    print(f"Trainer {trainer['Nombre']} asignado al puesto {añadir}")
                    TrainersS.pop(trainer_index)
                    reindexar_IDs_entrenadores_secundarios(TrainersS)
                    enter = input("")
                    break
            else:
                print("Trainer no encontrado")
                x = input("Presione Enter para continuar")

        else:
            print("Puesto ocupado")
            x = input("Presione Enter para continuar")
    else:
        print("Opción inválida. Debes seleccionar 1, 2 o 3.")
        x = input("Presione Enter para continuar")

    with open('datos.json', 'w', encoding="utf8") as outfile:
        json.dump(mijson, outfile, indent=2)

