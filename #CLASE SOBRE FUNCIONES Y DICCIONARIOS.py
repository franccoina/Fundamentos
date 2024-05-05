                                                        #CLASE SOBRE FUNCIONES Y DICCIONARIOS:

                                                        #FUNCIONES GNRALES: 
#INTRO
'''
def coso(blah,blunt):
    pass    #se usa para Logica de codigo, medida de referencia. No para operar.
            #Omite si no hay codigo.para que pase...

#EJERCICIOS:

#A
def sumeNums(a,b):
    suma = a + b
    return suma

resultado1 = sumeNums(3,4)
print(f'La suma es {resultado1}')

#B
def promLista(lista):
    suma = sum(lista)
    length = len(lista)
    prom = float(suma/length)
    return prom

lista = [1,2,3,4]
resultado2 = promLista(lista)
print(f'Promedio es: {resultado2}')

#C
def palindromo(cadena):
    cadena = cadena.lower().replace(" ","")     #replace() reemplaza algo con otra cosa
                                                #y lower() es para convertir a minusculas
    return cadena == cadena[::-1]                            # comparamos la cadena original con su reverso (cadena invertida):
                                                        # NOTA: Al aplicar : primero me pone el rango o posición(vacio es que es tod), y el
                                                        # segundo : me indica lo que va a pasar con ese rango. En este caso un -1, dice
                                                        # que vamos de atras hacia adelante (la inversa)

palabra = "reconocer"
resultado3 = palindromo(palabra)
if resultado3:
    print("si lo es")
else:
    print("no lo es")

#D
def invertirLista(lista):
    return lista[::-1]

lista = [1,2,3,4]
listaInvertida = invertirLista(lista)
print(f'la lista invertida es {listaInvertida}')

#E
def contarPalabras(cadena):
    palabras = cadena.split()                           #uso split() para cortar la cadena por palabras
    cantPalabras = len(palabras)
    return cantPalabras

cad1 = "Cosaco"
cuenta = contarPalabras(cad1)
print(f'Tu cadena tiene {cuenta} palabras')

#F
def contarLetras(texto):
    contador = 0
    for i in texto:
        texto.count(i)                                  #count() es para contar lo que haya en un caracter
        if i in texto:
            contador += 1
        else:
            break                                       #break es para forzar salida de algun proceso
    return contador

contador = contarLetras("Manzana")
print(f'en el texto hay {contador} caracteres')

#PROBLEMA 1: Funcion doc por supuesto crear input que pida la info

def ingresoData():
    doc1 = []
    titulo = doc1.append(input("Escribir nombre del documento:"))
    escritor = doc1.append(input("Escribir escritor del documento:"))
    año = doc1.append(input("Escribir año de redacción del documento:"))
    return doc1

def listadoDocs():
    listDocs = []
    listDocs.append(input("Escribir nombre del listado de su documento:"))
    return listDocs

def correspondencia():
    correspondencias = [listDocs,doc1]
    return correspondencias

doc1 = ingresoData()
listDocs = listadoDocs()
print(f'Nuestro documento {doc1} pertenece a la lista {listDocs}')
correspondencias = correspondencia()
print(f'Nuestro documento esta ubicado en las coordenadas {correspondencias}')


                                                        #DICCIONARIOS:
#INTRO

diccionario = {"yo":3,"el":2,"ella":1,"eso":0}
print(diccionario["yo"])

diccionario["el"] = 4
print(diccionario["el"])

#FUNCIONES BASICAS:

#dict.items(), trabajamos con las pares clave-valor. Devuelve todos
#dict.values(), trabajamos con los valores del diccionarios, sobre todo para iterarlos. Devuelve todos
#dict.keys(), trabajamos con las claves. Devuelve todos
#dict.clear(), elimina todos los elementos del diccionario
#len(dict),  nos da el tamaño del diccionario

for valor,clave in diccionario.items():
    print(f'{clave}:{valor}')
for valor in diccionario.values():
    print(valor)
for clave in diccionario.keys():
    print(clave)

'''

#NECESITAMOS QUE DESDE UN DICCIONARIO A, LLEGUEMOS A UN DICCIONARIO B,
#DONDE LOS VALORES SEAN LA SUMA DEL ARREGLO DENTRO DE LOS VALORES
#DE MI DICCIONARIO A

#solucion

diccionarioA = {"uno":[1,2,3],"dos":[2,3,4],"tres":[3,4,5]}

def sumaValores():
    for clave,valor in diccionarioA.items():
        sumValor = sum(valor)
        diccionarioB = {clave:sumValor}
        for clave in diccionarioB:
            print(f'Si el valor de {clave} de mi diccionario A es {valor}, entonces, al sumarlos entre si, obtenemos el diccionario {diccionarioB}')
    return diccionarioB

diccionarioB = sumaValores()

#mas resumido

diccionarioA = {"uno":[1,2,3],"dos":[2,3,4],"tres":[3,4,5]}

def sumaValores():
    for clave,valor in diccionarioA.items():
      sumValor = sum(valor)
      diccionarioB = {clave:sumValor}
      impresion = print(f'Si el valor de {clave} de mi diccionario A es {valor}, entonces, al sumarlos entre si, obtenemos el diccionario {diccionarioB}')
    return impresion

diccionarioB = sumaValores()

    


    

    
