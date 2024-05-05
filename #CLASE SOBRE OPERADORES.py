'''
#                                Ejemplos sobre operadores:
#                                   Aritmeticos

num1= int(input("Inserte un numero para realizar la suma: "))
num2 = int(input("Inserte un numero para realizar la suma: "))

suma = num1 + num2

#                                   Logicos

print(suma)

comp = num1 <= num2

print(comp)

#                                   Mixtos

numRest = int(input("Inserte un numero para realizar la resta: "))
numRest -= 10

#                                   Condicionales

op1= int(input("Inserte un numero para realizar la suma: "))
op2 = int(input("Inserte un numero para realizar la suma: "))

op1 = num1 / num2
op2 = num1 % num2

if op1 == op2 and comp == False:
    print("Son iguales, y num1 es es menor o igual a num2")
else:
    print("Sog, mire a ver que no se cumple")
'''

#                                Ejercicios sobre operadores:
#                                   A. Programa que verifique
#                                   si edad esta entre 18 y 65
#                                   años. Si si, que diga elegible,
#                                   si no, que diga que no lo es.

age = int(input("Por favor ingrese su edad en años: "))

if (age >= 18 and age <= 65):
    print("Usted es elegible")
else:
    print("Usted no es elegible")

#                                   B. Simular un sistema de
#                                   autenticacion simple.
#                                   Que pida usuario y contraseña.
#                                   Si melo, sigue, si no, error


user = str(input("Por favor ingrese su usuario: "))
password = str(input("Por favor ingrese su contraseña: "))

setUser = str("Josecarlos") or str("josecarlos") 
setPassword = str("Jose23.")

if (user == setUser and password == setPassword):
    print("Acceso permitido. Bienvenido")
else:
    print("Eror: Usuario o contraseña incorrecta. Intente de nuevo")

#                                   C.
#                                   
#                                   
#                                   



#                                   D. 
#                                   
#                                   
#                                   





