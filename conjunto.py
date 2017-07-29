# -*- coding: utf-8 -*-
# pmli.py
#
# Descripcion: Implementacion del TAD Conjunto(enlazado)
#
# Autores: 
#	Br. Jean Alexander 12-10848
# 	Br. Diego Pedroza 12-11281
#

#Descripcion: Dado dos strings verifica si el primero es mayor que el
# segundo, de serlo devuelve True. En caso contrario devuelve False
# NOTA: Esta funcion permite que el orden lexicografico estandar de
# Unicode, ubique a la ñ entre la n y la o .
#Parametros: s1,s2 - string
#Precondicion: True
#Postcondicion: True
def mayor(s1:str,s2:str):
	for i in range(1,len(s1)):
		for j in range(1,len(s2)):
			if s1[i]=='ñ' and s2[j] >='o':
				return True
			elif s2[j]=='ñ' and s1[i] >='o':
				return False
			elif s1[i]<='n' and s2[j]=='ñ':
				return False
			elif s2[j]<='n' and s1[i]=='ñ':
				return True
			else:
				return s1 > s2
			
class Nodo(object):
	def __init__(self,elem):
		self.elem = elem
		self.sig = None

class Conjunto(object):
	#Descripcion: Crea un Conjunto vacio
	#Parametros: -
	#Precondicion: True
	#Postcondicion: self._tam = 0
	def __init__(self):
		self._head = None
		self._tam = 0
	
	#Descripcion: Tamaño del conjunto
	#Parametros: -
	#Precondicion: True
	#Postcondicion: tam == self._tam
	def TAM(self)->int:
		tam = self._tam
		return tam
	
	#Descripcion: Verifica si un elemento pertenece al conjunto
	#Parametros: a
	#Precondicion: True
	#Postcondicion: IN == nodoActual is not None
	def pertenece(self,a)->bool:
		nodoActual = self._head
		while nodoActual is not None and nodoActual.elem != a:
			nodoActual = nodoActual.sig
		IN = nodoActual is not None
		return IN
	
	#Descripcion: Agrega un elemento al conjunto
	#Parametros: a
	#Precondicion: self.pertenece(a) == False
	#Postcondicion: self.pertenece(a) == True
	def agregar(self,a):
		if not self.pertenece(a):
			nodoActual = self._head
			nodoNuevo = Nodo(a)
			
			if nodoActual is None:
				nodoNuevo.sig = self._head
				self._head = nodoNuevo
			elif mayor(nodoActual.elem,nodoNuevo.elem):
				nodoNuevo.sig = nodoActual
				self._head = nodoNuevo
			else:
				while ((nodoActual.sig is not None) and
						mayor(nodoNuevo.elem,nodoActual.sig.elem)):
					nodoActual = nodoActual.sig
				nodoNuevo.sig = nodoActual.sig
				nodoActual.sig = nodoNuevo
			self._tam +=1
		else:
			print(a+', ya pertenece al conjunto')

	#Descripcion: Elimina un elemento del conjunto
	#Parametros: a 
	#Precondicion: True
	#Postcondicion:	self.pertenece(a) == False
	def eliminar(self,a):
		nodoAnterior = None
		nodoActual = self._head
		while nodoActual is not None and nodoActual.elem != a:
			nodoAnterior = nodoActual
			nodoActual = nodoActual.sig

		#El conjunto no contiene al elemento
		if nodoActual is None:
			return False

		#Desenlaza el nodo
		self._tam -= 1
		if nodoActual is self._head:
			self._head = nodoActual.sig
		else:
			nodoAnterior.sig = nodoActual.sig
		return True

	#Descripcion: Imprime el conjunto de forma legible por
	#la salida estandar
	#Parametros: -
	#Precondicion: True
	#Postcondicion: True
	def __str__(self):
		txt=""
		nodoActual = self._head
		while nodoActual is not None:
			txt += str(nodoActual.elem)+","
			nodoActual = nodoActual.sig
		txt = "{"+txt[:-1]+"}"
		return txt
