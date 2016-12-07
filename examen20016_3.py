#ESCUELA POLITECNICA NACIONAL
#Escuela de formacion de tecnologos

#### Examen 1 2016 -Grupo 3
#Integrantes: CAMPOVERDE VARGAS	JORGE	CRISTIAN
#             CENTENO	ROCHA	JOHANA	MISHEL
#             MAZA CAÑAR  JERSON  STALIN
#             PADILLA PERALVO	EDISON GEOVANNY
#             TIBANTA LEGÑA MARIA FERNANDA

from time import *

def creartxt():
    archi=open('busqueda.txt','w')
    archi.close
    

def grabartxt():
    archi=open('busqueda.txt','a')
    archi.write("Camila Jorge ")
    archi.write("Jorge Estefania Camila Jorge Maza")
    archi.write("Camila Jorge ")
    archi.write("Jorge Estefania Camila Jorge Maza")
    archi.write("Camila Jorge ")
    archi.write("Jorge Estefania Camila Jorge Maza")
    archi.write("Camila Jorge ")
    archi.write("Jorge Estefania Camila Jorge Maza")
creartxt()
grabartxt()

def leertxt():
    repetidas=0
    clave='Jorge'
    archi=open ('busqueda.txt','r')
    
    t_inicial=time()
                                              #Abre el archivo 
    linea=archi.readline()                    # lee la linea del archivo
    palabras=linea.split(' ')                 # separa la linea leida quitando los espacios
    cadena=len(palabras)                      #cadena es igualada al numero de palabras que fueron separadas en el comando anterior
    for i in range(cadena-1):                 # i en el rango de la cadena
        if palabras[i]==clave:                # evalua si la posicion de i de palabras es igual a la clave que es Harry
            repetidas=repetidas+1             #si encuentra la coinsidencia repetidas aumenta
    while linea != "":                        #repite todo lo mencionado antes hasta que no haya lineas
        linea=archi.readline()
        palabras=linea.split(' ')
        cadena=len(palabras)
        for i in range(cadena):
            if palabras[i]==clave:
                repetidas=repetidas+1
                
    t_final=time()
    resultado=t_final-t_inicial
    
    archi.close()
    
    archi=open('resultado.txt','a')          #Crea el archivo donde se almacena los resultados
    archi.write('Numero de palabras repetidas es :')
    archi.write(str(repetidas))
    archi.write("\t Tiempo transcurrido:")
    archi.write(str(resultado))

leertxt()
