def NotasFundamentosProgramacion():
    import json
    with open('CampAprob.json','r', encoding="utf8") as file:
        mijson = json.load(file)
    with open('Notas.json', 'r', encoding="utf8") as file:
        mijson2 = json.load(file)
    tel = int(input("Digite su num de telefono: "))
    ListaTelefono = mijson['Datos']['Aprobados']

    for i in ListaTelefono:
        if i['Telefono'] == tel:
            print(i['Nombre'])
            print(i['Apellido1'])
def NotasProgramacionWeb():
    import json
    with open('CampAprob.json','r', encoding="utf8") as file:
        mijson = json.load(file)
    with open('Notas.json', 'r', encoding="utf8") as file:
        mijson2 = json.load(file)
    tel = int(input("Digite su num de telefono: "))
    ListaTelefono = mijson['Datos']['Aprobados']

    for i in ListaTelefono:
        if i['Telefono'] == tel:
            print(i['Nombre'])
            print(i['Apellido1'])
def NotasProgramacionFormal():
    import json
    with open('CampAprob.json','r', encoding="utf8") as file:
        mijson = json.load(file)
    with open('Notas.json', 'r', encoding="utf8") as file:
        mijson2 = json.load(file)
    tel = int(input("Digite su num de telefono: "))
    ListaTelefono = mijson['Datos']['Aprobados']

    for i in ListaTelefono:
        if i['Telefono'] == tel:
            print(i['Nombre'])
            print(i['Apellido1'])
def NotasBasesDeDatos():
    import json
    with open('CampAprob.json','r', encoding="utf8") as file:
        mijson = json.load(file)
    with open('Notas.json', 'r', encoding="utf8") as file:
        mijson2 = json.load(file)
    tel = int(input("Digite su num de telefono: "))
    ListaTelefono = mijson['Datos']['Aprobados']

    for i in ListaTelefono:
        if i['Telefono'] == tel:
            print(i['Nombre'])
            print(i['Apellido1'])
def NotasBackend():
    import json
    with open('CampAprob.json','r', encoding="utf8") as file:
        mijson = json.load(file)
    with open('Notas.json', 'r', encoding="utf8") as file:
        mijson2 = json.load(file)
    tel = int(input("Digite su num de telefono: "))
    ListaTelefono = mijson['Datos']['Aprobados']

    for i in ListaTelefono:
        if i['Telefono'] == tel:
            print(i['Nombre'])
            print(i['Apellido1'])