
class Move():
    def __init__(self, piece, new_pos, captured_piece = None):
        self.piece = piece
        self.old_pos = (piece.board_x, piece.board_y)
        self.new_pos = new_pos

        self.captured_piece = captured_piece

    def execute(self, white_pieces, black_pieces, lost_pieces):
        self.piece.move_history.append(self)

        self.piece.board_x = self.new_pos[0]
        self.piece.board_y = self.new_pos[1]

        if self.captured_piece:
            lost_pieces.append(self.captured_piece)
            self.captured_piece.captured = True

            try:
                black_pieces.remove(self.captured_piece) # delete piece here if it was black
            except: # whoops, piece was white
                white_pieces.remove(self.captured_piece) # delete piece here if it was white

    def reverse(self, white_pieces, black_pieces, lost_pieces):
        self.piece.move_history.remove(self)

        self.piece.board_x = self.old_pos[0]
        self.piece.board_y = self.old_pos[1]

        if self.captured_piece:
            lost_pieces.remove(self.captured_piece)
            self.captured_piece.captured = False

            if self.captured_piece.team_color == "black":
                black_pieces.append(self.captured_piece) # append piece here if it was black
            elif self.captured_piece.team_color == "white":
                white_pieces.append(self.captured_piece) # append piece here if it was white


class Castling(Move): # doesn't call any super methods or anything but still kinda is a move.. Is inheritance a good idea here?
    def __init__(self, king, new_board_x, rook):
        self.piece = king
        self.rook = rook
        self.new_board_x = new_board_x

        self.old_board_x = king.board_x

    def execute(self, white_pieces, black_pieces, lost_pieces): # arguments are not actually needed, but this method should be callable the same way Move.execute can be called
        self.piece.move_history.append(self)

        if self.piece.board_x < self.new_board_x:
            self.rook.board_x = self.new_board_x - 1
        else:
            self.rook.board_x = self.new_board_x + 1

        self.piece.board_x = self.new_board_x

    def reverse(self, white_pieces, black_pieces, lost_pieces):
        self.piece.move_history.remove(self)

        if self.old_board_x.board_x < self.piece.board_x:
            self.rook.board_x = self.piece.board_x - 1
        else:
            self.rook.board_x = self.piece.board_x + 1

        self.piece.board_x = self.old_board_x


