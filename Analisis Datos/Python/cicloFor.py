"""
tabla = 1
for i in range (1,10):
    print (tabla, "x", i, "=", i*tabla)
    tabla+=1
    for i in range(1,11):
        print (tabla, "x", i, "=", i*tabla)"""
        

txt = input("Ingrese un texto: ")
letra = input("que letra desea contar: ")

for i in range (1,2):
    print(txt.count(letra))