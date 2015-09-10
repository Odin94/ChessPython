import pygame
from pygame.locals import *

import Utils

from Deferred import Deferred
from Graphics import render_text, font, font_small, screen

#REFACTOR: On mouse_over animation, on mouse_down animation

class Button():

    def __init__(self, text, on_click_deferred, on_click_return_value, window_values, surface, spritesheet_values=(), font_size='big'): #spritesheet for potential fancy animations later
        self.x, self.y, self.w, self.h = window_values

        self.font_size = font_size

        self.text = text

        self.surface = surface

        self.text_label = render_text(text, (0,0,0), font_size)
        self.get_text_draw_coords()

        self.on_click_deferred = on_click_deferred
        self.on_click_return_value = on_click_return_value


    def on_click(self):
        self.on_click_deferred.value = self.on_click_return_value

    def draw(self):
        screen.blit(self.surface, (self.x, self.y))
        screen.blit(self.text_label, (self.text_x, self.text_y))


    def mouse_over_button(self, mouse_pos):
        return Utils.point_in_rect(mouse_pos, (self.x, self.y, self.w, self.h))

    def get_text_draw_coords(self):
        if self.font_size == "big":
            text_w = font.size(self.text)[0]
            text_h = font.size(self.text)[1]
        elif self.font_size == "small":
            text_w = font_small.size(self.text)[0]
            text_h = font_small.size(self.text)[1]

        self.text_x = self.x + 0.5 * self.w - 0.5 * text_w
        self.text_y = self.y + 0.5 * self.h - 0.5 * text_h

