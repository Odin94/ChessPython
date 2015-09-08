import pygame
from pygame.locals import *
from Chess import ChessGame
from Deferred import Deferred
from Button import Button
from Graphics import LobbyAssets

class Lobby():
    def __init__(self, screen):
        info = pygame.display.Info()

        self.w = info.current_w
        self.h = info.current_h

        self.screen = screen

        self.assets = {}
        self.load_assets()
        self.draw()
        
        self.decision = Deferred("")
        self.buttons = {}
        self.buttons["play"] = Button(self.screen, "PLAY", self.decision, "play", (100, 225, 292, 120), LobbyAssets.button_surface)
        self.buttons["back"] = Button(self.screen, "BACK", self.decision, "back", (100, 475, 292, 120), LobbyAssets.button_surface)


        self.running = True
        while self.running:
            self.update()
            if self.decision.value == "play":
                pass

            if self.decision.value == "back":
                self.running = False

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
            elif event.type == KEYUP:
                if event.key == K_ESCAPE:
                    self.running = False
            elif event.type == MOUSEBUTTONUP:
                ChessGame()
            # elif event.type == MOUSEMOTION:
            #     controls.mouse_motion(event.buttons, event.pos, event.rel)

    def update(self):
        self.handle_events()
        self.draw()


    def draw(self):
        self.screen.blit(self.assets["background"], (0,0))

        pygame.display.flip()

    def load_assets(self, style="Default"):
        path = "Assets/"+style+"/Lobby/"

        self.assets["background"] = pygame.image.load(path+'background.png').convert()


        for surface in self.assets:
            self.assets[surface].set_colorkey((0,100,100))