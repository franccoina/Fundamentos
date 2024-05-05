'''
class autor:
    def __init__(self,nombre,nacion,obra):
        autor.nombre = self
        autor.nacion = self
        autor.obra = self
        
    def instancia(self):
        autor.nombre = "Homero"
        autor.nacion = "griega"
        autor.obra = "La Iliada"
    
    def bio(self):
        print("Nombre del autor:",autor.nombre)
        print("Nacionalidad:",autor.nacion)
        print("Obra:",autor.obra)
        
        print(autor.nombre,"de nacionalidad",autor.nacion,"es autor del libro",autor.obra)
      
bio1 = autor("Homero","griega","La Iliada")
bio1.instancia()
bio1.bio()
'''

'''
class autor:
    def __init__(self,nombre,nacion,obra):
        autor.nombre = nombre
        autor.nacion = nacion
        autor.obra = obra
    
    def bio(self):
        print("Nombre del autor:",autor.nombre)
        print("Nacionalidad:",autor.nacion)
        print("Obra:",autor.obra)
        
        print(autor.nombre,"de nacionalidad",autor.nacion,"es autor del libro",autor.obra)
        
bio1 = autor("Homero","griega","La Iliada")
bio1.bio()
'''

class autor:
    def __init__(self,nombre,nacion,obra):
        autor.nombre = nombre
        autor.nacion = nacion
        autor.obra = obra

    def bio(self):
        print("Nombre del autor:",autor.nombre)
        print("Nacionalidad:",autor.nacion)
        print("Obra:",autor.obra)
        
        print("RESUMEN:",autor.nombre,", de nacionalidad",autor.nacion,", es autor del libro",autor.obra)
    
print("A continuacion se muestra una breve biografía del autor: ")
bio1 = autor("Homero","griega","La Iliada")
bio1.bio()

#En conclusión, usaremos la denominacion class.atributoVariable para cuando necesitemos heredar
#información de una clase base, hacia una subclase. Cuando solo tenemos una clase para realizar
#un proceso no se hace necesario. Es mas corto y rapido usar la denominacion self.atributoVariable.
#A continuación, un ejemplo con el caso anterior.

class venta(autor):
    def __init__(self,precio,comprador):
        super().__init__(autor.nombre,autor.nacion,autor.obra)
        self.precio = precio
        self.comprador = comprador
        
    def infoVenta(self):
        print("Nombre del comprador:",self.comprador)
        print("Precio:",self.precio,"USD")
        print("Obra:",self.obra)
        
        print(self.comprador,"pagó",self.precio,"USD por el libro",autor.obra,", del autor",autor.nombre)

print("A continuacion se muestra la información de la venta del libro realizada: ")
venta1 = venta(4,"José Álvarez")
venta1.infoVenta()
    