#------------------------- PUNTO 1 -------------------------------

# class ReproductorMusica:
#     def __init__(self,volumen=0) -> None:
#         self.volumen=volumen
        
#     def obtener_volumen(self):
#         print(f"El volumen actual es {self.volumen} \n")
    
#     def aplicar_volumen(self,nuevo_volumen):
#         if nuevo_volumen>0 and nuevo_volumen<100:
#             self.volumen = nuevo_volumen
#             print(f'''El volumen fue ajustado correctamente a: {self.volumen}''')
#         elif nuevo_volumen > 100:
#             self.volumen = 100
#             print(f'''El volumen fue ajustado al límite máximo: 100''')
#         else:
#             self.volumen = 0
#             print(f'''El volumen fue ajustado al límite mínimo: 0''')
            
# prueba = ReproductorMusica()
# prueba.obtener_volumen()
# prueba.aplicar_volumen(19)
# prueba.obtener_volumen()
# prueba.aplicar_volumen(-9)
# prueba.obtener_volumen()
# prueba.aplicar_volumen(1999)

# #------------------------- PUNTO 2 -------------------------------

# def accion():
#     print("Se le recomienda la película de acción: Spider-Man 2")

# def comedia():
#     print("Se le recomienda la película de Comedia: Deadpool")

# def terror():
#     print("Se le recomienda la película de Terror: El Aro")
    
# def eleccionPropia():
#     print("Se le recomienda la película de Tercermundismo: Matare")

# def opcionInvalida():
#     print("La opción ingresada no es válida. Ingrese una válida.")

# diccionario = {
#     1 : accion,
#     2 : comedia,
#     3 : terror,
#     4 : eleccionPropia  
# }

# print("Menú de géneros: \n 1. Acción \n 2. Comedia \n 3. Terror \n 4. Opción Propia \n")
# opcion = int(input("Seleccione un género de película correspondiente al menú: "))
# resultado = diccionario.get(opcion,opcionInvalida)
# resultado()

#------------------------- PUNTO 3 -------------------------------

# edad = int(input("Ingrese su edad actual: "))
# print()

# if edad > 0 and edad < 13:
#     print("Usted es un niño.")
# elif edad > 13 and edad < 17:
#     print("Usted es un adolescente.")
# elif edad > 18 and edad < 65:
#     print("Usted es un adulto.")
# elif edad > 65:
#     print("Usted es un Anciano")
# else:
#     print("La edad ingresada no es válida.")