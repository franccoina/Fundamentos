class tratamiento:
    def _init_(self, nombre, med, inicioIngesta, horasxDosis, duracionDias, funcion, infoUsuario, contador):
        tratamiento.nombre = self
        tratamiento.med = self
        tratamiento.inicioIngesta = self
        tratamiento.horasxDosis = self
        tratamiento.duracionDias = self
        tratamiento.contador = self
        tratamiento.funcion = self
        tratamiento.infoUsuario = self
    
    def infoBasica():
        tratamiento.nombre = str(input("Escribe tu nombre o el del paciente para el tratamiento: "))
        tratamiento.med = str(input("Escribe el nombre del medicamento para el tratamiento: "))

    def infoIngesta():
        tratamiento.inicioIngesta = int(input("Escribe la hora de primera ingesta del medicamento: "))
        tratamiento.horasxDosis = int(input("Escribe cada cuantas horas debes ingerir el medicamento: "))
        tratamiento.duracionDias = int(input("Escribe durante cuantos dias debes ingerir medicamento: "))

    def opFuncion():
        tratamiento.funcion = int((tratamiento.duracionDias*24)/tratamiento.horasxDosis)

    def tituloHorario():
        print(tratamiento.nombre,", a continuacion veras el horario en que debe tomar cada dosis de",tratamiento.med,":")

    def horarioMed():

        tratamiento.contador = 1

        while tratamiento.contador <= tratamiento.funcion:

            if tratamiento.inicioIngesta >= 24:
                tratamiento.inicioIngesta = tratamiento.inicioIngesta - 24
            else:
                tratamiento.inicioIngesta
    
            print("A las ",tratamiento.inicioIngesta,"hr es su ingesta numero ",tratamiento.contador," de ",tratamiento.funcion," toma(s) del medicamento.")
    
            tratamiento.inicioIngesta = tratamiento.inicioIngesta + tratamiento.horasxDosis

            tratamiento.contador = tratamiento.contador + 1

tratamiento.infoBasica()
tratamiento.infoIngesta()
tratamiento.opFuncion()
tratamiento.tituloHorario()
tratamiento.horarioMed()