import pygame
from pygame.locals import *

from Deferred import Deferred
from Lobby import Lobby
from Button import Button
from Graphics import MenueAssets, screen
from Options import Options
from OptionsGUI import OptionsGUI

#REFACTOR: maybe keyboard selection?
#REFACTOR: graphics module for loading/preparing surfaces, animations

class Menue():
    def __init__(self, window_x=200, window_y=200, style="Default"):

        self.x = window_x
        self.y = window_y
                
        self.load_assets()

        self.decision = Deferred("")
        self.buttons = {}
        self.buttons["play"] = Button("PLAY", self.decision, "lobby", (100, 225, 292, 120), MenueAssets.button_surface, MenueAssets.button_hover_animation_surface, MenueAssets.button_pressed_surface)
        self.buttons["options"] = Button("OPTIONS", self.decision, "options", (100, 350, 292, 120), MenueAssets.button_surface, MenueAssets.button_hover_animation_surface, MenueAssets.button_pressed_surface)
        self.buttons["quit"] = Button("QUIT", self.decision, "quit", (100, 475, 292, 120), MenueAssets.button_surface, MenueAssets.button_hover_animation_surface, MenueAssets.button_pressed_surface)


        
        self.running = True
        while self.running:
            self.update()
            if self.decision.value == "lobby":
                Lobby()

            if self.decision.value == "options":
                OptionsGUI()

            if self.decision.value == "quit":
                self.running = False
        
            self.decision.value = ""

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False

            elif event.type == KEYUP:
                if event.key == K_ESCAPE:
                    self.running = False

            elif event.type == MOUSEBUTTONUP:
                for btn in self.buttons:
                    if self.buttons[btn].mouse_over_button(event.pos):
                        self.buttons[btn].on_click()

            elif event.type == MOUSEBUTTONDOWN:
                for btn in self.buttons:
                    if self.buttons[btn].mouse_over_button(event.pos):
                        self.buttons[btn].on_mouse_down()

            elif event.type == MOUSEMOTION:
                for btn in self.buttons:
                    if self.buttons[btn].mouse_over_button(event.pos):
                        self.buttons[btn].on_hover()
                    else:
                        self.buttons[btn].on_hover_off()

    def update(self):
        for btn in self.buttons:
            self.buttons[btn].update()
        self.handle_events()
        self.draw()


    def draw(self):
        screen.blit(MenueAssets.background_surface, (0,0))

        for btn in self.buttons:
            self.buttons[btn].draw()

        pygame.display.flip()

    def load_assets(self):
        MenueAssets.load_assets()