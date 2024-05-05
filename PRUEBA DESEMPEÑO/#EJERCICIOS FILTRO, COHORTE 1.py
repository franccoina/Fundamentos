'''
PERMISOS:                       SACAR NOTAS 3 VECES, (5 MINS)

Comprensión enunciado           15%
Calidad código                  15%
Cumplimiento de Requerimientos  15%
Comentarios y documentación     15%
Sustentación                    40%

EJERCICIOS:

A. Programa que permita al usuario ingresar info de productos comprador.                               HARD
Debe calcular el total de la factura, aplicar descuentos y mostrar un recibo
detallado de compra. Desc no acumulativos.

{prod:precio}

Tabla descuentos:   si 3 o mas productos, desc del 5%
                    si 5 o mas productos, desc del 10%
                    si 7 o mas prodcutos, bono redimible de 100.000
                    mas de 500.000, no IVA

B. Programa que permita al usuario ingresar y revisar, segun Salario mes, sus gastos                     MEDIUM
mensuales. Categorias de transporte, vivienda, entretenimiento y alimentación.
Saldo restante en salario - gastos. Se le pregunta al usuario. Todo pasa hasta que
lo ingresado sea 0.

Gastos adicionales. Que pueda crear categorias y gastos nuevos. Todo pasa hasta que
lo ingresado sea 0.

Tambien total gastos, y gastos por categoria.

C. Programa que permita al usuario ingresar su edad.                                                   EASY
'''

'''
#C
actual=int(input("Ingrese el año actual: "))
nacimiento=int(input("Ingrese el año de nacimiento: "))

def calculoEdad():
    edad=actual-nacimiento
    print(f"Su edad es {edad}")

persona = calculoEdad()
'''

#B

# gastosCategoria = {}

# def calculoGastosCategoria():
#   gastoViv = int(input("Agregue un gasto por la Categoria Vivienda:"))
#   gastosCategoria["Vivienda"]=gastoViv   
  
#   gastoAli = int(input("Agregue un gasto por la Categoria Alimentación:"))
#   gastosCategoria["Alimentacion"]=gastoAli

#   gastoEnt = int(input("Agregue un gasto por la Categoria Entretenimiento:"))
#   gastosCategoria["Entretenimiento"]=gastoEnt

#   gastoTra = int(input("Agregue un gasto por la Categoria Transporte:"))
#   gastosCategoria["Transporte"]=gastoTra
  
#   pregunta = str(input((f"Escribir 'add' para añadir nueva categoria. ENTER para omitir:")))
#   pregunta.lower()

#   while pregunta == "add":
#     added = str(input(f"Agregue su Categoria Nueva: "))
#     gastoAdded = int(input("Agregue un gasto por la Categoria Vivienda:"))
#     gastosCategoria.update({added:gastoAdded})

#     terminar = str(input((f"Escribir 'salir' para terminar la adicion. ENTER para agregar mas:")))
#     terminar.lower()
#     if terminar == "salir" or gastoAdded==0:
#       break

# def calculos():
#   salarioMes = int(input("Ingerese su salario:"))
#   gastosTotales = 0
#   for valor in gastosCategoria.values():
#     gastosTotales = gastosTotales + valor
#     saldo = salarioMes - gastosTotales
#   return (saldo, gastosTotales)

# def menu(saldoLocal,gastosTotalesLocal):
#   print(f'''
#   INFORMACION SALDO:
        
#   Tu saldo actual es de {saldoLocal}
#   Tu gasto total fue de {gastosTotalesLocal}''')
  
#   for clave,valor in gastosCategoria.items():
#     print(f'''  Tu gasto por categoria fue de {valor} para {clave}''')
  
#   return (saldoLocal,gastosTotalesLocal)

# calculoGastosCategoria()
# var1 = calculos()
# menu(var1[0],var1[1])

'''
'''

#A

'''
A. Programa que permita al usuario ingresar info de productos comprador.                               HARD
Debe calcular el total de la factura, aplicar descuentos y mostrar un recibo
detallado de compra. Desc no acumulativos.

{prod:precio}

Tabla descuentos:   si 3 o mas productos, desc del 5%
                    si 5 o mas productos, desc del 10%
                    si 7 o mas productos, bono redimible de 100.000
                    mas de 500.000, no IVA'''

precioProd = {"chocolate":2000,"paleta":1500,"mani":3000,
             "confite":300,"galleta":1000,"papitas":5000,
             "regaliz":500,"barrilete":500,"chicle":400}
carrito = {}
factura = {}
iva = 0.81
bono = 100000

def carritoCompra():
  print(f'''
  INGRESO DE PRODUCTOS:
        
  A continuación podrás ingresar cada producto comprado,
  con su respectiva cantidad. Si terminaste de ingresar
  valores, escribe 'salir' donde se indica.
  ''')
  
  for clave in precioProd.keys():
    producto = str(input("Escriba el nombre del producto comprado:"))
    producto.lower()
    
    while producto not in (precioProd.keys()):
      producto = str(input("EROR: Producto no existe. Escriba de nuevo el nombre del producto comprado:"))
      producto.lower()
    
    if producto in (precioProd.keys()):
      cant = int(input("Escriba la cantidad comprada del producto ingresado:"))
      carrito.update({producto:cant})
    
      salir = str(input("Si desea salir del ingreso de productos, escriba 'salir'"))
      salir.lower()
      if salir=="salir":
        break

  print(f'''
Su factura es la siguiente:        
''',carrito)
  return carrito

def descuentos():
  pagoTotal = 0
  for clave,valor in carrito.items():
    if carrito[clave]<3:
      pago = valor * precioProd[clave] 
      if pago<500000:
        pago *= iva
      factura[clave]={valor:pago}
      pagoTotal += pago
    
    if carrito[clave]>=3 and carrito[clave]<5:
      pago = valor * precioProd[clave] * 0.95
      if pago<500000:
        pago *= iva
      factura[clave]={valor:pago}
      pagoTotal += pago
    
    if carrito[clave]>=5 and carrito[clave]<7:
      pago = valor * precioProd[clave] * 0.9
      if pago<500000:
        pago *= iva
      factura[clave]={valor:pago}
      pagoTotal += pago
    
    if carrito[clave]>=7:
      pago = valor * precioProd[clave]
      if pago<500000:
        pago *= iva
      factura[clave]={valor:pago}
      pagoTotal += pago
      
      print(f"Por la compra de {clave}, el cliente ganó bono por {bono}")
  
    
  if pagoTotal>=100000:
    redim = str(input("Si desea redimir un bono, escribir 'redim'. Si no, escriba 'pass'"))
    if redim=='redim':
        pagoTotal-=bono
        print(f"Se aplico bono por {bono}")
    if redim=='pass':
        print(f"No se aplicó ningún bono")
  
    print(f'''
Su factura es la siguiente:        
''',factura,'''
El valor total de compra, menos el bono por''',bono,'''es de:''',pagoTotal)
  else:
    print(f'''
Su factura es la siguiente:        
''',factura,'''
El valor total de compra es de:''',pagoTotal)
  
  return factura

carritoCompra()
descuentos()
