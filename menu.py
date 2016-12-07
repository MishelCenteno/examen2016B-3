def menu():
    opcion=0;
    while(opcion!=4):
        print("Menu del programa")
        print("1. Scrip")
        print("2.Contabilizar las repeticiones ")
        print("3.Calcular el volumen de una piscina ")
        print("4.Salir")
        opcion=int(input("Ingrese la opcion que desea elegir:"))
        if (opcion==1):
            print("generar un scrip")
        if (opcion==2):
            print("ocurrencias")
        if (opcion==3):
            print("el volumen ")
            menu_piscina()
        if (opcion==4):
            print ("Adios")      

def menu_piscina():
    opcion=0;
    while(opcion!=4):
        print("Calcular el volumen de una piscina")
        print("1.Volumen de forma rectangular")
        print("2.3Volumen de forma eliptica")
        print("3.volumen de forma cilindrica")
        opcion=int(input("Selecione: "))
        if (opcion==1):
            print("Volumen de forma rectangular")
        if (opcion==2):
            print("Volumen de froma eliptica")
        if (opcion==3):
            print("Volumen  de forma cilindrica")
        if (opcion==4):
            print ("Adios")

menu()



