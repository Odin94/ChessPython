
import pygame, sys
from pygame.locals import *
from random import randint

from Move import Move
from Graphics import ChessBoardAssets, screen, render_text, tile_size


class AI():
    def __init__(self, team_color, game_board, black_pieces, white_pieces):
        self.team_color = team_color
        self.game_board = game_board
        self.black_pieces = black_pieces
        self.white_pieces = white_pieces

        self.selected_piece = None
        self.latest_move = None

        self.type = "ai_player"

    def get_move(self):
        pass

    def update(self, captured_pieces):
        pass

    def handleEvents(self, events, my_turn, chessgame):
        pass


class RandomAI(AI):
    def __init__(self, team_color, game_board, white_pieces, black_pieces):
        super().__init__(team_color, game_board, black_pieces, white_pieces)

    def get_move(self): # REFACTOR: if there is no possible move we get stuck in the loop (is such a situation even possible without triggering an end-game condition?)
        move = None
        move_made = False
        while not move_made: # loop until a possible move was found
            if self.team_color == "black":
                piece_number = randint(0, len(self.black_pieces)-1) # pick random black piece
                selected_piece = self.black_pieces[piece_number]

                possible_moves = selected_piece.get_possible_moves(self.game_board.board) # get possible moves for that piece
                if possible_moves: # if there are no possible moves for the piece we go back to the top of the loop
                    move_number = randint(0, len(possible_moves)-1)
                    selected_pos = possible_moves[move_number]

                    move = Move(selected_piece, selected_pos, self.game_board.board[selected_pos[0]][selected_pos[1]].occupying_piece)
                    move_made = True


            elif self.team_color == "white":
                piece_number = randint(0, len(self.white_pieces)-1) # pick random white piece
                selected_piece = self.white_pieces[piece_number]

                possible_moves = selected_piece.get_possible_moves(self.game_board.board) # get possible moves for that piece
                if possible_moves: # if there are no possible moves for the piece we go back to the top of the loop
                    move_number = randint(0, len(possible_moves)-1)
                    selected_pos = possible_moves[move_number]

                    move = Move(selected_piece, selected_pos, self.game_board.board[selected_pos[0]][selected_pos[1]].occupying_piece)
                    move_made = True

        return move



