# -*- coding: utf-8 -*-
# prueba_ortografia.py
#
# Descripcion: Cliente de prueba
#
# Autores: 
#	Br. Jean Alexander 12-10848
# 	Br. Diego Pedroza 12-11281
#

from ayudante_ortografico import*
import sys

separador="\n****\n"
		
def muestraOpciones():
	print(" Por favor, ingrese alguna de las siguientes\
 opciones:\n\
 1. Crear un nuevo ayudante ortográfico\n\
 2. Cargar un diccionario.\n\
 3. Eliminar palabra.\n\
 4. Corregir texto.\n\
 5. Mostrar diccionario\n\
 6. Salir de la aplicación\n")

def EleccionOpcion():
	i=0
	while True:
		
		try:
			muestraOpciones()
			opcion=int(input("Ingrese opción: "))
			print("\n")
			assert(any(opcion==i for i in range(0,7)))
			
			break
		except:
			print("opción inválida")
			i +=1
			if i>10:
				print("Máximo de intentos alcanzado")
				print("\nGracias por usar nuestro ayudante\n")
				
				sys.exit(12)
				
	return opcion

def proceso(numero,A,B,nombre):
	opcion=EleccionOpcion()
	
	#SALIR
	if opcion==6:
		print("Usted ha decidido salir.\nGracias por usar nuestro ayudante\n")
		sys.exit()

	#CREAR AYUDANTE
	elif opcion==1:
		if numero==0:
			A=ayudante_ortografico()
			print("Ha sido creado un nuevo ayudante\n")
			numero +=1
			print(separador)
			proceso(numero,A,B,nombre)
		else:
			A=ayudante_ortografico()
			print("Ha sido creado un nuevo ayudante, sobreescribiendo el anterior\n")
			numero +=1
			print(separador)
			proceso(numero,A,B,nombre)

	#CARGAR DICCIONARIO
	elif opcion==2:
		#No hay Ayudante Creados
		if numero==0:
			print("No existe un ayudante ortográfico donde cargar\ncree uno y luego vuelva a esta opción\n")
			proceso(numero,A,B,nombre)
		#Hay al menos un ayudante creado				
		elif numero>=1:
			j=0
			while True:
				try:
					nombre=str(input("Ingrese el nombre del diccionario omitiendo el .txt: "))
					A.cargarDiccionario(nombre)
					break
				except:
					print("No existe el archivo\n")
					j+=1
					if j>3:
						print("Máximo de intentos alcanzado")
						proceso(numero,A,B,nombre)
					else:
						pass
		print("\n")
		proceso(numero,A,B,nombre)			
	#MOSTRAR EL DICCIONARIO
	elif opcion==5:
		#No hay Ayudante Creados
		if numero==0:
			print("No existe un ayudante ortográfico donde cargar\ncree uno y luego vuelva a esta opción\n")
			
			proceso(numero,A,B,nombre)
		#Hay al menos un ayudante creado				
		elif numero>=1:
			A.imprimirDiccionario()
		print("\n")
		proceso(numero,A,B,nombre)


	#ELIMINAR PALABRA
	elif opcion==3:
		#No existen ayudantes
		if numero==0:
			print("No existe un ayudante ortográfico donde cargar\ncree uno y luego vuelva a esta opción\n")
			proceso(numero,A,B,nombre)
			
		#Hay al menos un ayudante creado				
		elif numero>=1:
			j=0
			while True:
				try:
					nombre=str(input("Ingrese la palabra a eliminar: "))
					A.eliminarPalabra(nombre)
					break
				except:
					print("No existe el archivo\n")
					j+=1
					if j>3:
						print("Máximo de intentos alcanzado")
						proceso(numero,A,B,nombre)
					else:
						pass
		print("\n")		
		proceso(numero,A,B,nombre)
	
	#CORREGIR TEXTO
	elif opcion==4:
		#No hay Ayudante Creados
		if numero==0:
			print("No existe un ayudante ortográfico donde cargar\ncree uno y luego vuelva a esta opción\n")
			proceso(numero,A,B,nombre)
		
		#Hay al menos un ayudante creado				
		elif numero>=1:
			j=0
			while True:
				try:
					nombre=str(input("Ingrese el nombre del archivo, omitiendo el .txt: "))
					A.corregirTexto(nombre)
					break
				except:
					print("No existe el archivo\n")
					j+=1
					if j>3:
						print("Máximo de intentos alcanzado")
						proceso(numero,A,B,nombre)
					else:
						pass
		print("\n")		
		proceso(numero,A,B,nombre)
		print("\n")
		proceso(numero,A,B,nombre)
		

print("Hola!\nBienvenido al menu de ayudante ortográfico JD\n")
A=0
B=0
nombre="Diccionario2"
numero=0
proceso(numero,A,B,nombre)

