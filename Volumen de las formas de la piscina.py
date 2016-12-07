print ("VOLUMEN DE UNA PISCINA")
import math

def menu_vol():
    opcion=0
    while (opcion!=4):
        print ("\n")
        print("Calcular el volumen de una piscina")
        print("1.Volumen de forma rectangular")
        print("2.Volumen de forma eliptica")
        print("3.volumen de forma cilindrica")
        print ("\n")
        opcion= int (input("Ingrese la opcion que desea: "))
        if opcion == 1:
            print ("Volumen de una piscina rectangular")
            a=float(input("Ingrese el valor de la altura: "))
            b=float(input("Ingrese el valor del largo de la piscina: "))
            c=float(input("Ingrese el valor del ancho de la piscina: "))
            volumenR=a*b*c
            print("Volumen de la piscina de forma rectangular es: ", volumenR)


        if opcion == 2:
            print ("Volumen de una piscina eliptica")
            a=float(input("Ingrese el valor del eje mayor: "))
            b=float(input("Ingrese el valor del eje menor: "))
            c=float(input("Ingrese el valor de la altura: "))
            volumenE=math.pi*((a/2)*(b/2)*c)
            print("Volumen de la piscina de forma eliptica es: ", volumenE)


        if opcion == 3:
            print ("Volumen de una piscina cilindrica")
            r=float(input("Ingrese el valor del radio: "))
            h=float(input("Ingrese el valor de la altura: "))
            volumenC=math.pi*r**2*h
            print("Volumen de una piscina de forma circular es: ", volumenC)


menu_vol()
