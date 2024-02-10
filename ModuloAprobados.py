
def pruebainical (): 
    import json
    x = open ('inscritos.json')
    mijson= json.load(x)
    x1 = open ('aprobados.json')
    mijson2= json.load(x1)
    listainscritos=mijson['datos']['inscripciones']
    estado="Aprobado"


    aprobado={}
    y=int(input("Escriba el id del estudiante a actualizar "))
    for i  in listainscritos :
        if i['id']==y:
            notapractica=int(input("Digite la nota de la prueba practica"))
            notateorica=int(input("Digite la nota de la prueba teorica"))
            notafinal=(notapractica+notateorica)/2
            if notafinal>=60:
                aprobado["Nombre"]=i['Nombre']
                aprobado["Apellido1"]=i['Apellido1']
                aprobado["Apellido2"]=i['Apellido2']
                aprobado["Direccion"]=i['Direccion']
                aprobado["Nombre Acudiente"]=i['Acudiente']
                aprobado["Celular"]=i['Celular']
                aprobado["Telefono"]=i['Telefono']
                aprobado["Estado"]= estado
                aprobado["Fecha de inicio"]=input("Escriba la fecha de inicio del estudiante")
                aprobado["Fecha de finalizacion"]=input("Escriba la fecha de finalizacion")

                mijson2['Datos']['Matriculados'].append(aprobado)
                with open('aprobados.json', 'w') as file:
                 json.dump(mijson2, file, indent=2)

pruebainical()