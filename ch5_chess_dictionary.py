pieces = 16
valid_positions = ('a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8',
                   'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8',
                   'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8',
                   'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8',
                   'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8',
                   'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8',
                   'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8',
                   'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8')
all_pieces = {'wking': '', 'wqueen': '', 'wbishop': '', 'wrook': '', 'wknight': '', 'wpawns': '',
              'bking': '', 'bqueen': '', 'bbishop': '', 'brook': '', 'bknight': '', 'bpawns': ''}
all_positions = {'a1': '', 'a2': '', 'a3': '', 'a4': '', 'a5': '', 'a6': '', 'a7': '', 'a8': '',
                 'b1': '', 'b2': '', 'b3': '', 'b4': '', 'b5': '', 'b6': '', 'b7': '', 'b8': '',
                 'c1': '', 'c2': '', 'c3': '', 'c4': '', 'c5': '', 'c6': '', 'c7': '', 'c8': '',
                 'd1': '', 'd2': '', 'd3': '', 'd4': '', 'd5': '', 'd6': '', 'd7': '', 'd8': '',
                 'e1': '', 'e2': '', 'e3': '', 'e4': '', 'e5': '', 'e6': '', 'e7': '', 'e8': '',
                 'f1': '', 'f2': '', 'f3': '', 'f4': '', 'f5': '', 'f6': '', 'f7': '', 'f8': '',
                 'g1': '', 'g2': '', 'g3': '', 'g4': '', 'g5': '', 'g6': '', 'g7': '', 'g8': '',
                 'h1': '', 'h2': '', 'h3': '', 'h4': '', 'h5': '', 'h6': '', 'h7': '', 'h8': ''}


def isvalidchessboard(chess_board, positions):
    if chess_board['wking'] <= 1:
        pass
    else:
        print('invalid number of White Kings')
        return False
    if chess_board['wqueen'] <= 1:
        pass
    else:
        print('invalid number of White Queens')
        return False
    if chess_board['wbishop'] <= 2:
        pass
    else:
        print('invalid number of White Bishops')
        return False
    if chess_board['wrook'] <= 2:
        pass
    else:
        print('invalid number of White Rooks')
        return False
    if chess_board['wknight'] <= 2:
        pass
    else:
        print('invalid number of White Knights')
        return False
    if chess_board['wpawns'] <= 8:
        pass
    else:
        print('invalid number of White Pawns')
        return False
    if chess_board['wking'] + chess_board['wqueen'] + chess_board['wbishop'] + chess_board['wrook'] + chess_board['wknight'] + chess_board['wpawns'] <= pieces:
        pass
    else:
        print('invalid number of pieces')
        return False
    if chess_board['bking'] <= 1:
        pass
    else:
        print('invalid number of Black Kings')
        return False
    if chess_board['bqueen'] <= 1:
        pass
    else:
        print('invalid number of Black Queens')
        return False
    if chess_board['bbishop'] <= 2:
        pass
    else:
        print('invalid number of Black Bishops')
        return False
    if chess_board['brook'] <= 2:
        pass
    else:
        print('invalid number of Black Brooks')
        return False
    if chess_board['bknight'] <= 2:
        pass
    else:
        print('invalid number of Black Knights')
        return False
    if chess_board['bpawns'] <= 8:
        pass
    else:
        print('invalid number of Black Pawns')
        return False
    if chess_board['bking'] + chess_board['bqueen'] + chess_board['bbishop'] + chess_board['brook'] + chess_board['bknight'] + chess_board['bpawns'] <= pieces:
        pass
    else:
        print('invalid number of pieces')
        return False
    return True


all_pieces['wking'] = int(input('Number of White Kings: '))
for i in range(all_pieces['wking']):
    wking_p = input('White King Position: ')
    if wking_p not in valid_positions:
        print('Invalid position')
        exit()
    if all_positions[wking_p] != 'x':
        all_positions[wking_p] = 'x'
    else:
        print('occupied position')
        exit()
all_pieces['wqueen'] = int(input('Number of White Queens: '))
for i in range(all_pieces['wqueen']):
    wqueen_p = input('White Queen Position: ')
    if wqueen_p not in valid_positions:
        print('Invalid position')
        exit()
    if all_positions[wqueen_p] != 'x':
        all_positions[wqueen_p] = 'x'
    else:
        print('occupied position')
        exit()
