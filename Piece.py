import pygame
import Utils

from Graphics import screen, offset

class Piece():
    def __init__(self, team, board_x, board_y, w, h, surface):
        self.team = team

        self.board_x = board_x
        self.board_y = board_y
        self.w = w
        self.h = h

        self.surface = surface

    def draw(self):
        screen.blit(self.surface, (offset[0] + self.board_x*self.w, offset[1] + self.board_y*self.h))

    def mouse_on_piece(self, mouse_pos):
        rx = self.board_x * self.w + offset[0]
        ry = self.board_y * self.h + offset[1]

        return Utils.point_in_rect(mouse_pos, (rx, ry, self.w, self.h))


class Pawn(Piece):
    def __init__(self, team, board_x, board_y, w, h, surface): #x & y are Chessboard coordinates here!
        super().__init__(team, board_x, board_y, w, h, surface)

    def get_possible_moves(self, board):
        moves = []

        #two steps forward
        if self.team == "black" and self.board_y == 6 and board[self.board_x][self.board_y-2].occupying_piece == None: #board[self.board_x][self.board_y-2] should only get checked if board_y == 6 so this shouldnt ever go off board
            moves.append((self.board_x, self.board_y-2))


        #one step forward
        try:
            if board[self.board_x][self.board_y-1].occupying_piece == None: #try: because "self.board_y-1" could be off-board
                moves.append((self.board_x, self.board_y-1))
        except:
            pass

        #one step diagonally right
        try:
            if board[self.board_x+1][self.board_y-1].occupying_piece.team != self.team:
                moves.append((self.board_x+1, self.board_y-1))
        except:
            pass

        #one step diagonally left
        try:
            if board[self.board_x-1][self.board_y-1].occupying_piece.team != self.team:
                moves.append((self.board_x-1, self.board_y-1))
        except:
            pass

        return moves


