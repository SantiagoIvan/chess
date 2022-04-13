board1 = [ [ '*', 'q', '*', '*', 'k' ], [ '*', '*', '*', '*', '*' ], [ '*', '*', '*', '*', '*' ], [ '*', '*', '*', '*', '*' ], [ '*', '*', '*', '*', '*' ] ];
board2 = [ [ '*', '*', '*', '*', '*' ], [ '*', 'k', '*', 'q', '*' ], [ '*', '*', '*', '*', '*' ], [ '*', '*', '*', '*', '*' ], [ '*', '*', '*', '*', '*' ] ];
board3 = [ [ 'k', '*', '*', '*', '*' ], [ '*', '*', '*', '*', '*' ], [ 'q', '*', '*', '*', '*' ], [ '*', '*', '*', '*', '*' ], [ '*', '*', '*', '*', '*' ] ];
board4 = [ [ '*', 'q', '*', '*', '*' ], [ '*', '*', '*', '*', '*' ], [ '*', 'k', '*', '*', '*' ], [ '*', '*', '*', '*', '*' ], [ '*', '*', '*', '*', '*' ] ];
board5 = [ [ '*', 'k', '*', '*', '*' ], [ '*', '*', 'q', '*', '*' ], [ '*', '*', '*', '*', '*' ], [ '*', '*', '*', '*', '*' ], [ '*', '*', '*', '*', '*' ] ];
board6 = [ [ '*', '*', 'k', '*', '*' ], [ '*', 'q', '*', '*', '*' ], [ '*', '*', '*', '*', '*' ], [ '*', '*', '*', '*', '*' ], [ '*', '*', '*', '*', '*' ] ];
board7 = [ [ '*', '*', '*', 'q', '*' ], [ '*', '*', 'k', '*', '*' ], [ '*', '*', '*', '*', '*' ], [ '*', '*', '*', '*', '*' ], [ '*', '*', '*', '*', '*' ] ];
board8 = [ [ '*', '*', 'q', '*', '*' ], [ '*', '*', '*', 'k', '*' ], [ '*', '*', '*', '*', '*' ], [ '*', '*', '*', '*', '*' ], [ '*', '*', '*', '*', '*' ] ];

def get_piece(piece, board):
    for row in range(len(board)):
        for column in range(len(board[row])):
            if board[row][column] == piece:
                return (row, column)
    return None
    
    
def pieces_in_same_row(piece1, piece2):
    return piece1[0] == piece2[0]    

def pieces_in_same_column(piece1, piece2):
    return piece1[1] == piece2[1]

def pieces_in_same_diagonal(piece1, piece2):
    return abs(piece1[0]-piece2[0]) == abs(piece1[1]-piece2[1])

def check(board):
    queen = get_piece('q', board)
    king = get_piece('k', board)
    
    return True if pieces_in_same_row(queen, king) or pieces_in_same_column(queen, king) or pieces_in_same_diagonal(queen, king) else False
