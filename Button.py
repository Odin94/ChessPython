import pygame
from pygame.locals import *

import Utils

from Deferred import Deferred
from Graphics import render_text, font, font_small, screen
from Animation import TileSheet, Animation

#REFACTOR: put whole animation in arguments, has to include spritesheet dimensions etc in one variable

class Button():

    def __init__(self, text, on_click_deferred, on_click_return_value, window_values, surface, hover_animation_surface = None, mouse_down_animation = None, spritesheet_dimensions=(2, 2), font_size='big'): #spritesheet for potential fancy animations later
        self.x, self.y, self.w, self.h = window_values

        self.font_size = font_size

        self.text = text

        self.surface = surface

        self.text_label = render_text(text, (0,0,0), font_size)
        self.get_text_draw_coords()

        self.on_click_deferred = on_click_deferred
        self.on_click_return_value = on_click_return_value

        hover_animation_surface = None

        if hover_animation_surface:
            self.on_hover_animation = Animation(TileSheet(hover_animation_surface, 292, 120, spritesheet_dimensions[0], spritesheet_dimensions[1]), 10, 4)
        else:
            self.on_hover_animation = None

        if mouse_down_animation:
            self.mouse_down_animation = Animation(TileSheet(mouse_down_animation, 292, 120, 1, 1), 10, 1)
        else:
            self.mouse_down_animation = None

        self.on_hover_animation_active = False
        self.mouse_down_animation_active = False

    def on_click(self):
        if self.mouse_down_animation:
            self.mouse_down_animation.done = True
        self.on_click_deferred.value = self.on_click_return_value

    def on_mouse_down(self):
        if not self.mouse_down_animation_active and self.mouse_down_animation:
            self.mouse_down_animation_active = True

    def on_hover(self):
        if not self.on_hover_animation_active and self.on_hover_animation:
            self.on_hover_animation_active = True

    def on_hover_off(self):
        self.mouse_down_animation_active = False

    def update(self, time=1):
        if self.mouse_down_animation_active:
            if self.mouse_down_animation.done:
                self.mouse_down_animation.done = False
                self.mouse_down_animation.reset()
                #self.mouse_down_animation_active = False

            self.mouse_down_animation.update(time)

        elif self.on_hover_animation_active:
            if self.on_hover_animation.done:
                self.on_hover_animation.done = False
                self.on_hover_animation.reset()
                self.on_hover_animation_active = False

            self.on_hover_animation.update(time)


    def draw(self):
        if self.mouse_down_animation_active:
            self.mouse_down_animation.draw(screen, self.x, self.y)
        elif self.on_hover_animation_active:
            self.on_hover_animation.draw(screen, self.x, self.y)
        else:
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

