import pygame
from pygame.locals import *
import sys

from Graphics import ChessBoardAssets, screen, render_text
from Board import Board
from Piece import *

class ChessGame:
    def __init__(self, style="Default"):
        self.running = False
        self.clock = pygame.time.Clock() #to track FPS
        self.fps= 0

        ChessBoardAssets.load_assets(style)

        self.board_pos_mouseover_label = render_text("0 / 0", (100, 100, 200))

        self.board = Board()

        self.white_pieces = []
        self.black_pieces = []

        self.selected_piece = None

        for i in range(8):
            self.black_pieces.append(Pawn("black", i, 6, 60, 60, ChessBoardAssets.black_pawn_surface))
            self.white_pieces.append(Pawn("white", i, 1, 60, 60, ChessBoardAssets.white_pawn_surface))

        self.mainLoop()
        
    def handleEvents(self):
        LEFT = 1 #REFACTOR: move mousecontrols somewhere else? At least move LEFT etc definition somewhere else..
        MIDDLE = 2
        RIGHT = 3

        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False

            elif event.type == KEYDOWN:
                self.keyDown(event.key)

            elif event.type == KEYUP:
                if event.key == K_ESCAPE:
                    self.running = False
                    sys.quit()
                self.keyUp(event.key)

            elif event.type == MOUSEBUTTONDOWN:
               # selected_a_piece = False
                for piece in self.black_pieces:
                    if piece.mouse_on_piece(event.pos):
                       # selected_a_piece = True
                        self.selected_piece = piece


            elif event.type == MOUSEBUTTONUP:
                if event.button == RIGHT:
                    try:
                        new_place = self.board.get_tile_below_mouse(event.pos)
                        if new_place in self.selected_piece.get_possible_moves(self.board.board):
                            self.selected_piece.board_x = new_place[0]
                            self.selected_piece.board_y = new_place[1]
                    except:
                        print("click inside the chessboard, please.")

            elif event.type == MOUSEMOTION:
                for tiles in self.board.board:
                    for tile in tiles:
                        if tile.mouse_on_tile(event.pos):
                            self.board_pos_mouseover_label = render_text(str(tile.board_x+1) + " / " + str(tile.board_y+1), (100, 100, 200))
                            break

                #self.mouseMotion(event.buttons, event.pos, event.rel)
    
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
            self.handleEvents()
            self.update()
            self.draw()
            pygame.display.flip()
            self.clock.tick(self.fps)
            
    def update(self):
        self.board.update(self.white_pieces + self.black_pieces)

        
    def draw(self):
        self.board.draw()
        for piece in self.black_pieces:
            piece.draw()
        for piece in self.white_pieces:
            piece.draw()

        screen.blit(self.board_pos_mouseover_label, (10, 450))


        
    def keyDown(self, key):
        pass
        
    def keyUp(self, key):
        pass
    
    def mouseUp(self, button, pos):
        pass
        
    def mouseMotion(self, buttons, pos, rel):
        pass