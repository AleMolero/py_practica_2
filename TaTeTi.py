from random import randrange


# -------------------------------------------------------
def DisplayBoard(board):
    # La función acepta un parámetro el cual contiene el estado actual del tablero
    # y lo muestra en la consola.
    # imprime tablero
    for j in range(13):  # cambiar 13 por generico
        for i in range(len(board[j])):
            print(board[j][i], end="")
        print("")


# -------------------------------------------------------
def EnterMove(board):
    # La función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento,
    # verifica la entrada y actualiza el tablero acorde a la decisión del usuario.
    seguir = True
    while seguir:
        jugada = input("Ingrese el numero del casillero de su siguiente jugada: ")
        casilleros = casilleros_coord()
        libres = MakeListOfFreeFields(board)
        if jugada in casilleros.keys() and casilleros[jugada] in libres:
            board[casilleros[jugada][0]][casilleros[jugada][1]] = "O"
            # print (casilleros[jugada])
            # print (libres)
            seguir = False
            DisplayBoard(board)
        else:
            print("No ha ingresado un valor válido ")


# -------------------------------------------------------
def MakeListOfFreeFields(board):
    # La función examina el tablero y construye una lista de todos los cuadros vacíos.
    # La lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna.
    libres = []
    for g in range(3):
        for p in range(3):
            if board[2 + g * 4][4 + p * 8].isnumeric():
                libres.append((2 + g * 4, 4 + p * 8))
    return libres


# -------------------------------------------------------
def verificar_trio(sign, list):
    trio = sign * 3
    return trio in list


# -------------------------------------------------------
def victory_for(board, sign):
    # La función analiza el estatus del tablero para verificar si
    # el jugador que utiliza las 'O's o las 'X's ha ganado el juego.
    lin = []
    for g in range(3):
        lin.append("")
        for p in range(3):
            lin[g] += board[2 + g * 4][4 + p * 8]
    if verificar_trio(sign, lin):
        return True
    col = []
    for g in range(3):
        col.append("")
        for p in range(3):
            col[g] += board[2 + p * 4][4 + g * 8]
    if verificar_trio(sign, col):
        return True
    diag = []
    diag.append("")
    for p in range(3):
        diag[0] += board[2 + p * 4][4 + p * 8]
    diag.append("")
    for p in range(3):
        diag[1] += board[10 - p * 4][4 + p * 8]
    if verificar_trio(sign, diag):
        return True


# -------------------------------------------------------
def draw_move(board):
    # La función dibuja el movimiento de la máquina y actualiza el tablero.
    seguir = True
    while seguir:
        jugada = str(randrange(9) + 1)
        casilleros = casilleros_coord()
        libres = MakeListOfFreeFields(board)
        if casilleros[jugada] in libres:
            board[casilleros[jugada][0]][casilleros[jugada][1]] = "X"
            seguir = False
            DisplayBoard(board)


# -------------------------------------------------------
def casilleros_coord():
    casilleros = {}
    n = 1
    for g in range(3):
        for p in range(3):
            casilleros[str(n)] = (2 + g * 4, 4 + p * 8)
            n += 1
    return casilleros


# -------------------------------------------------------
def generar_linea(interseccion, medio):
    linea = []
    for i in range(3):
        linea.append(interseccion)
        for j in range(7):
            linea.append(medio)
    linea.append(interseccion)
    return linea


# -------------------------------------------------------
def generar_tablero_inicial():
    board = []
    linea_h = generar_linea("+", "-")
    linea_v = generar_linea("|", " ")
    # crea tablero
    board.append(linea_h)
    for i in range(3):
        for j in range(3):
            nueva = linea_v[:]
            board.append(nueva)
        board.append(linea_h)
    n = 1
    for g in range(3):
        for p in range(3):
            board[2 + g * 4][4 + p * 8] = str(n)
            n += 1
    return board


# ---PROGRAMA-------------------------------------------------
board = generar_tablero_inicial()
print("EMPECEMOS! ")
DisplayBoard(board)
print("1° mi turno ")
board[6][12] = "X"
DisplayBoard(board)

n = 0
continuar = True
while n < 4 and continuar:
    print("")
    print((n + 1), "° tu turno ")
    EnterMove(board)
    if victory_for(board, "O"):
        print("Has GANADO! :)")
        continuar = False
    if continuar:
        print("")
        print((n + 2), "° mi turno ")
        draw_move(board)
        if victory_for(board, "X"):
            print("Has Perdido! :(")
            continuar = False
        n += 1
if continuar:
    print(" Empatamos...")
