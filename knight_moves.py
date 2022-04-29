#[
#    [ '0', '0', '0', '0', '0', '0', '0', '0' ],
#    [ '0', '0', '0', '0', '0', '0', '0', '0' ],
#    [ '0', '0', '0', '0', '0', 'K', '0', '0' ],
#    [ '0', '0', '0', '0', '0', '0', '0', 'I' ],
#    [ '0', '0', '0', '0', '0', '0', '0', '0' ],
#    [ '0', '0', 'V', '0', '0', 'O', '0', '0' ],
#    [ '0', '0', '0', '0', '0', '0', '0', '0' ],
#    [ '0', '0', '0', '0', '0', '0', '0', '0' ]
#]

# Esa V seria una posicion valida final, para tener como ejemplo.
# La idea del enunciado es, dada un caballo y una posicion inicial
# retornar si es posible pasar por todos los casilleros, sin repetir los ya visitados

# pos = (row, col)

# Otra forma de saber si esta completo es usando la variable global moves.
# Yo se que para completar el tablero tengo que hacer 64 movimientos (incluyendo al movimiento inicial)
# esto es para no volver a revisar el tablero en cada iteracion


def valid_position(pos, chessboard):
    return pos[0] in range(0,len(chessboard)) and pos[1] in range(0, len(chessboard)) and chessboard[pos[0]][pos[1]] != 'K'

def is_board_completed(chessboard, moves):
    #for i in range(0,8):
    #    for j in range(0,8):
    #        if chessboard[i][j] == 'O': return False
    return moves == (len(chessboard) ** 2)

def move_up_right(row, col):
    return (row-2, col+1) 

def move_up_left(row, col):
    return (row-2, col-1)

def move_left_up(row, col):
    return (row-1, col-2)

def move_left_down(row, col):
    return (row+1, col-2)

def move_down_left(row, col):
    return (row+2, col-1)

def move_down_right(row, col):
    return (row+2, col+1)

def move_right_down(row, col):
    return (row+1, col+2)

def move_right_up(row, col):
    return (row-1, col+2)


# me muevo en cada direccion existente, preguntando el valor de retorno
# si devuelvo None, es porque no tengo solucion por ese lugar, e intento con otro
# si todos me devuelven None, retorno None, dejando un lugar en blanco en mi posicion

# Si existe solucion, retorno True, si no existe, retorno False.
# Como el tablero lo puse en una variable global, no haria falta retornar el tablero, puedo printearlo luego de procesarlo.

def can_complete_chessboard_with_knight(current_pos, chessboard, moves):
    if not valid_position(current_pos, chessboard):
        return None
    (row, col) = current_pos
    
    # Como mi posicion es valida, pongo una K en mi lugar
    chessboard[row][col] = 'K'
    moves += 1
    
    # Pregunto si el tablero esta completo, si esta completo, retorno al tablero, y sino, me muevo
    if is_board_completed(chessboard, moves): return True
    
    # Ahora invoco esta misma funcion, pero moviendome en todas las direcciones posibles
    if( can_complete_chessboard_with_knight(move_up_right(row, col), chessboard, moves) 
       or can_complete_chessboard_with_knight(move_up_left(row, col), chessboard, moves) 
       or can_complete_chessboard_with_knight(move_left_up(row, col), chessboard, moves) 
       or can_complete_chessboard_with_knight(move_left_down(row, col), chessboard, moves) 
       or can_complete_chessboard_with_knight(move_down_left(row, col), chessboard, moves) 
       or can_complete_chessboard_with_knight(move_down_right(row, col), chessboard, moves) 
       or can_complete_chessboard_with_knight(move_right_down(row, col), chessboard, moves) 
       or can_complete_chessboard_with_knight(move_right_up(row, col), chessboard, moves)): return True
    
    # si no pude completar el tablero, pongo un O en mi lugar y retorno False
    chessboard[row][col] = 'O'
    moves -= 1
    return False

total_moves = 0
board = [
    [ '0', '0', '0', '0', '0', '0', '0', '0' ],
    [ '0', '0', '0', '0', '0', '0', '0', '0' ],
    [ '0', '0', '0', '0', '0', 'O', '0', '0' ],
    [ '0', '0', '0', '0', '0', '0', '0', 'O' ],
    [ '0', '0', '0', '0', '0', '0', '0', '0' ],
    [ '0', '0', 'O', '0', '0', 'O', '0', '0' ],
    [ '0', '0', '0', '0', '0', '0', '0', '0' ],
    [ '0', '0', '0', '0', '0', '0', '0', '0' ]
]

print(can_complete_chessboard_with_knight((2,5), board, total_moves))
