from typing import List

# Fichas del juego
J1 = 'X'
J2 = 'O'
NINGUNO = ' '

def crear_tablero(n_filas: int, n_columnas: int) -> List[List[str]]:
    """Crea un nuevo tablero de cuatro en línea, con dimensiones
    n_filas por n_columnas.
    Para todo el módulo `cuatro_en_linea`, las cadenas reconocidas para los
    valores de la lista de listas son las siguientes:
        - Celda vacía: ' '
        - Celda con símbolo X: 'X'
        - Celda con símbolo O: 'O'

    PRECONDICIONES:
        - n_filas y n_columnas son enteros positivos mayores a tres.

    POSTCONDICIONES:
        - la función devuelve un nuevo tablero lleno de casilleros vacíos
          que se puede utilizar para llamar al resto de las funciones del
          módulo.
    """
    tablero = []
    for _ in range(n_filas):
        fila = []
        for _ in range(n_columnas):
            fila.append(' ')
        tablero.append(fila)    

    return tablero

def es_turno_de_x(tablero: List[List[str]]) -> bool:
    """Dado un tablero, devuelve True si el próximo turno es de X. Si, en caso
    contrario, es el turno de O, devuelve False.
    - Dado un tablero vacío, dicha función debería devolver `True`, pues el
      primer símbolo a insertar es X.
    - Luego de insertar el primer símbolo, esta función debería devolver `False`
      pues el próximo símbolo a insertar es O.
    - Luego de insertar el segundo símbolo, esta función debería devolver `True`
      pues el próximo símbolo a insertar es X.
    - ¿Qué debería devolver si hay tres símbolos en el tablero? ¿Y con cuatro
      símbolos?

    PRECONDICIONES:
        - el parámetro `tablero` fue inicializado con la función `crear_tablero`
        - los símbolos del tablero fueron insertados previamente insertados con
          la función `insertar_simbolo`"""
    
    cantidad_x = 0
    cantidad_o = 0

    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if tablero[i][j] == J1:
                cantidad_x +=1 
            if tablero[i][j] == J2:
                cantidad_o +=1

    return cantidad_x == cantidad_o
            
def insertar_simbolo(tablero: List[List[str]], col: int) -> bool:
    """Dado un tablero y un índice de columna, se intenta colocar el símbolo del
    turno actual en dicha columna.
    Un símbolo solo se puede colocar si el número de columna indicada por
    parámetro es válido, y si queda espacio en dicha columna.
    El número de la columna se encuentra indexado en 0, entonces `0` corresponde
    a la primer columna.

    PRECONDICIONES:
        - el parámetro `tablero` fue inicializado con la función `crear_tablero`
    POSTCONDICIONES:
        - si la función devolvió `True`, se modificó el contenido del parámetro
          `tablero`. Caso contrario, el parámetro `tablero` no se vio modificado
    """
    if not 0 <= col < len(tablero[0]):
        return False
    
    for fila in range(len(tablero) - 1, -1, -1):
        
        if tablero[fila][col] == ' ':
            if es_turno_de_x(tablero):
                tablero[fila][col] = J1
            else:
                tablero[fila][col] = J2
            return True 
        
    return False
                  
def tablero_completo(tablero: List[List[str]]) -> bool:
    """Dado un tablero, indica si se encuentra completo. Un tablero se considera
    completo cuando no hay más espacio para insertar un nuevo símbolo, en tal
    caso la función devuelve `True`.

    PRECONDICIONES:
        - el parámetro `tablero` fue inicializado con la función `crear_tablero`
    """
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if ' ' in tablero[i][j]:
                return False
    return True
    
def obtener_ganador(tablero: List[List[str]]) -> str:
    """Dado un tablero, devuelve el símbolo que ganó el juego.
    El símbolo ganador estará dado por aquel que tenga un cuatro en línea. Es
    decir, por aquel símbolo que cuente con cuatro casilleros consecutivos
    alineados de forma horizontal, vertical, o diagonal.
    En el caso que el juego no tenga ganador, devuelve el símbolo vacío.
    En el caso que ambos símbolos cumplan con la condición de cuatro en línea,
    la función devuelve cualquiera de los dos.

    PRECONDICIONES:
        - el parámetro `tablero` fue inicializado con la función `crear_tablero`
    """
            
    return verificar_horizontal(tablero) or verificar_vertical(tablero) or verificar_diagonal_principal(tablero) or verificar_diagonal_secundaria(tablero) or NINGUNO

def verificar_horizontal(tablero: List[List[str]]) -> str:
    """Dado un tablero, devuelve el simbolo ganador de forma horizontal. Si los cuatro simbolos consecutivos son 'X' retorna X. Si son 'O' retorna 'O'.

    PRECONDICIONES:
        - el parámetro `tablero` fue inicializado con la función `crear_tablero`
    """
    for i in range(len(tablero)):
        for j in range(len(tablero[i]) - 3):
            if tablero[i][j] == tablero[i][j + 1] == tablero[i][j + 2] == tablero[i][j + 3] == J1:
                return J1
            if tablero[i][j] == tablero[i][j + 1] == tablero[i][j + 2] == tablero[i][j + 3] == J2:
                return J2
            
def verificar_vertical(tablero: List[List[str]]) -> str:
    """Dado un tablero, devuelve el simbolo ganador de forma vertical. Si los cuatro simbolos consecutivos son 'X' retorna X. Si son 'O' retorna 'O'.

    PRECONDICIONES:
        - el parámetro `tablero` fue inicializado con la función `crear_tablero`
    """
    for i in range(len(tablero) - 3):
        for j in range(len(tablero[i])):
            if tablero[i][j] == tablero[i + 1][j] == tablero[i + 2][j] == tablero[i + 3][j] == J1:
                return J1
            if tablero[i][j] == tablero[i + 1][j] == tablero[i + 2][j] == tablero[i + 3][j] == J2:
                return J2
            
def verificar_diagonal_principal(tablero: List[List[str]]) -> str:
    """Dado un tablero, devuelve el simbolo ganador de forma vertical. Si los cuatro simbolos consecutivos son 'X' retorna X. Si son 'O' retorna 'O'.

    PRECONDICIONES:
        - el parámetro `tablero` fue inicializado con la función `crear_tablero`
    """
    for i in range(len(tablero) - 3):
        for j in range(len(tablero[i])- 3):
            if tablero[i][j] == tablero[i + 1][j + 1] == tablero[i + 2][j + 2] == tablero[i + 3][j + 3] == J1:
                return J1
            if tablero[i][j] == tablero[i + 1][j + 1] == tablero[i + 2][j + 2] == tablero[i + 3][j + 3] == J2:
                return J2
            
def verificar_diagonal_secundaria(tablero: List[List[str]]) -> str:

    for i in range(len(tablero) - 3):
        for j in range(3, (len(tablero[i]))):
            if tablero[i][j] == tablero[i + 1][j - 1] == tablero[i + 2][j - 2] == tablero[i + 3][j - 3] == J1:
                return J1
            if tablero[i][j] == tablero[i + 1][j - 1] == tablero[i + 2][j - 2] == tablero[i + 3][j - 3] == J2:
                return J2
            