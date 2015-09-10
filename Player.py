import pygame, sys
from pygame.locals import *

from Move import Move
from Graphics import ChessBoardAssets, screen, render_text, tile_size


class Player():
    def __init__(self, team_color, game_board, black_pieces, white_pieces):
        self.team_color = team_color
        self.game_board = game_board
        self.black_pieces = black_pieces
        self.white_pieces = white_pieces

        self.selected_piece = None
        self.latest_move = None

        self.type = "local_player"

    def move(self, mouse_pos):
        try:
            new_pos = self.game_board.get_tile_below_mouse(mouse_pos)
            if new_pos in self.selected_piece.get_possible_moves(self.game_board.board):
                move = Move(self.selected_piece, new_pos, self.game_board.board[new_pos[0]][new_pos[1]].occupying_piece)

                self.selected_piece = None # prevents accidental moves (and fixes being able to waste a move on captured pieces)

                return move
        
        except (ValueError, AttributeError):
            return None

    def get_move(self):
        move = self.latest_move
        self.latest_move = None # ensures that this move is only used once

        return move

    def update(self, captured_pieces):
        if self.selected_piece in captured_pieces:
            self.selected_piece = None


    def handleEvents(self, events, my_turn, chessgame):
        LEFT = 1 #REFACTOR: move mousecontrols somewhere else? At least move LEFT etc definition somewhere else..
        MIDDLE = 2
        RIGHT = 3

        for event in events:
            if event.type == QUIT:
                chessgame.running = False

            elif event.type == KEYDOWN:
                chessgame.keyDown(event.key)

            elif event.type == KEYUP:
                if event.key == K_ESCAPE:
                    chessgame.running = False
                    sys.quit()
                chessgame.keyUp(event.key)

            elif event.type == MOUSEBUTTONDOWN:
                if self.team_color == "black": # select a piece
                    for piece in chessgame.black_pieces:
                        if piece.mouse_on_piece(event.pos):
                            self.selected_piece = piece

                elif self.team_color == "white":
                    for piece in chessgame.white_pieces:
                        if piece.mouse_on_piece(event.pos):
                            self.selected_piece = piece


            elif event.type == MOUSEBUTTONUP:
                if my_turn:
                    if event.button == RIGHT:
                        self.latest_move = self.move(event.pos)

            elif event.type == MOUSEMOTION:
                for tiles in chessgame.game_board.board:
                    for tile in tiles:
                        if tile.mouse_on_tile(event.pos):
                            chessgame.board_pos_mouseover_label = render_text(str(tile.board_x+1) + " / " + str(8 - tile.board_y), (100, 100, 200))
                            break