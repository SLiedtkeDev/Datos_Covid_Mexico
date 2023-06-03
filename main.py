from matplotlib import pyplot as plt

headers_tablas_maximos = ['Estado', 'Fecha', 'Maximo']
headers_tablas_porcentaje = [
    'Estado', 'Poblacion', '# Contagiados', 'Porcentaje']


def grafica_linea(x, y):
    fig, ax = plt.subplots(figsize=(20, 15))
    ax.plot(x, y)
    plt.xticks(x, rotation=90)
    plt.show()


def grafica_barra(x, y):
    fig, ax = plt.subplots(figsize=(20, 15))
    ax.bar(x, y)
    plt.xticks(x, rotation=90)
    plt.show()


def muestra_tabla(datos, headers):
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.table(cellText=datos, loc="center", colLabels=headers)
    ax.axis('tight')
    ax.axis('off')
    plt.show()


def crear_matriz_inicial():
    matriz = []
    with open("casos_covid.csv", "r") as file:
        linea = True
        while linea:
            linea = file.readline()
            fila = linea.split(",")
            matriz.append(fila)
        matriz = matriz[:-1]
        return matriz


def crear_menu():
    print("""
     _____        _               _____           _     _  
    |  __ \      | |             / ____|         (_)   | | 
    | |  | | __ _| |_ ___  ___  | |     _____   ___  __| | 
    | |  | |/ _` | __/ _ \/ __| | |    / _ \ \ / / |/ _` | 
    | |__| | (_| | || (_) \__ \ | |___| (_) \ V /| | (_| | 
    |_____/ \__,_|\__\___/|___/  \_____\___/ \_/ |_|\__,_| 
    
                                                        
    +----------------------+-------+
    |  Selecciona Opcion   | Nume. |
    +----------------------+-------+
    | Dia con mas casos    |     1 |
    | Casos por porcentaje |     2 |
    | Linea de tiempo      |     3 |
    | Salir                |     4 |
    +----------------------+-------+                                                      
    """)
    print(70 * '*')


def tabla_plot_maximos_casos(matriz):
    matriz_casos = []
    eje_x = []
    eje_y = []
    for i in range(1, len(matriz)):
        F = []
        estado = matriz[i][2]
        estado = estado.strip('\"')
        F.append(estado)
        casos_maximos = 0
        indice = None
        for j in range(3, len(matriz[0])):
            if int(matriz[i][j]) > casos_maximos:
                indice = j
                casos_maximos = int(matriz[i][j])
        fecha = matriz[0][indice]
        F.append(fecha)
        F.append(casos_maximos)
        matriz_casos.append(F)
    muestra_tabla(matriz_casos, headers_tablas_maximos)
    for i in range(len(matriz_casos)-1):
        x = matriz_casos[i][0]
        y = matriz_casos[i][2]
        eje_x.append(x)
        eje_y.append(y)
    grafica_linea(x=eje_x, y=eje_y)


def tabla_plot_casos_porcentaje(matriz):
    matriz_porcentajes = []
    eje_x = []
    eje_y = []
    for i in range(1, len(matriz)):
        F = []
        estado = matriz[i][2]
        estado = estado.strip('\"')
        F.append(estado)
        poblacion = matriz[i][1]
        F.append(poblacion)
        suma_casos = 0
        for j in range(4, len(matriz[0])):
            suma_casos += int(matriz[i][j])
        F.append(suma_casos)
        porcentaje_infeccion = round((suma_casos / int(poblacion)) * 100, 2)
        F.append(porcentaje_infeccion)
        matriz_porcentajes.append(F)
    muestra_tabla(matriz_porcentajes, headers_tablas_porcentaje)
    for i in range(len(matriz_porcentajes)-1):
        x = matriz_porcentajes[i][0]
        y = matriz_porcentajes[i][3]
        eje_x.append(x)
        eje_y.append(y)
    grafica_barra(x=eje_x, y=eje_y)


def crear_linea_tiempo(matriz, lugar):
    pass


def main():
    crear_menu()
    datos = crear_matriz_inicial()
    while True:
        opcion = int(input("Que opcion deseas elegir: "))
        if opcion == 4:
            print("Vuelva pronto, gracias por usar nuestro sistema!")
            break
        elif opcion == 1:
            tabla_plot_maximos_casos(datos)
        elif opcion == 2:
            tabla_plot_casos_porcentaje(datos)
        elif opcion == 3:
            lugar = int(input(""))
            crear_linea_tiempo(datos)
        else:
            print("Opcion no valida, vuelva a elegir")


if __name__ == "__main__":
    main()
