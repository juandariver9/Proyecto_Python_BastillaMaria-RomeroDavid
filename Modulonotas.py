# Modulo para agregar notas 
def fundamentosprogramacion():
    def notafinal ():
       notapruebas= pruebapractica*0.6 + pruebateorica*0.3
       notatalleres= (totalquizes+totaltrabajos)*0.1
       notafinal= notapruebas+notatalleres
       return notafinal

       
    from ModuloReportes import ListaAprobaronExamen
    print ("Por favor escriba el id del estudiante a actualizar")
    idestudiante=int(input("---->"))
    for i in ListaAprobaronExamen["id"]:
        if idestudiante== ListaAprobaronExamen["id"]:
            print("Digite nota prueba teorica")
            pruebateorica=int(input("--->"))
            print("Digite nota de prueba practica ")
            pruebapractica=int(input("--->"))
            print("Digite la cantidad de quizes hechos durante el modulo")
            quizes=int(input("--->"))
            sumatotal=0
            for i in range (quizes):
             notas=int(input("Digite nota quiz #" (i)))
             sumatotal= sumatotal+notas
             totalquizes= sumatotal/quizes
                       
            print("Digite la antidad de Trabajos hechos durante el modulo")
            Trabajos=int(input("--->"))
            sumatotaltrabajos=0
            for i in range (Trabajos):
             notas=int(input("Digite nota Trabajo #" (i)))
             sumatotaltrabajos= sumatotaltrabajos+notas
             totaltrabajos=sumatotaltrabajos/Trabajos
    return notafinal
                       


    notafinal()
        