all_pieces['wbishop'] = int(input('Number of White Bishops: '))
for i in range(all_pieces['wbishop']):
    wbishops_p = input('White Bishop Position: ')  # multiple
    if wbishops_p not in valid_positions:
        print('Invalid position')
        exit()
    if all_positions[wbishops_p] != 'x':
        all_positions[wbishops_p] = 'x'
    else:
        print('occupied position')
        exit()
all_pieces['wrook'] = int(input('Number of White Rooks: '))
for i in range(all_pieces['wrook']):
    wrooks_p = input('White Rooks Position: ')  # multiple
    if wrooks_p not in valid_positions:
        print('Invalid position')
        exit()
    if all_positions[wrooks_p] != 'x':
        all_positions[wrooks_p] = 'x'
    else:
        print('occupied position')
        exit()
all_pieces['wknight'] = int(input('Number of White Knights: '))
for i in range(all_pieces['wknight']):
    wknights_p = input('White Knights Position: ')  # multiple
    if wknights_p not in valid_positions:
        print('Invalid position')
        exit()
    if all_positions[wknights_p] != 'x':
        all_positions[wknights_p] = 'x'
    else:
        print('occupied position')
        exit()
all_pieces['wpawns'] = int(input('Number of White Pawns: '))
for i in range(all_pieces['wpawns']):
    wpawns_p = input('White Pawns Position: ')  # multiple
    if wpawns_p not in valid_positions:
        print('Invalid position')
        exit()
    if all_positions[wpawns_p] != 'x':
        all_positions[wpawns_p] = 'x'
    else:
        print('occupied position')
        exit()
all_pieces['bking'] = int(input('Number of Black Kings: '))
for i in range(all_pieces['bking']):
    bking_p = input('Black King Position: ')  # multiple
    if bking_p not in valid_positions:
        print('Invalid position')
        exit()
    if all_positions[bking_p] != 'x':
        all_positions[bking_p] = 'x'
    else:
        print('occupied position')
        exit()
all_pieces['bqueen'] = int(input('Number of Black Queens: '))
for i in range(all_pieces['bqueen']):
    bqueen_p = input('Black Queen Position: ')  # multiple
    if bqueen_p not in valid_positions:
        print('Invalid position')
        exit()
    if all_positions[bqueen_p] != 'x':
        all_positions[bqueen_p] = 'x'
    else:
        print('occupied position')
        exit()
all_pieces['bbishop'] = int(input('Number of Black Bishops: '))
for i in range(all_pieces['bbishop']):
    bbishops_p = input('Black Bishop Position: ')  # multiple
    if bbishops_p not in valid_positions:
        print('Invalid position')
        exit()
    if all_positions[bbishops_p] != 'x':
        all_positions[bbishops_p] = 'x'
    else:
        print('occupied position')
        exit()
all_pieces['brook'] = int(input('Number of Black Rooks: '))
for i in range(all_pieces['brook']):
    brooks_p = input('Black Rooks Position: ')  # multiple
    if brooks_p not in valid_positions:
        print('Invalid position')
        exit()
    if all_positions[brooks_p] != 'x':
        all_positions[brooks_p] = 'x'
    else:
        print('occupied position')
        exit()
all_pieces['bknight'] = int(input('Number of Black Knights: '))
for i in range(all_pieces['bknight']):
    bknights_p = input('Black Knights Position: ')  # multiple
    if bknights_p not in valid_positions:
        print('Invalid position')
        exit()
    if all_positions[bknights_p] != 'x':
        all_positions[bknights_p] = 'x'
    else:
        print('occupied position')
        exit()
all_pieces['bpawns'] = int(input('Number of Black Pawns: '))
for i in range(all_pieces['bpawns']):
    bpawns_p = input('Black Pawns Position: ')  # multiple
    if bpawns_p not in valid_positions:
        print('Invalid position')
        exit()
    if all_positions[bpawns_p] != 'x':
        all_positions[bpawns_p] = 'x'
    else:
        print('occupied position')
        exit()

print(all_pieces)
print(all_positions)

isvalidchessboard(all_pieces, all_positions)

# get positions and store them
# occupied space
