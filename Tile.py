import pygame

import Utils

from Graphics import screen, offset

class Tile():
    def __init__(self, board_x, board_y, w, h, surface): #x & y are Chessboard coordinates here!
        self.board_x = board_x
        self.board_y = board_y
        self.w, self.h = w, h

        self.surface = surface
        self.screen = screen

        self.occupying_piece = None

    def draw(self):
    	screen.blit(self.surface, (offset[0] + self.board_x * self.w, offset[1] + self.board_y * self.h))

    def mouse_on_tile(self, mouse_pos):
        rx = self.board_x * self.w + offset[0]
        ry = self.board_y * self.h + offset[1]

        return Utils.point_in_rect(mouse_pos, (rx, ry, self.w, self.h))