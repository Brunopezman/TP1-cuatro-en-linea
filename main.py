import cuatro_en_linea
from typing import List

# CTE para finalizar juego
FINALIZAR = 'S'

def separar_con_guiones() -> None:
    print(100*'-')

def validar_filas_columnas() -> tuple:

    n_filas = input('Cantidad de filas mayores a 3: ')
    while not n_filas.isdigit() or not 3 < int(n_filas) <=10: 
        n_filas = input('Ingrese una cantidad de filas valida mayor a 3: ')

    n_columnas = input('Cantidad de columnas mayores a 3: ')
    while not n_columnas.isdigit() or not 3 < int(n_columnas) <= 10: 
        n_columnas = input('Ingrese una cantidad de columnas valida mayor a 3: ')

    return int(n_filas), int(n_columnas)

def validar_columna(n_columnas) -> int:
    col = input("Ingrese una columna para ubicar su ficha o 'S' para salir: ")
    if col.upper() == FINALIZAR:
        return col.upper()
        
    while not col.isdigit() or not 0 <= int(col) < n_columnas:
        col = input('ingrese una columna valida: ') 
    
    return int(col)

def imprimir_tablero(tablero: List[List[str]], n_columnas) -> None:

    for i in range(n_columnas):
        print('|'+str(i), end='')
    print('|')
    print('\n')
    for i in range(len(tablero)): 
        print('|' + '|'.join(tablero[i]) + '|')  

def main():
    print('Crucigrama interactivo')
    separar_con_guiones()

    n_filas, n_columnas = validar_filas_columnas()
    tablero = cuatro_en_linea.crear_tablero(n_filas,n_columnas)
    separar_con_guiones()

    imprimir_tablero(tablero, n_columnas)
    while not cuatro_en_linea.tablero_completo(tablero):
    
        if cuatro_en_linea.es_turno_de_x(tablero):
            print('Es el turno de X')
        else:
            print('Es el turno de O')

        col = validar_columna(n_columnas)
        if col ==FINALIZAR:
            break
        cuatro_en_linea.insertar_simbolo(tablero, col)
        imprimir_tablero(tablero, n_columnas)

        ganador = cuatro_en_linea.obtener_ganador(tablero)
        if ganador != ' ':
            print(f"El ganador fue {ganador}")
            return
        
    print('No gano ninguno')

main()