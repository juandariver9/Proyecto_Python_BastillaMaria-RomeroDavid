
def MainTrainersAñadir():
    import json
    with open('datos.json', 'r', encoding="utf8") as file:
        mijson = json.load(file)
    nuevo_id = max([inscripcion["id"] for inscripcion in mijson['Datos']['Trainer']], default=0) + 1
    nueva_inscripcion = {}
    nueva_inscripcion['id'] = nuevo_id
    nueva_inscripcion['Identificacion'] = int(input("Escriba el número de identificación: "))
    nueva_inscripcion['Nombre'] = str(input("Escriba el nombre: "))
    nueva_inscripcion['Apellido1'] = input("Escriba el apellido 1: ")
    nueva_inscripcion['Celular'] = int(input("Escriba el número de celular: "))
    nueva_inscripcion['Telefono'] = int(input("Escriba el número de teléfono: "))
    
    mijson['Datos']['Trainer'].append(nueva_inscripcion)
    
    with open('datos.json', 'w', encoding="utf8") as file:
        json.dump(mijson, file, indent=2)

def MainTrainersEliminar():
    def eliminar_entrenador(identificacion):
        import json
        with open('datos.json', 'r', encoding="utf8") as file:
            mijson = json.load(file)
        
        entrenadores = mijson['Datos']['Trainer']
        indice_a_eliminar = None
        
        for i, entrenador in enumerate(entrenadores):
            if entrenador['Identificacion'] == identificacion:
                indice_a_eliminar = i
                break
        
        if indice_a_eliminar is not None:
            del mijson['Datos']['Trainer'][indice_a_eliminar]
            
            with open('datos.json', 'w', encoding="utf8") as file:
                json.dump(mijson, file, indent=2)
            print("Entrenador eliminado exitosamente.")
        else:
            print("No se encontró ningún entrenador con la identificación proporcionada.")
    identificacion_a_eliminar = int(input("Ingrese el número de identificación del entrenador a eliminar: "))
    eliminar_entrenador(identificacion_a_eliminar)


