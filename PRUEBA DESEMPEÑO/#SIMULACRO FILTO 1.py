#Programa para gestionar inventario en tienda. El usaurio debe poder
#agregar alimento. Actualizar cantidad existente de inventario. Eliminar
#alimentos de inventario. Listar todos los alimentos. 
# Verificar si alimento esta en inventario

#inventario debe tener nombre, precio unitario, cantidad

inventario = {}
bandera = True

def menu():
  while bandera: 
    comandos = ("add","update","del","list","search","end")
    correr = str(input("Escribir 'run' para iniciar el sistema de inventario:"))
    correr.lower()

    if correr!='run':
      print("No se ha iniciado el sistema. Vuelva a ejecutar")
      break

    while correr=='run':
      accion = str(input(f'''
SISTEMA DE INVENTARIO DE ALIMENTOS:
  
  1. Para agregar alimento, escriba 'add'
  2. Para actualizar la cantidad disponible de un alimento, escriba 'update'
  3. Para eliminar alimento del inventario, escriba 'del'
  4. Para conservar todos los elementos del inventario, escriba 'list'
  5. Para verificar si un alimento ya existe en inventario, escriba 'search'
  6. Para salir, escriba 'end'
    
Escribir que desea hacer:'''))
      accion.lower()
      
      while accion not in comandos:
        accion = str(input("ERROR: Comando no reconocido. Escribir de nuevo que desea hacer:"))
      accion.lower()

      if accion=='add':
        var1 = addAli()

      if accion=='update':
        updateAli(var1)
        
      if accion=='del':
        deleteAli()
        
      if accion=='list':
        listAli()
        
      if accion=='search':
        searchAli()
      
      if accion=='end':
        not bandera
        break
      
    return accion 

def addAli():
  while bandera:
    nombre = str(input("Escribir nombre del alimento para registrarlo al inventario:"))
    nombre.lower()
    
    precio = int(input("Escribir precio del alimento:"))
    cant = int(input("Escribir disponibilidad del alimento:"))
    inventario[nombre]={"precio":precio, "cantidad":cant}
    
    ask = str(input("Si desea parar de agregar, escriba 'stop':"))
    ask.lower()
    
    if ask=='stop':
      print(inventario)
      break
  return precio

def updateAli(precio):
  for clave,valor in inventario.items():
    nombreUp = input("Escribir nombre del alimento para actualizar disponibilidad:")
    nombreUp.lower()

    while nombreUp not in inventario.keys():
      nombreUp = input("ERROR: alimento no encontrado. Escribir de nuevo nombre del alimento a actualizar:")
      nombreUp.lower()
                
    if nombreUp in inventario:
      cantNew = int(input("Escribir disponibilidad actualizada del alimento para registrarlo al inventario:"))
      inventario[nombreUp]["cantidad"]=cantNew
        
      print(inventario)
      break
    break
  return inventario

def deleteAli():
  nomDel = str(input("Escribir nombre del alimento que desea eliminar de inventario:"))
  if nomDel in inventario.keys():
    inventario.pop(nomDel)
  print(f"El nuevo inventario es el siguiente:",inventario)
  return inventario

def listAli():
  print(f'INVENTARIO DE ALIMENTOS:')
  for clave,valor in inventario.items():
    print(f'ALIMENTO:',clave,', INFO',valor)
  return inventario

def searchAli():
  nomSearch = str(input("Escribir nombre del alimento que desea buscar en inventario:"))
  if nomSearch in inventario.keys():
    print(f'''Si existe. El ALIMENTO solicitado es:
ALIMENTO:''',nomSearch,'''INFO:''',inventario.get(nomSearch))
  else:
    print("El alimento que ha escrito no existe")
  return inventario

menu()

