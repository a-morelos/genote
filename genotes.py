#Script para generar referencias y notas a pie de página
#Fecha 05/12/2017

import argparse, sys
from yattag import Doc, indent

parser = argparse.ArgumentParser(description="Generador de notas y referencias en HTML")
group = parser.add_argument_group('rango')
group.add_argument("-f", type=int, help="inicio de rango", default=0)
group.add_argument("-t", type=int, help="fin de rango", default=0)

parser.add_argument("n", type=int, help="numero de notas a generar, escriba cero (0) si desea introducir rango")
parser.add_argument("-s", help="Lugar de origen de la referencia (sin extensión, la extension por default es xhtml)", default="capitulo1")
#parser.add_argument("-o", help="Archivo de destino para las notas.")
#parser.add_argument("-e", help="Cambio de extension para las referencias de un archivo" default="xhtml")

args = parser.parse_args()
num = args.n
#inicio de rango
ini = args.f
#fin de rango
fin =args.t
#capitulo de origen
origen = args.s + '.xhtml'
#archivo_notas = args.o + 'xhtml'

archivo_notas = "notas.xhtml"

doc, tag, text, line = Doc().ttl()

def crearNota(n, archivo):
	with tag('div', klass = "nota"):
		with tag('p', id = "nt{}".format(n)):
			line('sup', '[{}]'.format(n))
			text(' **Aquí va el texto de nota.** ')
			with tag('a', href = "../Text/{}#rf{}".format(archivo, n)):
				doc.asis('&lt;&lt;')
	
	nota = doc.getvalue()
	return nota

def crearReferencia(n, archivo_notas):
	with tag ('a', href = "../Text/{}#nt{}".format(archivo_notas, n), id="rf{}".format(n)):
		line('sup', '[{}]'.format(n))
	
	ref = doc.getvalue()
	return ref

def generarArchivo(archivo_notas, notas, accion):
	with open(archivo_notas, accion) as output_file:
			output_file.write(indent(notas))

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

if num != 0:
	
	while i < num:
		notas = crearNota(i + 1, origen)
		refs = crearReferencia(i + 1, archivo_notas)
		i += 1

	#print(indent(refs))
	imprimir(archivo_notas, refs)

elif args.f == 0 | args.t == 0:
	print("Debe indicar inicio y fin para rango")
else:

	while ini <= fin:
		nueva_nota = crearNota(ini, origen)
		nueva_ref = crearReferencia(ini, archivo_notas)
		notas = nueva_ref
		ini += 1
		i+= 1
	#print (indent(notas))
	imprimir(archivo_notas, notas)

print('Has creado ', i, 'notas')
sys.exit()
