# -*- coding: utf-8 -*-
# ayudante_ortografico.py
#
# Descripcion: Implementacion del TAD ayudante_ortografico
#
# Autores: 
#	Br. Jean Alexander 12-10848
# 	Br. Diego Pedroza 12-11281
#
from pmli import*

#Descripcion: Dados dos strings, devuelve la distancia entre ellos
#Parametros: s1,s2 - string
#Precondicion: True
#Postcondicion: True
def levenshtein(s1:str,s2:str)->int:
	m = [[0 for j in range(len(s2)+1)] for i in range(len(s1)+1)]
	for i in range(len(s1)):
		m[i+1][0] = i
	for j in range(len(s2)):
		m[0][j+1] = j
	for i in range(1,len(s1)+1):
		for j in range(1,len(s2)+1):
			comp = 1
			if s1[i-1]==s2[j-1]:
				comp = 0
			m[i][j] = min(m[i-1][j-1]+comp,m[i-1][j]+1,m[i][j-1]+1)
	return m[len(s1)][len(s2)]
	
class ayudante_ortografico(object):
	#Descripcion: Crea al ayudante ortografico
	#Parametros: -
	#Precondicion: True
	#Postcondicion: Se inicializa la estructura self.dicc creando
	# 27 instancias del TAD pmli, una para cada letra del alfabeto.
	def __init__(self):
		self.MAX = 27
		self.dicc = [ pmli(i) for i in 'abcdefghijklmnñopqrstuvwxyz']
	
	#Descripcion: Carga, desde un archivo .txt, todas las palabras que
	# cumplan con la funcion esPalabraValida al self.dicc en el pmli
	# correspondiente. Las palabras no validas las ignora
	#Parametros: nombre - string
	#Precondicion: el archivo nombre debe cumplir con el formato
	# establecido (una palabra por linea)
	#Postcondicion: Se agregan en self.dicc las palabras de nombre
	# que cumplen la especificacion del TAD pmli, en su pmli 
	# correspondiente
	def cargarDiccionario(self,nombre:str):
		try:
			f = open(nombre+".txt",'r')
			archivo = f.read()
			linea = archivo.splitlines()
			for i in range(len(linea)):
				if esPalabraValida(linea[i]):
					for j in range(27):
						if linea[i][0] == self.dicc[j].letra:
							self.dicc[j].agregarPalabra(linea[i])
			f.close()
		except:
			print('El diccionario posee una o más palabras no validas')
	
	#Descripcion: Dada una palabra verifica si es valida. Luego si lo
	# es, y pertenece a alguno de los pmli, la elimina, si no pertenece
	# a alguno de los pmli self.dicc se mantiene sin cambios.
	# Si la palabra no es valida se muestra el mensaje 
	# p+', no  es una palabra valida'
	#Parametros: p - string
	#Precondicion: esPalabraValida(p)
	#Postcondicion: si p pertenece al conjunto de palabras de alguno
	# de los pmli en self.dicc retorna True, de lo contrario False,
	# self.dicc es el diccionario despues de aplicar eliminarPalabra(p)
	# al pmli correspondiente
	def eliminarPalabra(self,p:str)->bool:
		try:
			i = 0
			while self.dicc[i].letra != p[0]:			
				i += 1
			self.dicc[i].eliminarPalabra(p)
			return True
		except:
			print(p+' no  es una palabra valida')
			return False
	
	#Descripcion: Dado un nombre de archivo de texto lo lee, verifica
	# cuales de las palabras en él son validas y no estan en el
	# diccionario. Luego para cada palabra del archivo encuentra las
	# cuatro palabras con menor distancia usando la Levenshtein distance
	# sobre el conjunto de palabras de cada pmli correspondiente.
	# El formato es: la palabra que no se encuentre en el diccionario 
	# comienza en una línea y luego le sigue las alternativas separadas
	# por un espacio.
	#Parametros: entrada - string
	#Precondicion: True
	#Postcondicion: Imprime en el archivo un salida cada una de las 
	# palabras validas contenidas en el archivo entrada que no se 
	# encuentren en dicc, seguidas de las cuatro palabras con menor 
	# distancia	
	def corregirTexto(self,entrada:str):
		f = open(entrada+'.txt','r')
		archivo = f.read()
		words = archivo.split()
		L = len(words)
		g = open("salida.txt","w")
		for i in range(0,L):
			if esPalabraValida(words[i]):
				for j in range(27):
					if words[i][0]==self.dicc[j].letra:
						if not self.dicc[j].palabras.pertenece(words[i]):
							nodoAnterior=self.dicc[j].palabras._head
							if nodoAnterior == None:
								g.write(words[i]+"\n")
								g.write("No existen palabras en el di")
								g.write("ccionario con esa letra ")
								g.write("o esta vacío\n\n")
							else:
								nodoActual=nodoAnterior.sig
								A = []
								while nodoActual is not None:
									if A == []:
										A=A+[nodoAnterior.elem]
									elif (levenshtein(words[i],A[0]) >=
										levenshtein(words[i],nodoAnterior.elem)):
										A=[nodoAnterior.elem]+A
									elif (levenshtein(words[i],A[0]) < 
										levenshtein(words[i],nodoAnterior.elem)):
										A=A+[nodoAnterior.elem]
									nodoAnterior = nodoActual
									nodoActual = nodoActual.sig								
								g.write(words[i]+"\n")
								if len(A)>=4:
									for k in range(4):
										g.write(A[k]+' ')
								else:
									for p in range(len(A)):
										g.write(A[p]+' ')
								g.write("\n")
		g.close()
		f.close()

	#Descripcion: Muestra la estructura dicc en un formato que permita
	# entender facilmente el contenido de la misma
	#Parametro: -
	#Precondicion: True
	#Postcondicion: Muestra dicc con las palabras en orden lexicografico
	def imprimirDiccionario(self):
		for i in range(27):
			print('Palabras que inician con '+self.dicc[i].letra)
			self.dicc[i].mostrarPalabras()


