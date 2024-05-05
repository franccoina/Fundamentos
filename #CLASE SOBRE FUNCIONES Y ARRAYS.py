#CLASE SOBRE FUNCIONES Y ARRAYS

'''

lista = [1,2,3,4]

#variable en forma de LISTA, siempre entre corchetes estan sus elementos. Desde el 0

lista.append(9)

#agrego el valor dentro del parentesis en la ultima posicion

del lista[0]

#elimino el valor en la posicion dentro de los corchetes

lista.remove(2)

#elimino el primer valor que sea igual al puesto en el parentesis

lista[1]=9

#asi reemplazo un valor en la posicion dentro del corchete, con otro valor
#definido despues del igual

len(lista)

#la longitud de la lista, es decir, numero de elementos

x = sorted(lista)

#asi organizo alfabeticamente/numericamente una lista

'''

'''
#Calcular el promedio de una lista de calificaciones total

calificaciones = [2,3,5,1,3,2,4,2]
len = float(len(calificaciones))
prom = float(sum(calificaciones)/len)
print("El promedio de las calificaciones",calificaciones,"es:",prom)

#Calcular el numero mas grande

numeros = [12,58,89,90]
max = max(numeros)
print("El numero mas grande es:",max)

#...otra forma

numeros = [12,58,89,90]
max = numeros[0]
for i in numeros:
  if i > max:
    max = i
print("El  numero mas grande es:",max)
'''

'''
duplicados = [1,1,4,4,5,5,7,8,99,43,23,12,43]
normal = []

duplicados = set(duplicados)
normal = list(duplicados)

print(normal)

'''

'''
#

lista1 = [1,2,3,4,5,3]
lista2 = ["2","3","4","5"]

len1 = len(lista1)
len2 = len(lista2)

if len1 > len2:
  print("La menor es la de",lista2,"pues es igual a:",len2)
else:
  print("La menor es la de",lista1,"pues es igual a:",len1)
  
'''

'''
#Mostra info de libros en biblioteca, ordenadas por titulo, autor y año

class libro:
  def __init__(self,titulo,autor,año):
    self.titulo=titulo
    self.auto=autor
    self.año=año

  def infoLibro(self):
    print(self.titulo,self.autor,self.año)

bio1 = libro("Python for Data Science","Jake VanderPlas",2015)
bio2 = libro("Deep Learning","Ian Goodfellow",2016)
bio3 = libro("The elements of Statistical Learning","Trevor Hastle",2009)

bio1.infoLibro()
bio2.infoLibro()


#Forma diferente

bio1 = ("Python for Data Science","Deep Learning","The elements of Statistical Learning")
bio2 = ("Jake VanderPlas","Ian Goodfellow","Trevor Hastle")
bio3 = (2015,2016,2009)

print("Titulo:",bio1[0],"Autor",bio2[0],"Año",bio3[0])
print("Titulo:",bio1[1],"Autor",bio2[1],"Año",bio3[1])
print("Titulo:",bio1[2],"Autor",bio2[2],"Año",bio3[2])

'''

'''

cadenas = ["Naranja","Pera","Kiwi"]
cadOrdenada1 = []

cadOrdenada1 = sorted(cadenas)

print(cadOrdenada1)

'''