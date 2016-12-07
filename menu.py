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
        if (opcion==4):
            print ("Adios")      
menu()

