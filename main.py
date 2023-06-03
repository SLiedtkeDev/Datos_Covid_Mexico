from matplotlib import pyplot as plt

headers_tablas_maximos = ['Estado', 'Fecha', 'Maximo']
headers_tablas_porcentaje = [
    'Estado', 'Poblacion', '# Contagiados', 'Porcentaje']


def grafica_linea(x, y, title):
    fig, ax = plt.subplots(figsize=(11, 6))
    ax.plot(x, y)
    ax.grid(True)
    ax.set_ylabel("Contagios")
    ax.set_title(title)
    plt.xticks(x, rotation=90)
    plt.show()


def grafica_barra(x, y):
    fig, ax = plt.subplots(figsize=(11, 6))
    ax.bar(x, y)
    ax.grid(True)
    ax.set_ylabel("Porcentaje")
    ax.set_title("% Contagios respecto a la población")
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
            linea = linea[:-1]
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
    grafica_linea(x=eje_x, y=eje_y,
                  title='Máximos  # de contagios por estado')


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


def crear_linea_tiempo(matriz):
    lugar_no_encontrado = True
    posicion_lugar = -1

    while lugar_no_encontrado:
        print(70 * '*')
        print("En Lugar puedes teclear el nombre de algun estado o Nacional")
        print(70 * '*')
        lugar = input("Lugar -> ").upper()
        posicion_lugar = buscar_lugar(matriz, lugar)

        if posicion_lugar != -1:
            lugar_no_encontrado = False
        else:
            print("Lugar inválido")

    cabecera, datos = obtener_cabecera_datos_lugar(matriz, posicion_lugar)
    lista_meses, lista_datos = obtener_listas_meses_datos(cabecera, datos)
    titulo = "Serie de tiempo mensual para " + lugar

    grafica_linea(lista_meses, lista_datos, title=titulo)


def obtener_listas_meses_datos(cabecera, datos):
    n_columnas = len(cabecera)
    mes_anterior = cabecera[3]
    suma = 0
    lista_meses = []
    lista_datos = []

    for i in range(3, n_columnas):
        dato = int(datos[i])
        mes_actual = cabecera[i]
        mes_numero = mes_actual.split('-')[1]
        mes_numero_anterior = mes_anterior.split('-')[1]

        if (mes_numero == mes_numero_anterior):
            suma += dato
        else:
            lista_meses.append(mes_actual[3:])
            lista_datos.append(suma)

            mes_anterior = mes_actual
            suma = 0

    return lista_meses, lista_datos


def obtener_cabecera_datos_lugar(matriz, posicion_lugar):
    return matriz[0], matriz[posicion_lugar]


def buscar_lugar(matriz, lugar):
    for i in range(1, len(matriz)):
        nombre = matriz[i][2].upper().replace("\"", '')

        if nombre == lugar:
            return i

    return -1


def main():
    crear_menu()
    datos = crear_matriz_inicial()
    while True:
        opcion = input("Que opcion deseas elegir: ")
        if opcion == '4':
            print("Vuelva pronto, gracias por usar nuestro sistema!")
            break
        elif opcion == '1':
            tabla_plot_maximos_casos(datos)
        elif opcion == '2':
            tabla_plot_casos_porcentaje(datos)
        elif opcion == '3':
            crear_linea_tiempo(datos)
        else:
            print("Opcion no valida, vuelva a elegir")


if __name__ == "__main__":
    main()
