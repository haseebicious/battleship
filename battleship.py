import layout

def initialize_board():
    """Initializes the board with water markers."""
    return [[layout.marker.water for _ in range(layout.columns)]
            for _ in range(layout.rows)]

def print_board(board):
    """Prints the board with decorations."""
    separator = layout.board.corner + (layout.board.top + layout.board.corner) * layout.columns

    for row in board:
        print(separator)
        row_str = layout.board.side
        for cell in row:
             row_str += cell + layout.board.side
        print(row_str)

    print(separator)

def main():
    board = initialize_board()
    print_board(board)

if __name__ == "__main__":
    main()
