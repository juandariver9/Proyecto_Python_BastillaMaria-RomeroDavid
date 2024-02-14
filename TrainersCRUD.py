def MainAsignarTrainers():
    import json
    def reindexar_IDs_entrenadores_secundarios(TrainersS):
        for i, trainer in enumerate(TrainersS, start=1):
            trainer['id'] = i
            
    with open('datos.json', 'r', encoding="utf8") as infile:
        mijson = json.load(infile)
    with open('Salones.json','r', encoding="utf8") as infile:
        mijson2 = json.load(infile)
    
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
                    
                    # Actualizar el archivo Salones.json con el nombre del profesor
                    with open('Salones.json', 'r', encoding="utf8") as infile:
                        salones_json = json.load(infile)
                    
                    if añadir == 1:
                        for salon_numero, salon_info in list(salones_json['Salones'].items())[:4]:
                            salones_json['Salones'][salon_numero]['Profesor'] = trainer['Nombre']
                    
                    elif añadir == 2:
                        for salon_numero, salon_info in list(salones_json['Salones'].items())[4:8]:
                            salones_json['Salones'][salon_numero]['Profesor'] = trainer['Nombre']
                    
                    elif añadir == 3:
                        for salon_numero, salon_info in list(salones_json['Salones'].items())[8:]:
                            salones_json['Salones'][salon_numero]['Profesor'] = trainer['Nombre']
                    
                    with open('Salones.json', 'w', encoding="utf8") as outfile:
                        json.dump(salones_json, outfile, indent=2)
                    
                    
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

