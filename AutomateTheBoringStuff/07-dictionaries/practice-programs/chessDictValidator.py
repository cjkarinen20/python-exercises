def isValidChessBoard(chessboard):
    
    
    # Define Pieces and Colors
    pieces = ['king', 'queen', 'rook', 'knight', 'bishop', 'pawn']
    colors = ['b', 'w']
    
    # Create a set of all the pieces
    
    all_pieces = set(color+piece for piece in pieces for color in colors)
    
    # Define valid range for piece counts 
    valid_counts = {'king': (1, 1), 'queen': (0, 1), 'rook': (0, 2), 'bishop': (0, 2), 'knight': (0, 2), 'pawn': (0, 8)}
    
    # Count the pieces on the board
    piece_count = {}
    for v in chessboard.values():
        if v in all_pieces:
            piece_count.setdefault(v, 0)
            piece_count[v] += 1
    
    # Check if there are a valid number of pieces
    for piece in all_pieces:
        count = piece_count.get(piece, 0)
        low, high = valid_counts[piece[1:]]
        if not low <= count <= high: # Count needs to be between high and low
            if low != high:
                print(f"There should be between {low} and {high} {piece} but there are {count}")
            else: 
                print(f"There should be {low} {piece} but there are {count}")
            return False
    
    # Check if locations are valid 
    for location in chessboard.keys():
        row = int(location[:1])
        column = location[1:]
        if not ((1 <= row <= 8) and ('a' <= column <= "h")):
            print(f"Invalid to have {chessboard[location]} at position {location}")
            return False
    
    # Check if all pieces have valid names
    for loc, piece in chessboard.items():
        if piece:
            if not piece in all_pieces:
                print(f"{piece} is not a valid chess piece at position {loc}")
                return False
            
    return True