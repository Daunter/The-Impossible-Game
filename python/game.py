#!/usr/bin/python

import pygame
import os
from datetime import datetime, timedelta

class Drawable:
    def draw_into(self, screen, x = 0, y = 0):
        screen.blit(self.image, self.rect.move(x, y))

class Box(Drawable):
    def __init__(self, image, x, y):
        self.jumping = False
        self.x = 0
        self.y = 0
        self.j_x = 0
        self.jump_max = 60
        self.jump_time = timedelta(seconds = 5)

    def jump(self):
        if not self.jumping:
            self.jumping = True
            self.jump_start = datetime.now()
            self.jump_peek = self.jump_start + self.jump_time / 2
            self.jump_end = self.jump_start + self.jump_time

    def draw_into(self, screen, x = 0, y = 0):
        now = datetime.now()
        if self.jumping:
            if now < self.jump_peek:
                m = now - self.jump_started
                t = m.seconds * 1000000 + m.microseconds
                
    
        if datetime.now() > self.jump_end:
            self.jumping = False


class Background(Drawable):
    def __init__(self, image):
       path = os.path.join('..', 'images', image)
       self.image = pygame.image.load(path)
       self.rect = self.image.get_rect()
    
    
def main():
    pygame.init()
    screen = pygame.display.set_mode((480, 340))
    pygame.display.set_caption('tig devel')
    pygame.mouse.set_visible(0)
    b = Background('testback.png')
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            
        b.draw_into(screen)
        pygame.display.flip()
    
    
if __name__ == '__main__':
    main()
