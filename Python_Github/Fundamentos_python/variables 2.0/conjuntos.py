#creando un conjunto con set()
conjunto = set(['dato1','dato2'])
#metiendo un conjunto dentro de otro conjunto
conjunto1 = frozenset(['dato1','dato2'])
conjunto2 = {conjunto1,'dato3'}
print(conjunto2)
#teoria de conjuntos
conjunto1 = {1,8,5,6}
conjunto2 = {1,6,8}
#verificando si es un subconjunto
resultado = conjunto2.issubset(conjunto1)
resultado = conjunto2 <= conjunto1
#verificando si es superconjunto
resultado = conjunto2.issuperset(conjunto1)
resultado = conjunto2 > conjunto1
#verificar si hay un algun numero en comun
resultaodo = conjunto2.isdisjoint(conjunto1)
print(resultado)