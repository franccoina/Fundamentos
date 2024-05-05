'''
Algoitmo que permita halla la distancia entre dos puntos
de un plano; con coordenadas en x y en y, las cuales,
seran ingresadas por el usuario. 
'''

class coord:
    def __init__(self,punt1,punt2,x1,x2,y1,y2):
        coord.punt1 = self
        coord.punt2 = self
        coord.funcionDistancia = self
        coord.x1 = self
        coord.x2 = self
        coord.y1 = self
        coord.y2 = self

    def instancia():
        coord.x1 = int(input("Escribir un valor para x1: "))
        coord.x2 = int(input("Escribir un valor para x2: "))
        coord.y1 = int(input("Escribir un valor para y1: "))
        coord.y2 = int(input("Escribir un valor para y2: "))

    def asigPunt():
        coord.punt1 = [coord.x1,coord.y1]
        coord.punt2 = [coord.x2,coord.y2]
        
    def distancia():
        coord.funcionDistancia = round(((coord.x2-coord.x1)**2 + (coord.y2-coord.y1)**2)**0.5)
    
    def impresion():
        print("La distancia entre los puntos",coord.punt1,"y",coord.punt2,"es de",coord.funcionDistancia,"unidades")

coord.instancia()
coord.asigPunt()
coord.distancia()
coord.impresion()