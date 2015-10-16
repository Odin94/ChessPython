import pygame
#ideas: define how often the animation should be looped and if loop starts from beginning or reverses; add option to play animation in reverse

class Animation():
    def __init__(self, tile_sheet, animation_frame_durations, frame_count = None, speed_mult = 1):
        self.tile_sheet = tile_sheet

        if type(animation_frame_durations) == int:
            self.animation_frame_durations = [animation_frame_durations for x in range(frame_count)]
            self.frame_count = frame_count
        else:
            self.animation_frame_durations = animation_frame_durations
            self.frame_count = len(animation_frame_durations)  

        self.speed = speed_mult

        self.frame_iterator = 0
        self.frame_time_acc = 0

        self.done = False
        self.looping = False

    def update(self, time = 1):
        self.frame_time_acc += time

        if self.frame_time_acc >= self.animation_frame_durations[self.frame_iterator]: # if accumulated time > current frame's show-duration
            self.frame_time_acc -= self.animation_frame_durations[self.frame_iterator] # reduce accumulator by last frames duration
            
            if self.looping:
                self.frame_iterator = (self.frame_iterator + 1) % len(self.frame_iterator) # select next frame
            elif not self.done:
                self.frame_iterator += 1
                if self.frame_iterator >= self.frame_count:
                    self.done = True

    def reset(self):
        self.frame_iterator = 0
        self. frame_time_acc = 0

    def get_current_frame_rect(self):
        x = (self.frame_iterator % self.tile_sheet.row_length_cap) * (self.tile_sheet.tile_width + self.tile_sheet.separation_thickness)
        y = int(self.frame_iterator % self.tile_sheet.column_length_cap) * (self.tile_sheet.tile_height + self.tile_sheet.separation_thickness)
        w = self.tile_sheet.tile_width
        h = self.tile_sheet.tile_height

        if y != 0:
            print(y, "   ",)

        return pygame.Rect(x , y, w, h)

    def draw(self, screen, x, y):
        source_rect = self.get_current_frame_rect()

        screen.blit(self.tile_sheet.sheet_image, (x, y), self.get_current_frame_rect())



class TileSheet():
    def __init__(self, sheet_image, tile_width, tile_height, row_length_cap = 10, column_length_cap = 10, separation_thickness = 0):
        self.sheet_image = sheet_image
        self.tile_width = tile_width
        self.tile_height = tile_height

        self.row_length_cap = row_length_cap
        self.column_length_cap = column_length_cap

        self.separation_thickness = separation_thickness




class ANIMATION():
    TYPE_LOOP, TYPE_REVERSE = range(2)