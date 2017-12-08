#Script para generar referencias y notas a pie de página
#Fecha 05/12/2017

import argparse
from yattag import Doc, indent

parser = argparse.ArgumentParser(description="Generador de notas y referencias en HTML")
group = parser.add_argument_group('rango')
group.add_argument("-f", type=int, help="inicio de rango", default=0)
group.add_argument("-t", type=int, help="fin de rango", default=0)

parser.add_argument("n", type=int, help="numero de notas a generar, cero para introducir rango")
#parser.add_argument("-s", help="Lugar de origen de la referencia")
args = parser.parse_args()
num = args.n
#cap = args.s


doc, tag, text = Doc().tagtext()

def crearNota(n):
	with tag('div', klass = "nota"):
		with tag('p', id = n):
			text(n, '. Aquí va el texto de nota.')
			with tag('a', href = "../Text/"):
				doc.asis('&lt;&lt;')
	nota = doc.getvalue()
	return nota

def crearReferencia(n):
	with tag('sup', id = n):
		with tag ('a', href = "/Text/notas.xhtml#{}".format(n)):
			text('[{}]'.format(n))
	ref = doc.getvalue()
	return ref

i = 0

if num != 0:
	
	while i < num:
		nueva_nota = crearNota(i + 1)
		nueva_ref = crearReferencia(i + 1)
		notas = nueva_ref
		i += 1
elif args.f == 0 | args.t == 0:
	print("Debe indicar inicio y fin para rango")

print('Has creado ', i, 'notas')
print (indent(notas))
