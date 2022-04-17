[ [ '0', '0', '0', '0', '0', '0', '0', '0' ],
  [ '0', '0', '0', '0', '0', '0', '0', '0' ],
  [ '0', '0', '0', '0', '0', 'K', '0', '0' ],
  [ '0', '0', '0', '0', '0', '0', '0', 'I' ],
  [ '0', '0', '0', '0', '0', '0', '0', '0' ],
  [ '0', '0', 'V', '0', '0', '0', '0', '0' ],
  [ '0', '0', '0', '0', '0', '0', '0', '0' ],
  [ '0', '0', '0', '0', '0', '0', '0', '0' ] ]
  
# La idea del enunciado es, dada un caballo y una posicion inicial
# retornar si es posible pasar por todos los casilleros, sin repetir los ya visitados

# pos = (row, col)

def valid_position(pos):
    return pos[0] in range(0,10) and pos[1] in range(0, 10)
    
def can_complete_with_knight(current_pos):
    if not valid_position(current_pos):
        return False
    # me muevo en cada direccion existente, preguntando el valor de retorno
    # si devuelvo false, es porque no tengo solucion por ese lugar, e intento con otro
    # si todos me devuelven False, retorno False
    pass
  
  
print("In progress...")
