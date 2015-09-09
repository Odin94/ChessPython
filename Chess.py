import pygame
from pygame.locals import *
import sys

from Graphics import ChessBoardAssets, screen, render_text, tile_size, offset
from Board import Board
from Piece import *
from Player import Player

class ChessGame:
    def __init__(self, style="Default", player1 = "local_player", player2 = "local_player"):
        self.running = False
        self.clock = pygame.time.Clock() #to track FPS
        self.fps= 0

        ChessBoardAssets.load_assets(style)

        self.board_pos_mouseover_label = render_text("0 / 0", (100, 100, 200))

        self.board = Board()

        self.white_pieces = []
        self.black_pieces = []

        self.captured_pieces = []
        
        for i in range(8):
            self.black_pieces.append(Pawn("black", i, 6, tile_size, tile_size, ChessBoardAssets.black_pawn_surface))
            self.white_pieces.append(Pawn("white", i, 1, tile_size, tile_size, ChessBoardAssets.white_pawn_surface))

        self.turn = TURN.PLAYER_1
        self.moves = []

        if player1 == "local_player":
            self.player1 = Player("black", self.board, self.white_pieces, self.black_pieces)

        if player2 == "local_player":
            self.player2 = Player("white", self.board, self.white_pieces, self.black_pieces)

        self.mainLoop()


    #wait until a key is pressed, then return
    def waitForKey(self):
        press=False
        while not press:
            for event in pygame.event.get():
                if event.type == KEYUP:
                    press = True
             
    #enter the main loop, possibly setting max FPS
    def mainLoop(self, fps=0):
        self.running = True
        self.fps= fps
        
        while self.running:
            pygame.display.set_caption("FPS: %i" % self.clock.get_fps())
            
            events = pygame.event.get()
            self.player1.handleEvents(events, self.turn==TURN.PLAYER_1, self)
            self.player2.handleEvents(events, self.turn==TURN.PLAYER_2, self)

            self.update()
            self.draw()
            pygame.display.flip()
            self.clock.tick(self.fps)
            
    def update(self):
        self.board.update(self.white_pieces + self.black_pieces)
        self.player1.update(self.captured_pieces)
        self.player2.update(self.captured_pieces)

        if self.turn == TURN.PLAYER_1:
            move = self.player1.get_move()

        elif self.turn == TURN.PLAYER_2:
            move = self.player2.get_move()

        if move: # if received move, execute it
            move.execute(self.white_pieces, self.black_pieces, self.captured_pieces)
            self.moves.append(move)
            self.turn = (self.turn + 1) % 2
        # wait for p1 move, execute - wait for p2 move, execute (with time limit?)

        
    def draw(self):
        self.board.draw()
        for piece in self.black_pieces:
            piece.draw()
        for piece in self.white_pieces:
            piece.draw()

        xoffset = 10
        for piece in self.captured_pieces: #Refactor: move this to piece class?
            piece.draw(xoffset)
            xoffset += 5


        if self.turn == TURN.PLAYER_1 and self.player1.type == "local_player" and self.player1.selected_piece:
            screen.blit(ChessBoardAssets.selected_piece, (self.player1.selected_piece.board_x * tile_size + offset[0], self.player1.selected_piece.board_y * tile_size + offset[1])) # draw selected

            for pos in self.player1.selected_piece.get_possible_moves(self.board.board): # draw possible captures & moves
                if self.board.board[pos[0]][pos[1]].occupying_piece:
                    screen.blit(ChessBoardAssets.possible_capture, (pos[0] * tile_size + offset[0], pos[1] * tile_size + offset[1])) # draw possible captures
                else:
                    screen.blit(ChessBoardAssets.possible_move, (pos[0] * tile_size + offset[0], pos[1] * tile_size + offset[1])) # draw possible moves

        elif self.turn == TURN.PLAYER_2 and self.player2.type == "local_player" and self.player2.selected_piece:
            screen.blit(ChessBoardAssets.selected_piece, (self.player2.selected_piece.board_x * tile_size + offset[0], self.player2.selected_piece.board_y * tile_size + offset[1]))

            for pos in self.player2.selected_piece.get_possible_moves(self.board.board):
                if self.board.board[pos[0]][pos[1]].occupying_piece:
                    screen.blit(ChessBoardAssets.possible_capture, (pos[0] * tile_size + offset[0], pos[1] * tile_size + offset[1])) # draw possible captures
                else:
                    screen.blit(ChessBoardAssets.possible_move, (pos[0] * tile_size + offset[0], pos[1] * tile_size + offset[1])) # draw possible moves

        screen.blit(self.board_pos_mouseover_label, (10, 450))


        
    def keyDown(self, key):
        pass
        
    def keyUp(self, key):
        pass
    
    def mouseUp(self, button, pos):
        pass
        
    def mouseMotion(self, buttons, pos, rel):
        pass

class TURN:
    PLAYER_1, PLAYER_2 = range(2)