import json
def inscripciones ():
    x = open ('inscritos.json')
    mijson= json.load(x)

    id_inscripciones= max([inscripciones["id"]for inscripciones in mijson ['datos']['inscripciones']]) if mijson ['datos']['inscripciones'] else 0

    estado="Inscrito"
    nuevo_id=id_inscripciones +1

    nueva_inscripcion= {}
    nueva_inscripcion['id']= nuevo_id
    nueva_inscripcion['identidad']= int(input("Escriba el numero de identificacion " ))
    nueva_inscripcion['Nombre']= input("Escriba el nombre " )
    nueva_inscripcion['Apellido1']= input("Escriba el apellido 1 " )
    nueva_inscripcion['Apellido2']= input("Escriba el apellido 2 " )
    nueva_inscripcion['Direccion']= input("Escriba la direccion " )
    nueva_inscripcion['Acudiente']=input ("Escriba el nombre de su acudiente(opcional) " )
    nueva_inscripcion['Celular']=int(input ("Escriba el numero de celular " ))
    nueva_inscripcion['Telefono']=int(input ("Escriba el numero de telefono " ))
    nueva_inscripcion['Estado']= estado

    mijson['datos']['inscripciones'].append(nueva_inscripcion)
    with open('inscritos.json', 'w') as file:
        json.dump(mijson, file, indent=2)
inscripciones()