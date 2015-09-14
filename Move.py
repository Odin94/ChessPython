
class Move():
    def __init__(self, piece, new_pos, captured_piece = None):
        self.piece = piece
        self.old_pos = (piece.board_x, piece.board_y)
        self.new_pos = new_pos

        self.captured_piece = captured_piece

    def execute(self, white_pieces, black_pieces, lost_pieces):
        self.piece.board_x = self.new_pos[0]
        self.piece.board_y = self.new_pos[1]

        if self.captured_piece:
            print("ha, gotteem")
            lost_pieces.append(self.captured_piece)
            self.captured_piece.captured = True

            try:
                black_pieces.remove(self.captured_piece) # delete piece here if it was black
            except: # whoops, piece was white
                white_pieces.remove(self.captured_piece) # delete piece here if it was white

    def reverse(self, white_pieces, black_pieces, lost_pieces):
        self.piece.board_x = self.old_pos[0]
        self.piece.board_y = self.old_pos[1]

        if self.captured_piece:
            lost_pieces.remove(self.captured_piece)
            self.captured_piece.captured = False

            if self.captured_piece.team_color == "black":
                black_pieces.append(self.captured_piece) # append piece here if it was black
            elif self.captured_piece.team_color == "white":
                white_pieces.append(self.captured_piece) # append piece here if it was white
