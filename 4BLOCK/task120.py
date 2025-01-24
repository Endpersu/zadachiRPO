def can_move_without_check(white_piece, black_piece, a, b, c, d, e, f):
    def is_under_attack(px, py, qx, qy, piece):
        if piece == 'rook':
            return px == qx or py == qy
        elif piece == 'bishop':
            return abs(px - qx) == abs(py - qy)
        elif piece == 'queen':
            return (px == qx or py == qy) or (abs(px - qx) == abs(py - qy))
        elif piece == 'knight':
            return (abs(px - qx), abs(py - qy)) in [(2, 1), (1, 2)]
        elif piece == 'king':
            return max(abs(px - qx), abs(py - qy)) == 1
        return False

    if white_piece == 'rook':
        if not is_under_attack(e, f, c, d, black_piece) and (a == e or b == f):
            return True
    elif white_piece == 'bishop':
        if not is_under_attack(e, f, c, d, black_piece) and abs(
            a - e) == abs(b - f):
            return True
    elif white_piece == 'queen':
        if not is_under_attack(e, f, c, d, black_piece) and (
            a == e or b == f or abs(a - e) == abs(b - f)):
            return True
    elif white_piece == 'knight':
        if not is_under_attack(e, f, c, d, black_piece) and (
            abs(a - e), abs(b - f)) in [(2, 1), (1, 2)]:
            return True
    elif white_piece == 'king':
        if not is_under_attack(e, f, c, d, black_piece) and max(abs(a - e), abs(b - f)) == 1:
            return True

    return False


a, b = 1, 1
c, d = 2, 2
e, f = 3, 1


combinations = [
    ('rook', 'rook'),
    ('rook', 'queen'),
    ('rook', 'knight'),
    ('rook', 'bishop'),
    ('queen', 'queen'),
    ('queen', 'rook'),
    ('queen', 'knight'),
    ('queen', 'bishop'),
    ('knight', 'knight'),
    ('knight', 'rook'),
    ('knight', 'queen'),
    ('knight', 'bishop'),
    ('bishop', 'bishop'),
    ('bishop', 'queen'),
    ('bishop', 'knight'),
    ('bishop', 'rook'),
    ('king', 'bishop'),
    ('king', 'queen'),
    ('king', 'knight'),
    ('king', 'rook'),
]

for white_piece, black_piece in combinations:
    result = can_move_without_check(white_piece, black_piece, a, b, c, d, e, f)
    print(f"Белая фигура: {white_piece}, Черная фигура: {black_piece} -> {'Может' if result else 'Не может'}")
