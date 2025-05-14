"""
frutas = ("banana", "manzana", "pera", "kiwi", "mango") #Es inmutable

print(frutas)
print(len(frutas))
print(frutas.count("bananas"))
print(frutas.index("kiwi"))
print(frutas[0])
print(frutas[1:])
"""

empleados = ("Juan", "Pedro", "Maria", "Ana", "Luis")

print(empleados)
copia = list(empleados)
copia.remove("Maria")
print(copia)
empleados = tuple(copia)
print(empleados)

