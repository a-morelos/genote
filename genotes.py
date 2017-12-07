#Script para generar referencias y notas a pie de página
#Fecha 05/12/2017

import argparse
from yattag import Doc

parser = argparse.ArgumentParser(description="Generador de notas y referencias en HTML")
group = parser.add_argument_group('rango')
group.add_argument("-f", type=int, help="inicio de rango", default=0)
group.add_argument("-t", type=int, help="fin de rango", default=0)

parser.add_argument("n", type=int, help="numero de notas a generar")
#parser.add_argument("-s", help="Lugar de origen de la referencia")
args = parser.parse_args()
num = args.n
#cap = args.s


doc, tag, text = Doc().tagtext()

notas = []

def crearNota(n):

	with tag('div', klass="nota"):
		with tag('p'):
			text(n, '. Aquí va el texto de nota.')
			with tag('a', href="../Text/"):
				doc.asis('&lt;&lt;')
	nota=doc.getvalue()
	return nota

i = 0

while i <= num:

	nueva_nota = crearNota(i + 1)
	notas.append(nueva_nota)

print('Has creado ', len(notas), 'notas')

for item in notas:
	print(item)
