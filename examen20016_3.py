#ESCUELA POLITECNICA NACIONAL
#Escuela de formacion de tecnologos

#### Examen 1 2016 -Grupo 3
#Integrantes: CAMPOVERDE VARGAS	JORGE	CRISTIAN
#             CENTENO	ROCHA	JOHANA	MISHEL
#             MAZA CAÑAR  JERSON  STALIN
#             PADILLA PERALVO	EDISON GEOVANNY
#             TIBANTA LEGÑA MARIA FERNANDA

from time import *

def leertxt():
    repetidas=0
    clave='JORGE'
    archi=open ('nombres2.txt','r')
    
    t_inicial=time()
                                              #Abre el archivo 
    linea=archi.readline()                    # lee la linea del archivo
    palabras=linea.split(' ')                 # separa la linea leida quitando los espacios
    cadena=len(palabras)                      
    for i in range(cadena-1):                 # i en el rango de la cadena
        if palabras[i]==clave:                # evalua si la posicion de i de palabras es igual a la clave 
            repetidas=repetidas+1             #si encuentra la coinsidencia repetidas aumenta
    while linea != "":                        
        linea=archi.readline()
        palabras=linea.split(' ')
        cadena=len(palabras)
        for i in range(cadena):
            if palabras[i]==clave:
                repetidas=repetidas+1
                
    t_final=time()
    resultado=t_final-t_inicial
    
    archi.close()

    archi=open('resultado.txt','a')         
    archi.write('')
    archi=open('resultado.txt','a')          #Crea el archivo donde se almacena los resultados
    archi.write('Numero de palabras repetidas es :')
    archi.write(str(repetidas))
    archi.write("\t Tiempo transcurrido:")
    archi.write(str(resultado))

leertxt()
