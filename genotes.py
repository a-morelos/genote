#Script para generar referencias y notas a pie de página
#Fecha 05/12/2017

import argparse
from yattag import Doc

parser = argparse.ArgumentParser(description="Generador de notas y referencias en HTML")
group = parser.add_argument_group('rango')
group.add_argument("-f", type=int, help="inicio de rango", default=0)
group.add_argument("-t", type=int, help="fin de rango", default=0)

parser.add_argument("n", type=int, help="numero de notas a generar")
#parser.add_argument("c", help="Lugar de origen de la referencia")
args = parser.parse_args()
num = args.n
#cap = args.c

doc, tag, text = Doc().tagtext()

#def generarNota(num):
#	if (args.f == 0 | args.t == 0):
#		while(i <= num):
with tag('div', klass="nota"):
	with tag('p'):
		text(num, '. Aquí va el texto de nota.')
		with tag('a', href="../Text/"):
			text('&lt&lt')
nota=doc.getvalue()
print(nota)
