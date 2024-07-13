def get_valid_moves(piece, position, positions):
    if piece.lower() == 'knight':
        return get_knight_moves(position, positions)
    elif piece.lower() == 'rook':
        return get_rook_moves(position, positions)
    elif piece.lower() == 'bishop':
        return get_bishop_moves(position, positions)
    elif piece.lower() == 'queen':
        return get_queen_moves(position, positions)
    else:
        return []

def get_knight_moves(position, positions):
    row, col = ord(position[0]), int(position[1])
    possible_moves = [(row+2, col+1), (row+2, col-1), (row-2, col+1), (row-2, col-1),
                      (row+1, col+2), (row+1, col-2), (row-1, col+2), (row-1, col-2)]
    valid_moves = []
    for r, c in possible_moves:
        if 'A' <= chr(r) <= 'H' and 1 <= c <= 8:
            target_pos = f"{chr(r)}{c}"
            if target_pos not in positions.values():
                valid_moves.append(target_pos)
    return valid_moves

def get_rook_moves(position, positions):
    row, col = ord(position[0]), int(position[1])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    return get_linear_moves(row, col, directions, positions)

def get_bishop_moves(position, positions):
    row, col = ord(position[0]), int(position[1])
    directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    return get_linear_moves(row, col, directions, positions)

def get_queen_moves(position, positions):
    row, col = ord(position[0]), int(position[1])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    return get_linear_moves(row, col, directions, positions)

def get_linear_moves(row, col, directions, positions):
    valid_moves = []
    for dr, dc in directions:
        r, c = row + dr, col + dc
        while 'A' <= chr(r) <= 'H' and 1 <= c <= 8:
            target_pos = f"{chr(r)}{c}"
            if target_pos in positions.values():
                valid_moves.append(target_pos)
                break
            valid_moves.append(target_pos)
            r += dr
            c += dc
    return valid_moves
