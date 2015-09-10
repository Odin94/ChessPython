import pygame, sys
from pygame.locals import *
from Chess import ChessGame
from Deferred import Deferred
from Button import Button
from Graphics import LobbyAssets, screen

class Lobby():
    def __init__(self):
        info = pygame.display.Info()

        self.w = info.current_w
        self.h = info.current_h

        self.player1 = "local_player"
        self.player2 = "local_player"

        self.assets = {}
        self.load_assets()
        
        self.decision = Deferred("")
        self.buttons = {}
        self.buttons["play"] = Button("PLAY", self.decision, "play", (490, 470, 292, 120), LobbyAssets.button_surface)
        self.buttons["back"] = Button("BACK", self.decision, "back", (15, 470, 292, 120), LobbyAssets.button_surface)

        self.buttons["player1_AI"] = Button("AI", self.decision, "p1_ai", (175, 296, 120, 50), LobbyAssets.button_small_surface, (), "small")
        self.buttons["player1_LOCAL"] = Button("LOCAL", self.decision, "p1_local", (300, 296, 120, 50), LobbyAssets.button_small_surface, (), "small")
        self.buttons["player1_NETWORK"] = Button("NETWORK", self.decision, "p1_net", (425, 296, 120, 50), LobbyAssets.button_small_surface, (), "small")

        self.buttons["player2_AI"] = Button("AI", self.decision, "p2_ai", (175, 400, 120, 50), LobbyAssets.button_small_surface, (), "small")
        self.buttons["player2_LOCAL"] = Button("LOCAL", self.decision, "p2_local", (300, 400, 120, 50), LobbyAssets.button_small_surface, (), "small")
        self.buttons["player2_NETWORK"] = Button("NETWORK", self.decision, "p2_net", (425, 400, 120, 50), LobbyAssets.button_small_surface, (), "small")


        self.running = True
        while self.running:
            self.update()
            if self.decision.value == "play":
                c = ChessGame()
                c.run(self.player1, self.player2)

            elif self.decision.value == "back":
                self.running = False


            elif self.decision.value == "p1_ai":
                print(self.decision.value)
                self.player1 = "ai_player"

            elif self.decision.value == "p1_local":
                print(self.decision.value)
                self.player1 = "local_player"

            elif self.decision.value == "p1_net":
                print(self.decision.value)
                self.player1 = "network_player"


            elif self.decision.value == "p2_ai":
                print(self.decision.value)
                self.player2 = "ai_player"

            elif self.decision.value == "p2_local":
                print(self.decision.value)
                self.player2 = "local_player"

            elif self.decision.value == "p2_net":
                print(self.decision.value)
                self.player2 = "network_player"

            self.decision.value = ""

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
            elif event.type == KEYUP:
                if event.key == K_ESCAPE:
                    self.running = False
                    sys.quit()
            elif event.type == MOUSEBUTTONUP:
                for btn in self.buttons:
                    if self.buttons[btn].mouse_over_button(event.pos):
                        self.buttons[btn].on_click()
            # elif event.type == MOUSEMOTION:
            #     controls.mouse_motion(event.buttons, event.pos, event.rel)

    def update(self):
        self.handle_events()
        self.draw()


    def draw(self):
        screen.blit(LobbyAssets.background_surface, (0,0))

        for btn in self.buttons:
            self.buttons[btn].draw()

        pygame.display.flip()

    def load_assets(self):
        LobbyAssets.load_assets()