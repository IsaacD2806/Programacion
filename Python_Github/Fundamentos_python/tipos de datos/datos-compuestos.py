# creando una lista (se pueden modificar)
lista = ['Isaac',16,'juego softbol',True,1.62]
# creando una tupla (no se pueden modificar)
tupla = ('Isaac',16,'juego softbol',True,1.62)
# esto es valido
#lista[1] = 22
# esto no es valido
#tupla[1] = 22

# creando un conujnto (set) (no se puede acceder a un indice, no almacena datos duplicados)
conjunto = {'Isaac',16,'juego softbol',True,1.62}
# print(conjunto[3]) no se puede acceder al elememnto

# creando un diccionario (dict), estrutura es (key : value) y separamos por comas (,) si tiene mas de un valor
diccionario = {
    'nombre' : "isaac",
    'edad' : 16,
    'esta_aprendiendo_a_programar' : True,
    'altura' : 1.62,
    'user_name' : 'Isaac1069'
}
print(diccionario['altura'] + 2)