def leer_archivo(ruta):
    with open(ruta, "r", encoding="utf-8") as file:
        info = [linea.strip() for linea in file]
    return info

def lista_empleados(datos):
    empleados = {}
    for i in range(1, len(datos)):
        linea = datos[i].split(";")
        nombres = linea[0]
        horas_trabajadas = linea[32]
        horas_contratadas = linea[33]

        if nombres not in empleados:
            empleados[nombres] = {
                "horas_trabajadas": horas_trabajadas,
                "horas_contratadas": horas_contratadas
            }

    return empleados

def main():
    info = leer_archivo("./alejandro_chaux.txt")
    empleados = lista_empleados(info)
    
    for nombre, datos in empleados.items():
        print(f"Nombre: {nombre} \nHoras Trabajadas: {datos['horas_trabajadas']} \nHoras Contratadas: {datos['horas_contratadas']}")
        print("-" * 40)

if __name__ == "__main__":
    main()