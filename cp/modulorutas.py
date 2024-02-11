

def Rutas():
    import json
    x = open("Rutas.json", 'r')
    mijson = json.load(x)

    listarutas = {}
    print("Por favor defina la cantidad de nuevas rutas que desea agregar")
    cantidad = int(input(""))

    for i in range(cantidad):
        Nombre = input("Digite el nombre de la nueva ruta: ")
        trainer = ("No definido")
        ruta = ("No definido")
        salones = ("No definido ")

        nueva_ruta = {
            "Nombre": Nombre,
            "Trainer_principal": trainer,
            "Ruta": ruta,
            "Salones": salones
        }

        mijson["Rutas"]["Rutas_nuevas"].append(nueva_ruta)

    with open("Rutas.json", 'w') as json_file:
        json.dump(mijson, json_file, indent=2)

Rutas()




