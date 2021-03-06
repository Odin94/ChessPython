import pygame
from pygame.locals import *
import sys

from Graphics import ChessBoardAssets, screen, render_text, tile_size, offset
from GameBoard import GameBoard
from Piece import *
from Player import Player
from AI import RandomAI
from Options import Options

class ChessGame:
    def __init__(self):
        pass

    def run(self, player1 = "local_player", player2 = "local_player"):
        self.running = False
        self.clock = pygame.time.Clock() #to track FPS
        self.fps= 0

        ChessBoardAssets.load_assets()

        self.board_pos_mouseover_label = render_text("0 / 0", (100, 100, 200))

        self.game_board = GameBoard()

        self.white_pieces = []
        self.black_pieces = []

        self.captured_pieces = []
        
        self.fill_board()


        self.turn = TURN.PLAYER_1
        self.moves = []

        if player1 == "local_player":
            self.player1 = Player("black", self.game_board, self.white_pieces, self.black_pieces)
        elif player1 == "ai_player":
            self.player1 = RandomAI("black", self.game_board, self.white_pieces, self.black_pieces)

        if player2 == "local_player":
            self.player2 = Player("white", self.game_board, self.white_pieces, self.black_pieces)
        elif player2 == "ai_player":
            self.player2 = RandomAI("white", self.game_board, self.white_pieces, self.black_pieces)

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
        self.game_board.update(self.white_pieces + self.black_pieces)
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
        self.game_board.draw()
        for piece in self.black_pieces:
            piece.draw()
        for piece in self.white_pieces:
            piece.draw()

        if Options.show_captured_pieces: # draw captured pieces on the side of the board
            xoffset = 10
            for piece in self.captured_pieces: #Refactor: move this to piece class?
                piece.draw(xoffset)
                xoffset += 5


        self.draw_color_helpers()
        
        screen.blit(self.board_pos_mouseover_label, (10, 450))


       
    def draw_color_helpers(self):
        if self.turn == TURN.PLAYER_1 and self.player1.type == "local_player" and self.player1.selected_piece:
            if Options.highlight_selected:
                screen.blit(ChessBoardAssets.selected_piece, (self.player1.selected_piece.board_x * tile_size + offset[0], self.player1.selected_piece.board_y * tile_size + offset[1]))# draw selected

            for pos in self.player1.selected_piece.possible_moves: # draw possible captures & moves
                if Options.highlight_capturable and self.game_board.board[pos[0]][pos[1]].occupying_piece:
                    screen.blit(ChessBoardAssets.possible_capture, (pos[0] * tile_size + offset[0], pos[1] * tile_size + offset[1])) # draw possible captures
                elif Options.highlight_possible_moves:
                    screen.blit(ChessBoardAssets.possible_move, (pos[0] * tile_size + offset[0], pos[1] * tile_size + offset[1])) # draw possible moves

        elif self.turn == TURN.PLAYER_2 and self.player2.type == "local_player" and self.player2.selected_piece:
            if Options.highlight_selected:
                screen.blit(ChessBoardAssets.selected_piece, (self.player2.selected_piece.board_x * tile_size + offset[0], self.player2.selected_piece.board_y * tile_size + offset[1]))

            for pos in self.player2.selected_piece.possible_moves:
                if Options.highlight_capturable and self.game_board.board[pos[0]][pos[1]].occupying_piece:
                    screen.blit(ChessBoardAssets.possible_capture, (pos[0] * tile_size + offset[0], pos[1] * tile_size + offset[1])) # draw possible captures
                elif Options.highlight_possible_moves:
                    screen.blit(ChessBoardAssets.possible_move, (pos[0] * tile_size + offset[0], pos[1] * tile_size + offset[1])) # draw possible moves


    def fill_board(self):
        for i in range(8):
            self.black_pieces.append(Pawn("black", i, 6, tile_size, tile_size, ChessBoardAssets.black_pawn_surface))
            self.white_pieces.append(Pawn("white", i, 1, tile_size, tile_size, ChessBoardAssets.white_pawn_surface))

        # rooks
        self.black_pieces.append(Rook("black", 7, 7, tile_size, tile_size, ChessBoardAssets.black_rook_surface))
        self.black_pieces.append(Rook("black", 0, 7, tile_size, tile_size, ChessBoardAssets.black_rook_surface))

        self.white_pieces.append(Rook("white", 7, 0, tile_size, tile_size, ChessBoardAssets.white_rook_surface))
        self.white_pieces.append(Rook("white", 0, 0, tile_size, tile_size, ChessBoardAssets.white_rook_surface))

        # Bishop
        self.black_pieces.append(Bishop("black", 5, 7, tile_size, tile_size, ChessBoardAssets.black_bishop_surface))
        self.black_pieces.append(Bishop("black", 2, 7, tile_size, tile_size, ChessBoardAssets.black_bishop_surface))

        self.white_pieces.append(Bishop("white", 5, 0, tile_size, tile_size, ChessBoardAssets.white_bishop_surface))
        self.white_pieces.append(Bishop("white", 2, 0, tile_size, tile_size, ChessBoardAssets.white_bishop_surface))

        # knights
        self.black_pieces.append(Knight("black", 6, 7, tile_size, tile_size, ChessBoardAssets.black_knight_surface))
        self.black_pieces.append(Knight("black", 1, 7, tile_size, tile_size, ChessBoardAssets.black_knight_surface))

        self.white_pieces.append(Knight("white", 6, 0, tile_size, tile_size, ChessBoardAssets.white_knight_surface))
        self.white_pieces.append(Knight("white", 1, 0, tile_size, tile_size, ChessBoardAssets.white_knight_surface))

        # Queens
        self.black_pieces.append(Queen("black", 3, 7, tile_size, tile_size, ChessBoardAssets.black_queen_surface))
        self.white_pieces.append(Queen("white", 3, 0, tile_size, tile_size, ChessBoardAssets.white_queen_surface))

        # Kings
        self.black_pieces.append(King("black", 4, 7, tile_size, tile_size, ChessBoardAssets.black_king_surface))
        self.white_pieces.append(King("white", 4, 0, tile_size, tile_size, ChessBoardAssets.white_king_surface))

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