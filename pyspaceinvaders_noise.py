import pygame
import numpy

def add_noise(surface):
    mask = surface.copy()
    mask.set_colorkey((255,255,255))

    screen_array = pygame.surfarray.pixels3d(surface)
    noise = numpy.random.random((surface.get_width(), surface.get_height())) * 255
    screen_array *= noise[:, :, numpy.newaxis]
    del screen_array

    surface.blit(mask, (0,0))
    surface = mask
