# -*- coding: utf-8 -*-
# pmli.py
#
# Descripcion: Implementacion del TAD PMLI
#
# Autores: 
#	Br. Jean Alexander 12-10848
# 	Br. Diego Pedroza 12-11281
#
from conjunto import*

#Descripcion: Dado un string, verifica si el mismo esta compuesto
#unicamente por letras del alfabeto
#Parametros: p - string
#Precondicion: True
#Postcondicion: all("a"<=p[i]<="z" or p[i]=='ñ' for i in range(0,len(p)))
def esPalabraValida(p:str)->bool:
	try:
		return all("a"<=p[i]<="z" or p[i]=='ñ' for i in range(0,len(p)))
	except:
		return False
	
#Implementacion del TAD PMLI
class pmli(object):
	#Descripcion: Creacion de un pmli vacio
	#Parametros: l - string
	#Precondicion: esPalabraValida(l) y len(l)==1
	#Postcondicion: self.letra = l y self.palabras es un conjunto vacio
	def __init__(self,l:str):
		if esPalabraValida(l) and len(l)==1:
			self.letra = l
			self.palabras = Conjunto()
		else:
			print(str(l)+" no es una letra valida")
	
	#Descripcion: Agrega una palabra al conjunto de palabras del pmli
	#Parametros: p -string
	#Precondicion: esPalabraValida(p) y p[0]==self.letra
	#Postcondicion: self.palabras = self.palabras inicial unido con {p}
	def agregarPalabra(self,p:str):
		if esPalabraValida(p) and p[0]==self.letra:
			self.palabras.agregar(p)
		else:
			if p[0] != self.letra:
				print(p+" no comienza con "+self.letra)
			else:
				print(str(p)+" no es una palabra valida")

	#Descripcion: Elimina una palabra del conjunto de palabras del pmli
	#Parametros: p - string
	#Precondicion: esPalabraValida(p) y p[0]==self.letra
	#Postcondicion: self.palabras = self.palabras inicial menos {p}
	def eliminarPalabra(self,p:str):
		if esPalabraValida(p) and p[0]==self.letra:
			self.palabras.eliminar(p)
		else:
			print(str(p)+" no es una palabra valida")

	#Descripcion: Muestra el conjunto de palabras del pmli
	#Parametros: -
	#Precondicion: True
	#Postcondicion: Muestra por la salida estandar los elementos en
	#self.palabras en orden lexicografico
	def mostrarPalabras(self):
		print(self.palabras)
