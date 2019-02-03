#Script para generar referencias y notas a pie de página
#Autor: Alberto Morelos
#Fecha 05/12/2017

import argparse, sys
from yattag import Doc, indent

parser = argparse.ArgumentParser(description="Generador de notas y referencias en HTML")

#define un grupo de parametros para introducir notas por rangos
group = parser.add_argument_group('rango')
group.add_argument("-f", type=int, help="inicio de rango", default=0)
group.add_argument("-t", type=int, help="fin de rango", default=0)

parser.add_argument("n", type=int, help="numero de notas a generar, escriba cero (0) si desea introducir rango")
parser.add_argument("-s", help="Lugar de origen de la referencia (sin extensión, la extension por default es xhtml)", default="capitulo1")
#parser.add_argument("-o", help="Archivo de destino para las notas.")
#parser.add_argument("-e", help="Cambio de extension para las referencias de un archivo" default="xhtml")

args = parser.parse_args()

total_notas = args.n
inicio_rango = args.f
fin_rango =args.t
# capitulo de origen
cap_origen = args.s + '.xhtml'
# archivo_notas = args.o + 'xhtml'

archivo_notas = "notas.xhtml"
archivo_refs = "referencias.xhtml"

#doc, tag, text, line = Doc().ttl()

def crearNota(num_nota, archivo_texto):

	# Genera una instancia de Doc para la nota
	note, tag, text, line = Doc().ttl()

	with tag('div', klass = "nota"): 
		with tag('p', id = "nt{}".format(num_nota)): 
			line('sup', '[{}]'.format(num_nota)) 
			text(' **Aquí va el texto de nota.** ')
			with tag('a', href = "../Text/{}#rf{}".format(archivo_texto, num_nota)):
				note.asis('&lt;&lt;')
	
	nota = indent(note.getvalue())
	return nota

def crearReferencia(num_nota, archivo_notas):

	# Genera una instancia de Doc para la referencia
	doc, tag, text, line = Doc().ttl()
	
	with tag ('a', href = "../Text/{}#nt{}".format(archivo_notas, num_nota), id="rf{}".format(num_nota)):
		line('sup', '[{}]'.format(num_nota))
	
	ref = doc.getvalue()
	return ref

def generarArchivo(archivo_notas, notas, accion):
	with open(archivo_notas, accion) as output_file:
		for x in notas:
			output_file.write(x)

def imprimir(archivo_notas, notas):
	try:
		generarArchivo(archivo_notas, notas, 'x')
	except FileExistsError:
		print("El archivo {} ya existe. ¿Desea sobreescribir?".format(archivo_notas))
		resultado = input("s/n ")
		if resultado == 's':
			generarArchivo(archivo_notas, notas, 'w')
		elif resultado == 'n':
			generarArchivo(archivo_notas, notas, 'a')
			print("Agregado al final del archivo {}".format(archivo_notas))

i = 0
notas = []
referencias = []

if total_notas != 0:
	
	while i < total_notas:
		notas.append(crearNota(i + 1, cap_origen) + "\n\n")
		referencias.append(crearReferencia(i + 1, archivo_notas) + "\n")
		i += 1

	#print(notas)
	imprimir(archivo_notas, notas)
	imprimir(archivo_refs, referencias)

#Se indica falta de parametros y se termina la ejecucion
elif args.f == 0 | args.t == 0:
	print("Debe indicar inicio y fin para rango")
else:

	while inicio_rango <= fin_rango:
		notas.append(crearNota(inicio_rango, cap_origen) + "\n\n")
		referencias.append(crearReferencia(inicio_rango, archivo_notas) + "\n")
		inicio_rango += 1
	#print (notas)
	imprimir(archivo_notas, notas)
	imprimir(archivo_refs, referencias)

print('Has creado ', len(notas), 'notas')
sys.exit()
