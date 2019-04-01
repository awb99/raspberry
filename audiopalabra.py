import pygame

pygame.mixer.init()
pygame.mixer.music.load("mp3/niunasolapalabra.mp3")
pygame.mixer.music.set_volume(4.0)
pygame.mixer.music.play()

while pygame.mixer.music.get_busy() == True:
	pass
