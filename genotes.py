#Script para generar referencias y notas a pie de página
#Fecha 05/12/2017

import argparse
from yattag import Doc, indent

parser = argparse.ArgumentParser(description="Generador de notas y referencias en HTML")
group = parser.add_argument_group('rango')
group.add_argument("-f", type=int, help="inicio de rango", default=0)
group.add_argument("-t", type=int, help="fin de rango", default=0)

parser.add_argument("n", type=int, help="numero de notas a generar, escriba cero (0) si desea introducir rango")
#parser.add_argument("-s", help="Lugar de origen de la referencia")
args = parser.parse_args()
num = args.n
ini = args.f
fin =args.t
#source = args.s

origen = "capitulo1.xhtml"
archivo_notas = "notas.xhtml"

doc, tag, text, line = Doc().ttl()

def crearNota(n, archivo):
	with tag('div', klass = "nota"):
		with tag('p', id = "nt{}".format(n)):
			line('sup', '[{}]'.format(n))
			text('Aquí va el texto de nota.')
			with tag('a', href = "../Text/{}#{}".format(archivo, n)):
				doc.asis('&lt;&lt;')
	
	nota = doc.getvalue()
	return nota

def crearReferencia(n, archivo_notas):
	with tag('sup', id = n):
		with tag ('a', href = "../Text/notas.xhtml#nt{}".format(n), id="rf{}".format(n)):
			line('sup', '[{}]'.format(n))
	
	ref = doc.getvalue()
	return ref

i = 0

if num != 0:
	
	while i < num:
		nueva_nota = crearNota(i + 1, origen)
		nueva_ref = crearReferencia(i + 1, archivo_notas)
		notas = nueva_ref
		i += 1

	print (indent(notas))
elif args.f == 0 | args.t == 0:
	print("Debe indicar inicio y fin para rango")
else:

	while ini <= fin:
		nueva_nota = crearNota(ini, origen)
		nueva_ref = crearReferencia(ini, archivo_notas)
		notas = nueva_ref
		ini += 1
		i+= 1
	print (indent(notas))

print('Has creado ', i, 'notas')
