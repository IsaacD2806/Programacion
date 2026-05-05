diccionary = {
    'Nombre':'Isaac',
    'Apellido':'Palomino',
    'edad':17
}

# devuelve un objeto dict_item
claves = diccionary.keys()

# obteniendo un elemento con get() y si no encuentra nada el programa continua
name_value = diccionary.get('Nombre')
print('Hello world')

# elimina todos los elementos del diccionario
# diccionary.clear()

# eliminando un elemento del diccionario
diccionary.pop('edad')

# obtiniendo un elemento dict_elemento iterable
diccionary_iterable = diccionary.items()
print(diccionary_iterable)