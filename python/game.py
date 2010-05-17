#!/usr/bin/python

import pygame
import os

class Drawable:
    def draw_into(self, screen, x = 0, y = 0):
        screen.blit(self.image, self.rect.move(x, y))


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
