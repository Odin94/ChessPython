import pygame
import Utils

from Graphics import screen, offset

class Piece():
    def __init__(self, team_color, board_x, board_y, w, h, surface):
        self.team_color = team_color

        self.board_x = board_x
        self.board_y = board_y
        self.w = w
        self.h = h

        self.captured = False

        self.surface = surface

    def draw(self, xoffset = 0): # xoffset is used for captured pieces only
        if not self.captured:
            screen.blit(self.surface, (offset[0] + self.board_x*self.w, offset[1] + self.board_y*self.h))
        else: # draw on the side of the board because the piece was captured
            screen.blit(self.surface, (offset[0] + xoffset + 8*self.w, offset[1] + self.board_y*self.h))


    def mouse_on_piece(self, mouse_pos):
        rx = self.board_x * self.w + offset[0]
        ry = self.board_y * self.h + offset[1]

        return Utils.point_in_rect(mouse_pos, (rx, ry, self.w, self.h))


class Pawn(Piece):
    def __init__(self, team_color, board_x, board_y, w, h, surface): #x & y are Chessboard coordinates here!
        super().__init__(team_color, board_x, board_y, w, h, surface)

    def get_possible_moves(self, board):
        moves = []

        #two steps forward
        if self.team_color == "black" and self.board_y == 6 and board[self.board_x][self.board_y-2].occupying_piece == None: #board[self.board_x][self.board_y-2] should only get checked if board_y == 6 so this shouldnt ever go off board
            moves.append((self.board_x, self.board_y-2))

        elif self.team_color == "white" and self.board_y == 1 and board[self.board_x][self.board_y+2].occupying_piece == None: 
            moves.append((self.board_x, self.board_y+2))

        #one step forward
        try:
            if self.team_color == "black" and board[self.board_x][self.board_y-1].occupying_piece == None: #try: because "self.board_y-1" could be off-board
                moves.append((self.board_x, self.board_y-1))

            elif self.team_color == "white" and board[self.board_x][self.board_y+1].occupying_piece == None:
                moves.append((self.board_x, self.board_y+1))
        except (IndexError, AttributeError) as e: # IndexError if the piece is at the border of the board and e.g. board_x+1 doesnt exist, Attribute if occupying_piece is None
            #print(e)
            pass

        #one step diagonally right
        try:
            if self.team_color == "black" and board[self.board_x+1][self.board_y-1].occupying_piece.team_color != self.team_color:
                moves.append((self.board_x+1, self.board_y-1))

            elif self.team_color == "white" and board[self.board_x+1][self.board_y+1].occupying_piece.team_color != self.team_color:
                moves.append((self.board_x+1, self.board_y+1))
        except (IndexError, AttributeError) as e:
            #print(e)
            pass

        #one step diagonally left
        try:
            if self.team_color == "black" and board[self.board_x-1][self.board_y-1].occupying_piece.team_color != self.team_color:
                moves.append((self.board_x-1, self.board_y-1))

            elif self.team_color == "white" and board[self.board_x-1][self.board_y+1].occupying_piece.team_color != self.team_color:
                moves.append((self.board_x-1, self.board_y+1))
        except (IndexError, AttributeError) as e:
            #print(e)
            pass

        return moves


