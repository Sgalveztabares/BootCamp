"""
frutas = {"manzanas", "banana","naranja", "kiwi", "mango"} #No tiene orden, y no puede tener elementos repertidos
print(frutas)

frutas.add("pera") #Agrega elementos al conjunto 
print(frutas)

frutas.remove("naranja") #Reemueve un pbjeto elegido
print(frutas)

frutas.discard("naranja") #Remueve un objeto, pero no da error si no esta el objeto a eliminar
print(frutas)

frutas.clear() #Elina todos lo elementos de un conjunto 
"""


colores = {"rojo", "verde", "azul", "amarillo"}
colores2 = {"verde", "azul"}
print(colores.difference(colores2)) # devuelve los elementos que no estan repertidos, esos son la diferencia
print(colores.union(colores2)) # Une los dos conjuntos
print(colores.intersection(colores2)) #Devueleve la intersection de los dos conjuntos
print(colores.issubset(colores2))
print(colores.issuperset(colores2))

