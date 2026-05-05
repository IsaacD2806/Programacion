cadena1 = 'Hola,mundo,betelgeuse'
cadena2 = 'bienvenido'
# dir es una funcion
resultado = dir(cadena1)

# forma: DATO.metodo()

# Convierte todo a mayusculas
mayuscula = cadena1.upper() 

# Convierte todo a minusculas
minuscula = cadena1.lower() 

# Convierte la primera letra en mayuscula
primer_letra_mayuscula = cadena1.capitalize()

# Buscamos una cadena en otra cadena, si no hay coincidencia nos devuelve -1
search_find = cadena1.find('z')

# Buscamos una cadena en otra cadena, si no hay coincidencia nos muestra una excepcion
search_index = cadena1.index('s')

# Si el dato es numerico, devuelve True, sino devuelve False
is_numeric = cadena1.isnumeric()

# Si el dato es alfanumerico , devuelve True, sino devuelve False
is_aphanumeric = cadena1.isalpha()

# Contamos coincidencias de una cadena dentro de otra cadena, devuelve la cantidad de coincidencia
counter_coincidence = cadena1.count('e')

# Contamos la cantidad de caracteres que tiene una cadena
counter_characters = len(cadena1)

# verificamos si una cadena empieza con otra cadena dada, si es asi devuelve True
start_with = cadena1.startswith('H')

# verificamos si una cadena termina con otra cadena dada, si es asi devuelve True
end_with = cadena1.endswith('se')

# Si el valor 1, se encuentra en la cadena original, reemplaza el valor 1 de la misma por el valor 2
string_new = cadena1.replace(',', ' ')

# separar cadenas con la cadena que le pasemos
string_separate = cadena1.split(',')
print(search_index)