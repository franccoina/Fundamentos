#Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente
#todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería devolver 10
#y multip([1,2,3,4]) debería devolver 24

#EJEMPLO 1
'''

class operacion:
  def __init__(self,arreglo1,arreglo2,prod,sum,x1,y1,z1,w1,x2, y2,z2,w2):
    self.arreglo1=arreglo1
    self.arreglo2=arreglo2
    self.prod=prod
    self.sum=sum
    self.x1=x1
    self.x2=x2
    self.y1=y1
    self.y2=y2
    self.z1=z1
    self.z2=z2
    self.w1=w1
    self.w2=w2

  def defArreglo1(self):
    print("Ingresa los valores de tu Arreglo 1")
    self.arreglo1=[]
    n=1
    for self.x1 in range(n):
      self.x1=int(input("Valor 1: "))
      self.arreglo1.append(self.x1)
    for self.y1 in range(n):
      self.y1=int(input("Valor 2: "))
      self.arreglo1.append(self.y1)
    for self.z1 in range(n):
      self.z1=int(input("Valor 3: "))
      self.arreglo1.append(self.z1)
    for self.w1 in range(n):
      self.w1=int(input("Valor 4: "))
      self.arreglo1.append(self.w1)
  
  def defArreglo2(self):
    print("Ingresa los valores de tu Arreglo 2")
    self.arreglo2=[]
    n=1
    for self.x2 in range(n):
      self.x2=int(input("Valor 1: "))
      self.arreglo2.append(self.x2)
    for self.y2 in range(n):
      self.y2=int(input("Valor 2: "))
      self.arreglo2.append(self.y2)
    for self.z2 in range(n):
      self.z2=int(input("Valor 3: "))
      self.arreglo2.append(self.z2)
    for self.w2 in range(n):
      self.w2=int(input("Valor 4: "))
      self.arreglo2.append(self.w2)

  def opSuma(self):
    self.sum = sum(self.arreglo1)
    print("La suma de los valores del arreglo",self.arreglo1,"es :",self.sum)
    
  def opProd(self):
    self.prod = int((self.x2)*(self.y2)*(self.z2)*(self.w2))
    print("El producto de los valores del arreglo",self.arreglo2,"es :",self.prod)

ej = operacion
ej.defArreglo1()
ej.defArreglo2()
ej.opSuma()
ej.opProd()

'''
#EJEMPLO2

'''

class operacion:
  def __init__(self, arreglo1, arreglo2, prod, sum, x1, y1, z1, w1, x2, y2,z2,w2):
    self.arreglo1=arreglo1
    self.arreglo2=arreglo2
    self.prod=prod
    self.sum=sum
    self.x1=x1
    self.x2=x2
    self.y1=y1
    self.y2=y2
    self.z1=z1
    self.z2=z2
    self.w1=w1
    self.w2=w2

  def defArreglo1(self):
    print("Ingresa los valores de tu Arreglo 1")
    
    self.x1=int(input("Valor 1: "))
    self.y1=int(input("Valor 2: "))
    self.z1=int(input("Valor 3: "))
    self.w1=int(input("Valor 4: "))
    
    self.arreglo1 = [self.x1,self.y1,self.z1,self.w1]
  
  def defArreglo2(self):
    print("Ingresa los valores de tu Arreglo 2")
    
    self.x2=int(input("Valor 1: "))
    self.y2=int(input("Valor 2: "))
    self.z2=int(input("Valor 3: "))
    self.w2=int(input("Valor 4: "))
    
    self.arreglo2 = [self.x2,self.y2,self.z2,self.w2]

  def opSuma(self):
    self.sum = sum(self.arreglo1)
    print("La suma de los valores del arreglo",self.arreglo1,"es :",self.sum)
    
  def opProd(self):
    self.prod = int(self.x2*self.y2*self.z2*self.w2)
    print("El producto de los valores del arreglo",self.arreglo2,"es :",self.prod)

ej = operacion
ej.defArreglo1()
ej.defArreglo2()
ej.opSuma()
ej.opProd()

'''
#EJEMPLO3

'''

class operacion:
  def __init__(self, arreglo1, arreglo2, prod, sum):
    self.arreglo1=arreglo1
    self.arreglo2=arreglo2
    self.prod=prod
    self.sum=sum
  
  def defArreglo1(self):
    print("Ingresa los valores de tu Arreglo 1")
    self.arreglo1 = []
    
    self.arreglo1.append(int(input("Valor 1: ")))
    self.arreglo1.append(int(input("Valor 2: ")))
    self.arreglo1.append(int(input("Valor 3: ")))
    self.arreglo1.append(int(input("Valor 4: ")))
  
  def defArreglo2(self):
    print("Ingresa los valores de tu Arreglo 2")
    
    self.arreglo2 = []
    
    self.arreglo2.append(int(input("Valor 1: ")))
    self.arreglo2.append(int(input("Valor 2: ")))
    self.arreglo2.append(int(input("Valor 3: ")))
    self.arreglo2.append(int(input("Valor 4: ")))

  def opSuma(self):
    self.sum = sum(self.arreglo1)
    print("La suma de los valores del arreglo",self.arreglo1,"es :",self.sum)
    
  def opProd(self):
    self.prod = int(self.arreglo2[0]*self.arreglo2[1]*self.arreglo2[2]*self.arreglo2[3])
    print("El producto de los valores del arreglo",self.arreglo2,"es :",self.prod)

ej = operacion
ej.defArreglo1()
ej.defArreglo2()
ej.opSuma()
ej.opProd()

'''

