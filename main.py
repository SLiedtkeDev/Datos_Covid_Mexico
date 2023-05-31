def crear_matriz():
    matriz = []
    with open("casos_covid.csv", "r") as file:
        linea = True
        while linea:
            linea = file.readline()
            fila = linea.split(",")
            matriz.append(fila)
        matriz = matriz[:-1]
        return matriz


def creat_menu():
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


def crear_tabla_maximos_casos(matriz):
    pass


def crear_tabla_casos_porcentaje(matriz):
    pass


def crear_linea_tiempo(matriz):
    pass


def main():
    creat_menu()
    datos = crear_matriz()
    while True:
        opcion = int(input("Que opcion deseas elegir: "))
        if opcion == 4:
            print("Vuelva pronto, gracias por usar nuestro sistema!")
            break
        elif opcion == 1:
            crear_tabla_maximos_casos()
        elif opcion == 2:
            crear_tabla_casos_porcentaje()
        elif opcion == 3:
            crear_linea_tiempo()
        else:
            print("Opcion no valida, vuelva a elegir")


if __name__ == "__main__":
    main()
