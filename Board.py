import pygame
#REFACTOR: w/h = 60; define in one place only(maybe graphics?)
from Tile import Tile
from Graphics import ChessBoardAssets, screen, offset

class Board():
    def __init__(self):
        self.board = [[0 for x in range(8)] for x in range(8)] 


        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if (i % 2 == 0 and j % 2 == 1) or (i % 2 == 1 and j % 2 == 0):
                    self.board[i][j] = Tile(i, j, 60, 60, ChessBoardAssets.white_tile_surface)
                else:
                    self.board[i][j] = Tile(i, j, 60, 60, ChessBoardAssets.black_tile_surface)

    def update(self, pieces):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                self.board[i][j].occupying_piece = None

        for piece in pieces:
            self.board[piece.board_x][piece.board_y].occupying_piece = piece



    def draw(self):
        screen.blit(ChessBoardAssets.background, (0,0))

        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
            	self.board[i][j].draw()

    def get_tile_below_mouse(self, mouse_pos):
    	for i in range(len(self.board)):
            for j in range(len(self.board[i])):
            	if self.board[i][j].mouse_on_tile(mouse_pos):
            		return (i, j)

class ENUM:
    A, B, C, D, E, F, G, H = range(8)
