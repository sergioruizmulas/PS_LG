#!/usr/bin/python
import sys

# Se comprueba que el fichero con numeros exista
try:
	fichero = open('numeros.txt','r')
except:
	print "No esta el fichero"
	sys.exit
	
numeros = fichero.readlines()

# Se define una funcion para saber si el numero es un numero perfecto, abundante o defectivo. 
#
# - Un numero perfecto es aquel que es igual a la suma de sus divisores propios positivos,
#   excluyendose a si mismo. Por ejemplo 6 = 1+2+3
# - Un numero abundante es aquel que la suma de los divisores propios es mayor que el numero.
# - Un numero defectivo es aquel que la suma de los divisores propios es menor que el numero.
#
#

def ejercicio1(lista):
	for u in lista:
		try:
			u=int(u)
			y = int(1)
			SumaDivisores = 0
			while y < u:
				division = u % y
				if division == 0:
					SumaDivisores = SumaDivisores + y 
				y = y+1
			if SumaDivisores < u:
				print "%s es numero defectivo." %u
			elif SumaDivisores > u:
				print "%s es numero abundante." %u
			elif SumaDivisores == u:
				print "%s es numero perfecto." %u
		except:
			print "%s no es integer." %u

cadena = raw_input("Introduce un integer para su comprobacion o enter para tratar el fichero de numeros.txt: ")
if cadena == '':
	ejercicio1(numeros)
else:
	ejercicio1(cadena)

