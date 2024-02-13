def HorarioTrainers():
    import json

    def convertir_horario(clase):
        if clase == "Clase1":
            return "6 a 9:30 AM"
        elif clase == "Clase2":
            return "10 AM a 2 PM"
        elif clase == "Clase3":
            return "2 a 5:30 PM"
        elif clase == "Clase4":
            return "6 a 10 PM"
        else:
            return "Horario no definido"
        
    print("**************************************************")
    print("*                HORARIO TRAINERS                *")
    print("**************************************************\n")

    with open('datos.json', 'r', encoding="utf8") as file:
        mijson = json.load(file)

    y = int(input("Digite el ID del profesor: "))
    print("")
    lista_trainers = mijson['Datos']['Trainer_Principales']

    profesor_encontrado = False

    for trainer in lista_trainers:
        if y == trainer['id']:
            profesor_encontrado = True
            horario = trainer['Horario'] 
            Nombre = trainer['Nombre']
            
            if not Nombre.strip():
                print("No hay ningún profesor en este puesto.")
                break
            
            print(f"\nHola profesor {Nombre}! Tu horario es: ")
            
            for clase, nombre_clase in horario.items():
                horario_convertido = convertir_horario(clase)
                print(f"{horario_convertido}: \t {nombre_clase}")
            break

    if not profesor_encontrado:
        print("No se encontró ningún profesor con horario en el ID proporcionado.")
    x = input("\nPresiona cualquier tecla para continuar")