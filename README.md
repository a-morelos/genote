Genote es un script en python3 para generar notas en HTML. Fue pensado para facilitar la creación de notas usadas en ebooks para el formato ePub. Aún esta en una fase temprana de desarrollo.

Genera dos archivos: ```notas.xhtml``` y ```referencias.xhtml``` que contienen el código HTML necesario para la creación de notas.

---
**Ejemplo de código generado en ```notas.xhtml```:**

```
<div class="nota">
  <p id="nt1"><sup>1</sup> **Aquí va el texto de nota.** <a href="../Text/capitulo01.html#rf1">&lt;&lt;</a></p>
</div>
```

---
**Ejemplo de código generado en ```referencias.xhtml```**
```
<a href="../Text/notas.xhtml#nt1 id="rf1"><sup>[1]</sup></a>
```

Requisitos para uso
--------------------
* [Yattag](http://www.yattag.org). Es una biblioteca para Python que permite generar texto HTML/XML de forma dinámica.

Uso
----
Abrir un terminal en la ubicación donde se desee crear los archivos y ejecute el script:

```python genote.py <numero-de-notas> [<opciones-de-rango>]```

Debería terminar con dos archivos:

```
notas.xhtml
referencias.xhtml
```

Donde notas.xhtml contiene las notas del archivo y referencias.xhtml el código para referenciar dichos archivos

## Creación de notas por rangos
Genote posee opciones para la elaboración de notas por rangos. Para esto, el numero de notas debe ser **0**.

```-f Define el inicio de rango```


```-t Define el fin de rango```

Por ejemplo si deseáramos crear notas del número 75 al número 105, el comando a ejecutar sería:

```python genote.py 0 -f 75 -t 105```
