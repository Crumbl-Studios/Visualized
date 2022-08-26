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
    elif currentgamestate == "logoScreen":
        pygame.mixer.music.load(fileHandler.get_logo_music())
        pygame.mixer.music.play(loops=1)
        pygame.mixer.music.set_volume(audio_vol)
    elif currentgamestate == "game_over":
        pygame.mixer.music.load(fileHandler.get_gameover_music())
        pygame.mixer.music.play(loops=-1)
        pygame.mixer.music.set_volume(audio_vol)
    elif currentgamestate == "shop_menu":
        pygame.mixer.music.load(fileHandler.get_shop_music())
        pygame.mixer.music.play(loops=-1)
        pygame.mixer.music.set_volume(audio_vol)
    elif currentgamestate == "sky_shop":
        pygame.mixer.music.load(fileHandler.get_sky_music())
        pygame.mixer.music.play(loops=-1)
        pygame.mixer.music.set_volume(audio_vol)
    elif currentgamestate == "char_shop":
        pygame.mixer.music.load(fileHandler.get_char_music())
        pygame.mixer.music.play(loops=-1)
        pygame.mixer.music.set_volume(audio_vol)
    elif currentgamestate == "game":
        pygame.mixer.music.load(fileHandler.get_play_music())
        pygame.mixer.music.play(loops=-1)
        pygame.mixer.music.set_volume(audio_vol)
    elif currentgamestate == "pause":
        pygame.mixer.music.load(fileHandler.get_pause_music())
        pygame.mixer.music.play(loops=-1)
        pygame.mixer.music.set_volume(audio_vol)
    else:
        print("audiohandler: currentgamestate value is (%s) is incorrect"%(currentgamestate))

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