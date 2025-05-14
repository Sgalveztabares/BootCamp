#if y else

"""
sueldo = int(input("Ingrese su sueldo: "))
if sueldo < 1500000:
    print("Tiene derecho a un bono de 200.000")
    sueldo = sueldo + 200000
    print("Su sueldo total es: ", sueldo )
else: 
    print("Tiene derecho a un bono de 50.000")
    sueldo = sueldo + 50000
    print("Su sueldo total es: ", sueldo )
print("Fin del programa")"""


"""
edad = int(input("Intruduce tu edad: "))

if edad >= 18:
    print("Le puedo vender cerveza por se mayor de edad")
else:
    print("Eres menor de edad, no te puedo vender cerveza")"""


#Elif
"""
edad = int(input("Introduce la edad: "))

if edad < 6 and edad > 0:
    print("Primera infacia")
elif edad >= 6 and edad < 13:
    print("Infancia")
elif edad >= 13 and edad < 18:
    print("Adolescencia")
elif edad >= 18:
    print("Adulto")
elif edad <= 0:
    print("Fabrique primero al mocoso")"""
    
dia = int(input("Ingrese el numero de un dia de la semana: "))

if dia == 1:
    print("Es lunes")
elif dia == 2:
    print("Es martes")
elif dia == 3:
    print("Es miercoles")
elif dia == 4:
    print("Es jueves")
elif dia == 5:
    print("Es viernes")
elif dia == 6:
    print("Es sabado")
elif dia == 7:
    print("Es domingo")
else:
    print("Pusiste un numero fuera de rango")

