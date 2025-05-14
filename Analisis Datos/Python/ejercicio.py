"""
nombre = input("Ingrese su nombre: ")
parcial1 = float(input("Ingrese la nota del primer parcial: "))
parcial2 = float(input("Ingrese la nota del segundo parcial: "))
parcial3 = float(input("Ingrese la nota del tercer parcial: "))
lista = [parcial1, parcial2, parcial3]
promedio = sum(lista) / len(lista)

if promedio >= 1 and promedio < 3:
    print(nombre, "Su promedio es de: ", promedio)
    print("Reprueba")
elif promedio >= 3 and promedio < 4:
    print(nombre, "Su promedio es de: ", promedio)
    print("Tiene que reforzar")
elif promedio >= 4 and promedio <= 5:
    print(nombre, "Su promedio es de: ", promedio)
    print("Aprueba")
"""

"""
Restaurante el Buen Comer
1. Tamales = 20.00
2. Tacos = 15.00
3. Tortas = 25.00
4. Enchiladas = 30.00
5. Quesadillas = 18.00
6. Sopes = 22.00
7. Finalizar Pedido
"""


tamales = 20
tacos = 15
tortas = 25
enchiladas = 30
quesadillas = 18
sopes = 22
menu = [tamales, tacos, tortas, enchiladas, quesadillas, sopes]
pedido = []
precio = sum(pedido)






