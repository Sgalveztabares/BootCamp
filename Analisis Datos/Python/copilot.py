def agregar_estudiante(estudiantes):
    """Función para agregar un estudiante con sus calificaciones."""
    nombre = input("Introduce el nombre del estudiante: ")
    num_materias = int(input("¿Cuántas materias tiene el estudiante? "))
    calificaciones = []
    
    for i in range(1, num_materias + 1):
        calificacion = float(input(f"Introduce la calificación de la materia {i} (1-10): "))
        while calificacion < 1 or calificacion > 10:
            print("La calificación debe estar entre 1 y 10.")
            calificacion = float(input(f"Introduce la calificación de la materia {i} (1-10): "))
        calificaciones.append(calificacion)
    
    promedio = sum(calificaciones) / len(calificaciones)
    estado = "Aprobado" if promedio >= 6 else "Desaprobado"
    
    estudiantes.append({
        "nombre": nombre,
        "calificaciones": calificaciones,
        "promedio": promedio,
        "estado": estado
    })
    print(f"Estudiante {nombre} agregado correctamente.\n")


def listar_estudiantes(estudiantes):
    """Función para listar todos los estudiantes y sus datos."""
    if not estudiantes:
        print("No hay estudiantes registrados.\n")
        return
    
    print("\nLista de estudiantes:")
    for estudiante in estudiantes:
        print(f"Nombre: {estudiante['nombre']}")
        print(f"Calificaciones: {estudiante['calificaciones']}")
        print(f"Promedio: {estudiante['promedio']:.2f}")
        print(f"Estado: {estudiante['estado']}\n")


def main():
    estudiantes = []
    while True:
        print("Gestión de Estudiantes y Notas")
        print("1. Agregar estudiante")
        print("2. Listar estudiantes")
        print("3. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            agregar_estudiante(estudiantes)
        elif opcion == "2":
            listar_estudiantes(estudiantes)
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.\n")


if __name__ == "__main__":
    main()