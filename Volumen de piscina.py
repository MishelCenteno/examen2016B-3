print ("VOLUMEN DE UNA PISCINA")

def pis_rect():
    print ("Volumen de una piscina rectangular")
    a=float(input("Ingrese el valor la altura: "))
    b=float(input("Ingrese el valor del largo de la piscina: "))
    c=float(input("Ingrese el valor del ancho de la piscina: "))
    volumenR=a*b*c
    print("Volumen de la priscina en forma de prisma rectangular es: ", volumenR)


def pis_elip():
    print ("Volumen de una piscina eliptica")
    a=float(input("Ingrese el valor del radio1: "))
    b=float(input("Ingrese el valor del redio2: "))
    c=float(input("Ingrese el valor del radio3: "))
    pi=3.14
    volumenE=4/3*pi*a*b*c
    print("Volumen de la piscina elipsoide es: ", volumenE)


def pis_cir():
    print ("Volumen de una piscina cilindrica")
    r=float(input("Ingrese el valor del radio: "))
    h=float(input("Ingrese el valor de la altura: "))
    pi=3.14
    volumenC=pi*r**2*h
    print("Volumen de una piscina eliptica es: ", volumenC)
    

pis_rect()
pis_elip()
pis_cir()
