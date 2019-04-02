import pygame

pygame.mixer.init()
pygame.mixer.music.load("mp3/intercom.mp3")
pygame.mixer.music.set_volume(4.0)
pygame.mixer.music.play()

while pygame.mixer.music.get_busy() == True:
	pass
