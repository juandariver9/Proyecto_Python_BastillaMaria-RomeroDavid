import json

print("**************************************************")
print("*                HORARIO TRAINERS                *")
print("**************************************************")

with open('datos.json', 'r', encoding="utf8") as file:
    mijson = json.load(file)

y = int(input("Digite el ID del profesor: "))
lista_trainers = mijson['Datos']['Trainer_Principales']

for trainer in lista_trainers:
    if y == trainer['id']:
        horario = trainer['Horario']
        Nombre = trainer['Nombre']
        print(f"El horario del profesor {Nombre} es: ")

        
        for clase, materia in horario.items():
            print(f"- Tienes clase con el grupo {clase} en el salón {materia}")
