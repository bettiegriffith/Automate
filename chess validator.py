#In this chapter, we used the dictionary value {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'} to represent a chess board. 
#Write a function named isValidChessBoard() that takes a dictionary argument and returns True or False depending on if the board is valid.
#A valid board will have exactly one black king and exactly one white king. 
#Each player can only have at most 16 pieces, at most 8 pawns, and all pieces must be on a valid space from '1a' to '8h'; that is, a piece can’t be on space '9z'. 
#The piece names begin with either a 'w' or 'b' to represent white or black, followed by 'pawn', 'knight', 'bishop', 'rook', 'queen', or 'king'. 
#This function should detect when a bug has resulted in an improper chess board.

def isValidChessBoard(board):
    count = {}
    for i in board.values():
        count.setdefault(i, 0)
        count[i] = count[i] + 1
    if count['bking'] == 1 and count['wking'] == 1 and count.get('wpawn', 0) <= 8 \
        and count.get('bpawn', 0) <= 8:
        print('True')
    else:
        print('False')
    print(count)

    spaceList = ['1a', '1b', '1c', '1d', '1e', '1f', '1g', '1h', \
    '2a', '2b', '2c', '2d', '2e', '2f', '2g', '2h', \
    '3a', '3b', '3c', '3d', '3e', '3f', '3g', '3h', \
    '4a', '4b', '4c', '4d', '4e', '4f', '4g', '4h', \
    '5a', '5b', '5c', '5d', '5e', '5f', '5g', '5h', \
    '6a', '6b', '6c', '6d', '6e', '6f', '6g', '6h', \
    '7a', '7b', '7c', '7d', '7e', '7f', '7g', '7h', \
    '8a', '8b', '8c', '8d', '8e', '8f', '8g', '8h']
    for spaceList not in board.keys():
        print('Off board.')

aBoard = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking', \
    '7g': 'wpawn', '7a': 'wpawn', '7b': 'wpawn', '7c': 'wpawn', '7d': 'wpawn', '7e': 'wpawn', '7f': 'wpawn', '7h': 'wpawn'}

isValidChessBoard(aBoard)
