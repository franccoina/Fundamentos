Algoritmo ConfigurarRecordatorioMeds
	Definir nomUsuario Como Cadena
	Escribir 'Hola, Usuario. Por favor, escribe tu nombre o el del paciente.'
	Leer nomUsuario
	Definir med Como Cadena
	Escribir 'Escribe el medicamento a ingerir.'
	Leer med
	Escribir 'AVISO: Según nuestra base, este medicamento está recetado por 3 dias, cada 8 horas.'
	Definir horaIngesta1 Como Entero
	Escribir 'Escribe solamente la hora, en formato 24hrs de la primera ingesta. Hora 24 no existe.'
	Leer horaIngesta1
	Mientras horaIngesta1>=24 Hacer
		Escribir 'ERROR: Escribe solamente la hora, en formato 24hrs de la primera ingesta.'
		Leer horaIngesta1
	FinMientras
	Definir minIngesta1 Como Entero
	Escribir 'Escribe los minutos de la hora, de la primera ingesta.'
	Leer minIngesta1
	Mientras minIngesta1>=60 Hacer
		Escribir 'ERROR: Escribe los minutos de la hora, de la primera ingesta.'
		Leer minIngesta1
	FinMientras
	Definir contador Como Entero
	contador <- 0
	Repetir
		horaIngesta1 <- horaIngesta1+8
		Si horaIngesta1>=24 Y horaIngesta1<48 Entonces
			Escribir nomUsuario, ', a las ', horaIngesta1-24, 'hrs y ', minIngesta1, 'min toma tu dosis de ', med
		SiNo
			Si horaIngesta1>=48 Entonces
				Escribir nomUsuario, ', a las ', horaIngesta1-48, 'hrs y ', minIngesta1, 'min toma tu dosis de ', med
			SiNo
				Escribir nomUsuario, ', a las ', horaIngesta1-0, 'hrs y ', minIngesta1, 'min toma tu dosis de ', med
			FinSi
		FinSi
		contador <- contador + 1
	Hasta Que contador=9
FinAlgoritmo
