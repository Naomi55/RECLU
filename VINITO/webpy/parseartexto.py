import re

#1.- Abrir archivo y extraer texto
_textoaparsear=open('TextoParaParseo.txt', 'r')  
_contenido=_textoaparsear.read()

#2.- Buscar patrones. --- Definir un Patron de busqueda
_patron = ((r"NOMBRE:\n"
	r"\s\n"
	r"(.*)\n"
	r"\s\n"
	r"CORREO:\s\n"
	r"(.*)\n"
	r"\s\n"
	r"EDAD:\s\n"
	r"(.*)\n"
	r"\s\n"
	r"DIRECCION:\n"
	r"\s\n"
	r"(.*)\n"
	r"\s\n"
	r"LICENCIATURA\n"
	r"\s\n"
	r"(.*)\n"
	r"\s\n"
	r"ESCUELA:\n"
	r"\s\n"
	r"(.*)\n"
	r"\s\n"
	r"PROMEDIO:\n"
	r"\s\n"
	r"(.*)\n"
	r"\s\n"
	r"IDIOMAS:\n"
	r"\s\n"
	r"(.*)\n"
	r"\s\n"
	r"EXPERIENCIA:\n"
	r"\s\n"
	r"(.*)\n"
	r"\s\n"
	r"\s\n"
	r"CURSOS:\n"
	r"\s\n"
	r"(.*\n"
	r"\s\n"
	r".*\s.*)\n"
	r"\s\n"
	r"CELULAR:\n"
	r"\s\n"
	r"(.*)\n"
	r"\s\n"
	r"APTITUDES:\n"
	r"\s\n"
	r"(.*\s.*\s.*\s.*\s.*)\n"
	r"\s\n"
	r"VACANTE:\s\n"
	r"(.*)")

#3.- Listado de resultados encontrados
_todos=re.findall(_patron, _contenido, re.MULTILINE)
print(_todos)

#4.- Mostrar
for _registro in _todos:
    print(_registro)
    print(_registro[1])