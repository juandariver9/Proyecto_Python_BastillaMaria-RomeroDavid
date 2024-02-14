def c_y_p_asociados_ruta():
    import json
    with open('Salones.json', 'r', encoding="utf8") as file:
        mijson = json.load(file)
    listaasocidos = [camper for camper in mijson["Salones"]["1"] if camper["Ruta"] == "Java"]
    print("Por favor, presione Enter para mostrar Campers en estado inscrito")
    enter = input("")

    for camper in listaasocidos:
        for llave, valor in camper.items():
            print(f"{llave}: {valor}")
        print("-------------------------\n")

    with open('datos.json', 'w', encoding="utf8") as x:
        json.dump(mijson, x, indent=4)
