import pygame
import fileHandler

#Get audio files

loaded = 0
audio_vol = 1

def play(currentgamestate):
    pygame.mixer.music.unload()
    pygame.mixer.music.set_volume(audio_vol)
    if currentgamestate == "title":
        pygame.mixer.music.load(fileHandler.get_title_music())
        pygame.mixer.music.play(loops=-1)
        pygame.mixer.music.set_volume(audio_vol)
    if currentgamestate == "game_over":
        pygame.mixer.music.load(fileHandler.get_gameover_music())
        pygame.mixer.music.play(loops=-1)
        pygame.mixer.music.set_volume(audio_vol)

def stop():
    pygame.mixer.music.stop()