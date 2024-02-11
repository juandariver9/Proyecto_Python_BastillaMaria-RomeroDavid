import json

def MainTrainersAñadir():
    with open('datos.json', 'r', encoding="utf8") as file:
        mijson = json.load(file)
    
    def mainTrainer():
        nuevo_id = max([inscripcion["id"] for inscripcion in mijson['Datos']['inscripciones']], default=0) + 1
        
        nueva_inscripcion = {}
        nueva_inscripcion['id'] = nuevo_id
        nueva_inscripcion['Identificacion'] = int(input("Escriba el número de identificación: "))
        nueva_inscripcion['Nombre'] = str(input("Escriba el nombre: "))
        nueva_inscripcion['Apellido1'] = input("Escriba el apellido 1: ")
        nueva_inscripcion['Celular'] = int(input("Escriba el número de celular: "))
        nueva_inscripcion['Telefono'] = int(input("Escriba el número de teléfono: "))
        
        mijson['datos']['Trainers'].append(nueva_inscripcion)
        
        with open('datos.json', 'w', encoding="utf8") as file:
            json.dump(mijson, file, indent=2)
    mainTrainer()