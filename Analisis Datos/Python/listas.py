frutas = ["manzana", "banana", "kiwi", "mora", "sandía"]
verduras = ["Lechuga", "tomate", "zanahoria" "Brocoli", "espinaca"]
print(frutas[0])
print(len(frutas))
frutas.append("naranja")
print(frutas)
"""
frutas.clear()
print(frutas)
del frutas
print(frutas)
"""
frutas2 = frutas.copy()
frutas2.append("Mango")
print(frutas2)
print(frutas)
 
print(frutas.count("banana"))
frutas.extend(verduras)
print(frutas)
