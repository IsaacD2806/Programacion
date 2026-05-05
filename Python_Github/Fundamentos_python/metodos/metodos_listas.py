# creando una lista con list
lista = list([17,True,'Shohei Ohtani'])

# devuelve la cantidad de elementos de una lista
quantity_elements = len(lista)

# APPEND agrega elementos a la lista 
lista.append(15)

# INSERT agregando un elemento a la lista en un indice en especifico
lista.insert(3,False)

# EXTEND agrega varios elementos a la lista
lista.extend([15449])

# POP elimina un elemento de la lista por su indice
lista.pop(0) # -1 para eliminar el ultimo elemento de la lista, -2 para el ante-ultimo y asi sucesivamente

# REMOVE remueve un elemento de la lista por su valor
lista.remove('Shohei Ohtani')

# CLEAR elimina todos los elementos de la lista
# lista.clear()

# SORT ordena los elementos de la lista de manera ascendente (si usamos REVERSE lo ordena en reversa)no se pueden cadenas de texto
lista.sort()

# REVERSE invierte los elementos de una lista
lista.reverse()

# verificamos si un elemento se encuentra en la lista
search_element = lista.index(True)
print(search_element)