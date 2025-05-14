estudiante = {"nombre": "Juan", 
            "edad": 30, 
            "notas": [3.2, 4.5, 2.8]
            }


promedio = sum(estudiante["notas"]) / len(estudiante["notas"])
print(estudiante["nombre"], "Este es su promedio este trimestre: ", promedio)    
#estudiante.clear()

estudiante.pop("notas")
print(estudiante)

#Diccionarios Anidados

familia = {
    
    "padre": {
        "nombre": "Juan"
        
    }
}





