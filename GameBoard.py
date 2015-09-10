import pygame
#REFACTOR: w/h = 60; define in one place only(maybe graphics?)
from Tile import Tile
from Graphics import ChessBoardAssets, screen, offset, tile_size

class GameBoard():
    def __init__(self):
        self.board = [[0 for x in range(8)] for x in range(8)] 


        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if (i % 2 == 0 and j % 2 == 1) or (i % 2 == 1 and j % 2 == 0):
                    self.board[i][j] = Tile(i, j, tile_size, tile_size, ChessBoardAssets.white_tile_surface)
                else:
                    self.board[i][j] = Tile(i, j, tile_size, tile_size, ChessBoardAssets.black_tile_surface)

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

        for i in range(8):
            screen.blit(ChessBoardAssets.numbers[i], (8*tile_size + offset[0] + 10, (7-i) * tile_size + offset[1])) # numbers
            screen.blit(ChessBoardAssets.letters[i], (i*tile_size + offset[0] + 10, 8 * tile_size + offset[1])) # letters

    def get_tile_below_mouse(self, mouse_pos):
    	for i in range(len(self.board)):
            for j in range(len(self.board[i])):
            	if self.board[i][j].mouse_on_tile(mouse_pos):
            		return (i, j)

class ENUM:
    A, B, C, D, E, F, G, H = range(8)
