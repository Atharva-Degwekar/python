class Color:
    BLACK = "Black"
    WHITE = "White"


class Piece:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def is_valid_move(self, start_row, start_col, end_row, end_col, board):
        raise NotImplementedError("This method should be overridden by subclasses")


class Pawn(Piece):
    def is_valid_move(self, start_row, start_col, end_row, end_col, board):
        direction = -1 if self.color == Color.WHITE else 1

        # Move one step forward
        if start_col == end_col:
            if end_row == start_row + direction and board.get_piece(end_row, end_col) is None:
                return True

            # Move two steps forward on first move
            if (start_row == 1 and self.color == Color.BLACK) or (start_row == 6 and self.color == Color.WHITE):
                if end_row == start_row + 2 * direction and board.get_piece(end_row, end_col) is None and board.get_piece(start_row + direction, start_col) is None:
                    return True

        # Capture diagonally
        if abs(start_col - end_col) == 1 and end_row == start_row + direction:
            target = board.get_piece(end_row, end_col)
            return target is not None and target.get_color() != self.color

        return False


class Knight(Piece):
    def is_valid_move(self, start_row, start_col, end_row, end_col, board):
        row_diff = abs(start_row - end_row)
        col_diff = abs(start_col - end_col)
        return (row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2)


class Bishop(Piece):
    def is_valid_move(self, start_row, start_col, end_row, end_col, board):
        if abs(start_row - end_row) == abs(start_col - end_col):
            return board.is_path_clear(start_row, start_col, end_row, end_col)
        return False


class Rook(Piece):
    def is_valid_move(self, start_row, start_col, end_row, end_col, board):
        if start_row == end_row or start_col == end_col:
            return board.is_path_clear(start_row, start_col, end_row, end_col)
        return False


class Queen(Piece):
    def is_valid_move(self, start_row, start_col, end_row, end_col, board):
        return Bishop(self.color).is_valid_move(start_row, start_col, end_row, end_col, board) or \
               Rook(self.color).is_valid_move(start_row, start_col, end_row, end_col, board)


class King(Piece):
    def is_valid_move(self, start_row, start_col, end_row, end_col, board):
        return abs(start_row - end_row) <= 1 and abs(start_col - end_col) <= 1


class ChessBoard:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.initialize_board()

    def initialize_board(self):
        for i in range(8):
            self.board[1][i] = Pawn(Color.BLACK)
            self.board[6][i] = Pawn(Color.WHITE)

        self.board[0][0] = self.board[0][7] = Rook(Color.BLACK)
        self.board[0][1] = self.board[0][6] = Knight(Color.BLACK)
        self.board[0][2] = self.board[0][5] = Bishop(Color.BLACK)
        self.board[0][3] = Queen(Color.BLACK)
        self.board[0][4] = King(Color.BLACK)

        self.board[7][0] = self.board[7][7] = Rook(Color.WHITE)
        self.board[7][1] = self.board[7][6] = Knight(Color.WHITE)
        self.board[7][2] = self.board[7][5] = Bishop(Color.WHITE)
        self.board[7][3] = Queen(Color.WHITE)
        self.board[7][4] = King(Color.WHITE)

    def get_piece(self, row, col):
        return self.board[row][col]

    def is_path_clear(self, start_row, start_col, end_row, end_col):
        row_step = 1 if end_row > start_row else -1 if end_row < start_row else 0
        col_step = 1 if end_col > start_col else -1 if end_col < start_col else 0

        row, col = start_row + row_step, start_col + col_step
        while row != end_row or col != end_col:
            if self.get_piece(row, col) is not None:
                return False
            row += row_step
            col += col_step
        return True

    def move_piece(self, start_row, start_col, end_row, end_col):
        piece = self.get_piece(start_row, start_col)
        if piece is None:
            print("No piece at the starting position!")
            return False

        if piece.is_valid_move(start_row, start_col, end_row, end_col, self):
            target_piece = self.get_piece(end_row, end_col)
            if target_piece is None or target_piece.get_color() != piece.get_color():
                self.board[end_row][end_col] = piece
                self.board[start_row][start_col] = None
                print(f"Moved {piece.__class__.__name__} to ({end_row}, {end_col})")
                return True
            else:
                print("Cannot capture your own piece!")
        else:
            print("Invalid move!")

        return False

    def __str__(self):
        board_str = ""
        for row in self.board:
            board_str += " | ".join([p.__class__.__name__[0] if p else "." for p in row]) + "\n"
        return board_str


if __name__ == "__main__":
    board = ChessBoard()
    print("Initial Board:")
    print(board)

    # Example Moves
    board.move_piece(1, 4, 3, 4)  # Move Pawn forward
    print(board)

    board.move_piece(0, 1, 2, 2)  # Move Knight
    print(board)

    board.move_piece(1, 3, 3, 3)  # Move Pawn forward
    print(board)

    board.move_piece(0, 3, 4, 7)  # Invalid move
    print(board)

    board.move_piece(0, 3, 4, 3)  # Move Queen
    print(board)

    board.move_piece(4, 3, 4, 7)  # Capture
    print(board)

    board.move_piece(7, 2, 5, 4)  # Move Bishop
    print(board)