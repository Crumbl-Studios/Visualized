import pygame
import fileHandler

#Get audio files

loaded = 0
audio_vol = 1

def play(currentgamestate): # Load and play music
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

def stop(): # Stop music
    pygame.mixer.music.stop()

def update_volume(increment = False,decrement = False): # Volume up/down function
    global audio_vol
    if increment == True and not audio_vol >= 1:
        audio_vol += 0.05
    if decrement == True and not audio_vol <= 0:
        audio_vol -= 0.05
    pygame.mixer.music.set_volume(audio_vol)
    print("audioHandler: volume is now %f" %(audio_vol))

def set_volume(vol):
    global audio_vol
    audio_vol = vol