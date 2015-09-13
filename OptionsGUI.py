import pygame
from pygame.locals import *

from Options import Options
from Deferred import Deferred
from Button import Button
from Graphics import OptionsAssets, screen



class OptionsGUI():
    def __init__(self):
        self.load_assets()
        Options.set_backup_options()

        self.decision = Deferred("")
        self.buttons = {}

        self.buttons["highlight_selected"] = Button("highlight_selected", self.decision, "hl_sel", (100, 225, 360, 50), OptionsAssets.button_small_surface, (), "small")
        self.buttons["highlight_capturable"] = Button("highlight_capturable", self.decision, "hl_cap", (100, 290, 360, 50), OptionsAssets.button_small_surface, (), "small")
        self.buttons["highlight_possible_moves"] = Button("highlight_possible_moves", self.decision, "hl_poss", (100, 355, 360, 50), OptionsAssets.button_small_surface, (), "small")
        self.buttons["show_captured_pieces"] = Button("show_captured_pieces", self.decision, "show_cap", (100, 420, 360, 50), OptionsAssets.button_small_surface, (), "small")

        self.buttons["back"] = Button("SAVE & BACK", self.decision, "back", (425, 520, 360, 50), OptionsAssets.button_small_surface, (), "small")
        self.buttons["cancel"] = Button("CANCEL", self.decision, "cancel", (25, 520, 360, 50), OptionsAssets.button_small_surface, (), "small")


        
        self.running = True
        while self.running:
            self.update()
            if self.decision.value == "hl_sel":
                Options.highlight_selected = not Options.highlight_selected
            if self.decision.value == "hl_cap":
                Options.highlight_capturable = not Options.highlight_capturable
            if self.decision.value == "hl_poss":
                Options.highlight_possible_moves = not Options.highlight_possible_moves
            if self.decision.value == "show_cap":
                Options.show_captured_pieces = not Options.show_captured_pieces

            if self.decision.value == "options":
                OptionsGUI()

            if self.decision.value == "back":
                Options.save_current_options()
                self.running = False

            if self.decision.value == "cancel":
                Options.load(Options.backup_options)
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

            # elif event.type == MOUSEMOTION:
            #     controls.mouse_motion(event.buttons, event.pos, event.rel)

    def update(self):
        self.handle_events()
        self.draw()


    def draw(self):
        screen.blit(OptionsAssets.background, (0,0))

        for btn in self.buttons:
            self.buttons[btn].draw()

        if Options.highlight_selected:
            screen.blit(OptionsAssets.check, (475, self.buttons["highlight_selected"].y))
        if Options.highlight_capturable:
            screen.blit(OptionsAssets.check, (475, self.buttons["highlight_capturable"].y))
        if Options.highlight_possible_moves:
            screen.blit(OptionsAssets.check, (475, self.buttons["highlight_possible_moves"].y))
        if Options.show_captured_pieces:
            screen.blit(OptionsAssets.check, (475, self.buttons["show_captured_pieces"].y))



        pygame.display.flip()

    def load_assets(self):
        OptionsAssets.load_assets()