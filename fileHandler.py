import pygame
import json
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
save_dir = os.path.join(current_dir, 'bin')
font_dir = os.path.join(current_dir, 'Font')

audio_dir = os.path.join(current_dir, 'Audio')
player_audio_dir = os.path.join(audio_dir, 'Player')
textures_dir = os.path.join(current_dir, 'Textures')

ui_dir = os.path.join(textures_dir, 'UI')

world_dir = os.path.join(textures_dir, 'World')
backgrounds_dir = os.path.join(world_dir, 'Backgrounds')
grounds_dir = os.path.join(world_dir, 'Grounds')

characters_dir = os.path.join(textures_dir, 'Characters')
enemies_dir = os.path.join(textures_dir, 'Enemies')

other_textures_dir = os.path.join(textures_dir, 'Other')

vr_guy_dir = os.path.join(characters_dir, 'Virtual Guy')
ninja_frog_dir = os.path.join(characters_dir, 'Ninja Frog')
mask_dude_dir = os.path.join(characters_dir, 'Mask Dude')
pink_man_dir = os.path.join(characters_dir, 'Pink Man')

turtle_dir = os.path.join(enemies_dir, 'Turtle')
bird_dir = os.path.join(enemies_dir, 'Bird')

dust_particle = pygame.image.load(os.path.join(other_textures_dir, 'Dust_particle.png'))

music = os.path.join(audio_dir, 'ThePirateAndTheDancer.mp3')
jump_sound = pygame.mixer.Sound(os.path.join(player_audio_dir, 'Jump.wav'))
game_over_sound = pygame.mixer.Sound(os.path.join(player_audio_dir, 'game_over.wav'))

icon = pygame.image.load(os.path.join(ui_dir, 'Icon.png'))

cursor1 = pygame.image.load(os.path.join(ui_dir, 'Cursor.png'))
cursor2 = pygame.image.load(os.path.join(ui_dir, 'Cursor1.png'))
cursor_files = [cursor1, cursor2]

ground_ends = pygame.image.load(os.path.join(grounds_dir, 'Ground_Ends.png'))
grass_base = pygame.image.load(os.path.join(grounds_dir, 'Grass_Base.png'))

green_sky = pygame.image.load(os.path.join(backgrounds_dir, 'Green.png'))

vr_guy_run_1 = pygame.image.load(os.path.join(vr_guy_dir, 'Run1.png'))
vr_guy_run_2 = pygame.image.load(os.path.join(vr_guy_dir, 'Run2.png'))
vr_guy_run_3 = pygame.image.load(os.path.join(vr_guy_dir, 'Run3.png'))
vr_guy_run_4 = pygame.image.load(os.path.join(vr_guy_dir, 'Run4.png'))
vr_guy_run_5 = pygame.image.load(os.path.join(vr_guy_dir, 'Run5.png'))
vr_guy_run_6 = pygame.image.load(os.path.join(vr_guy_dir, 'Run6.png'))
vr_guy_run_7 = pygame.image.load(os.path.join(vr_guy_dir, 'Run7.png'))
vr_guy_run_8 = pygame.image.load(os.path.join(vr_guy_dir, 'Run8.png'))
vr_guy_run_9 = pygame.image.load(os.path.join(vr_guy_dir, 'Run9.png'))
vr_guy_run_10 = pygame.image.load(os.path.join(vr_guy_dir, 'Run10.png'))
vr_guy_run_11 = pygame.image.load(os.path.join(vr_guy_dir, 'Run11.png'))
vr_guy_run_12 = pygame.image.load(os.path.join(vr_guy_dir, 'Run12.png'))
vr_guy_run = [vr_guy_run_1, vr_guy_run_2, vr_guy_run_3, vr_guy_run_4, vr_guy_run_5,
              vr_guy_run_6, vr_guy_run_7, vr_guy_run_8, vr_guy_run_9, vr_guy_run_10,
              vr_guy_run_11, vr_guy_run_12]
vr_guy_jump = pygame.image.load(os.path.join(vr_guy_dir, 'Jump.png'))
vr_guy_fall = pygame.image.load(os.path.join(vr_guy_dir, 'Fall.png'))
vr_guy_files = [vr_guy_run, vr_guy_jump, vr_guy_fall]

ninja_frog_run_1 = pygame.image.load(os.path.join(ninja_frog_dir, 'Run1.png'))
ninja_frog_run_2 = pygame.image.load(os.path.join(ninja_frog_dir, 'Run2.png'))
ninja_frog_run_3 = pygame.image.load(os.path.join(ninja_frog_dir, 'Run3.png'))
ninja_frog_run_4 = pygame.image.load(os.path.join(ninja_frog_dir, 'Run4.png'))
ninja_frog_run_5 = pygame.image.load(os.path.join(ninja_frog_dir, 'Run5.png'))
ninja_frog_run_6 = pygame.image.load(os.path.join(ninja_frog_dir, 'Run6.png'))
ninja_frog_run_7 = pygame.image.load(os.path.join(ninja_frog_dir, 'Run7.png'))
ninja_frog_run_8 = pygame.image.load(os.path.join(ninja_frog_dir, 'Run8.png'))
ninja_frog_run_9 = pygame.image.load(os.path.join(ninja_frog_dir, 'Run9.png'))
ninja_frog_run_10 = pygame.image.load(os.path.join(ninja_frog_dir, 'Run10.png'))
ninja_frog_run_11 = pygame.image.load(os.path.join(ninja_frog_dir, 'Run11.png'))
ninja_frog_run_12 = pygame.image.load(os.path.join(ninja_frog_dir, 'Run12.png'))
ninja_frog_run = [ninja_frog_run_1, ninja_frog_run_2, ninja_frog_run_3, ninja_frog_run_4, ninja_frog_run_5,
                  ninja_frog_run_6, ninja_frog_run_7, ninja_frog_run_8, ninja_frog_run_9, ninja_frog_run_10,
                  ninja_frog_run_11, ninja_frog_run_12]
ninja_frog_jump = pygame.image.load(os.path.join(ninja_frog_dir, 'Jump.png'))
ninja_frog_fall = pygame.image.load(os.path.join(ninja_frog_dir, 'Fall.png'))
ninja_frog_files = [ninja_frog_run, ninja_frog_jump, ninja_frog_fall]

mask_dude_run_1 = pygame.image.load(os.path.join(mask_dude_dir, 'Run1.png'))
mask_dude_run_2 = pygame.image.load(os.path.join(mask_dude_dir, 'Run2.png'))
mask_dude_run_3 = pygame.image.load(os.path.join(mask_dude_dir, 'Run3.png'))
mask_dude_run_4 = pygame.image.load(os.path.join(mask_dude_dir, 'Run4.png'))
mask_dude_run_5 = pygame.image.load(os.path.join(mask_dude_dir, 'Run5.png'))
mask_dude_run_6 = pygame.image.load(os.path.join(mask_dude_dir, 'Run6.png'))
mask_dude_run_7 = pygame.image.load(os.path.join(mask_dude_dir, 'Run7.png'))
mask_dude_run_8 = pygame.image.load(os.path.join(mask_dude_dir, 'Run8.png'))
mask_dude_run_9 = pygame.image.load(os.path.join(mask_dude_dir, 'Run9.png'))
mask_dude_run_10 = pygame.image.load(os.path.join(mask_dude_dir, 'Run10.png'))
mask_dude_run_11 = pygame.image.load(os.path.join(mask_dude_dir, 'Run11.png'))
mask_dude_run_12 = pygame.image.load(os.path.join(mask_dude_dir, 'Run12.png'))
mask_dude_run = [mask_dude_run_1, mask_dude_run_2, mask_dude_run_3, mask_dude_run_4, mask_dude_run_5,
                 mask_dude_run_6, mask_dude_run_7, mask_dude_run_8, mask_dude_run_9, mask_dude_run_10,
                 mask_dude_run_11, mask_dude_run_12]
mask_dude_jump = pygame.image.load(os.path.join(mask_dude_dir, 'Jump.png'))
mask_dude_fall = pygame.image.load(os.path.join(mask_dude_dir, 'Fall.png'))
mask_dude_files = [mask_dude_run, mask_dude_jump, mask_dude_fall]

pink_man_run_1 = pygame.image.load(os.path.join(pink_man_dir, 'Run1.png'))
pink_man_run_2 = pygame.image.load(os.path.join(pink_man_dir, 'Run2.png'))
pink_man_run_3 = pygame.image.load(os.path.join(pink_man_dir, 'Run3.png'))
pink_man_run_4 = pygame.image.load(os.path.join(pink_man_dir, 'Run4.png'))
pink_man_run_5 = pygame.image.load(os.path.join(pink_man_dir, 'Run5.png'))
pink_man_run_6 = pygame.image.load(os.path.join(pink_man_dir, 'Run6.png'))
pink_man_run_7 = pygame.image.load(os.path.join(pink_man_dir, 'Run7.png'))
pink_man_run_8 = pygame.image.load(os.path.join(pink_man_dir, 'Run8.png'))
pink_man_run_9 = pygame.image.load(os.path.join(pink_man_dir, 'Run9.png'))
pink_man_run_10 = pygame.image.load(os.path.join(pink_man_dir, 'Run10.png'))
pink_man_run_11 = pygame.image.load(os.path.join(pink_man_dir, 'Run11.png'))
pink_man_run_12 = pygame.image.load(os.path.join(pink_man_dir, 'Run12.png'))
pink_man_run = [pink_man_run_1, pink_man_run_2, pink_man_run_3, pink_man_run_4, pink_man_run_5,
                pink_man_run_6, pink_man_run_7, pink_man_run_8, pink_man_run_9, pink_man_run_10,
                pink_man_run_11, pink_man_run_12]
pink_man_jump = pygame.image.load(os.path.join(pink_man_dir, 'Jump.png'))
pink_man_fall = pygame.image.load(os.path.join(pink_man_dir, 'Fall.png'))
pink_man_files = [pink_man_run, pink_man_jump, pink_man_fall]

turtle_idle_type_1_1 = pygame.image.load(os.path.join(turtle_dir, 'Idle_type_1_1.png'))
turtle_idle_type_1_2 = pygame.image.load(os.path.join(turtle_dir, 'Idle_type_1_2.png'))
turtle_idle_type_1_3 = pygame.image.load(os.path.join(turtle_dir, 'Idle_type_1_3.png'))
turtle_idle_type_1_4 = pygame.image.load(os.path.join(turtle_dir, 'Idle_type_1_4.png'))
turtle_idle_type_1_5 = pygame.image.load(os.path.join(turtle_dir, 'Idle_type_1_5.png'))
turtle_idle_type_1_6 = pygame.image.load(os.path.join(turtle_dir, 'Idle_type_1_6.png'))
turtle_idle_type_1_7 = pygame.image.load(os.path.join(turtle_dir, 'Idle_type_1_7.png'))
turtle_idle_type_1_8 = pygame.image.load(os.path.join(turtle_dir, 'Idle_type_1_8.png'))
turtle_idle_type_1_9 = pygame.image.load(os.path.join(turtle_dir, 'Idle_type_1_9.png'))
turtle_idle_type_1_10 = pygame.image.load(os.path.join(turtle_dir, 'Idle_type_1_10.png'))
turtle_idle_type_1_11 = pygame.image.load(os.path.join(turtle_dir, 'Idle_type_1_11.png'))
turtle_idle_type_1_12 = pygame.image.load(os.path.join(turtle_dir, 'Idle_type_1_12.png'))
turtle_idle_type_1_13 = pygame.image.load(os.path.join(turtle_dir, 'Idle_type_1_13.png'))
turtle_idle_type_1_14 = pygame.image.load(os.path.join(turtle_dir, 'Idle_type_1_14.png'))
turtle_files = [turtle_idle_type_1_1, turtle_idle_type_1_2, turtle_idle_type_1_3, turtle_idle_type_1_4,
                turtle_idle_type_1_5, turtle_idle_type_1_6, turtle_idle_type_1_7, turtle_idle_type_1_8,
                turtle_idle_type_1_9, turtle_idle_type_1_10, turtle_idle_type_1_11, turtle_idle_type_1_12,
                turtle_idle_type_1_13, turtle_idle_type_1_14]

bird_fly_1 = pygame.image.load(os.path.join(bird_dir, 'Flying1.png'))
bird_fly_2 = pygame.image.load(os.path.join(bird_dir, 'Flying2.png'))
bird_fly_3 = pygame.image.load(os.path.join(bird_dir, 'Flying3.png'))
bird_fly_4 = pygame.image.load(os.path.join(bird_dir, 'Flying4.png'))
bird_fly_5 = pygame.image.load(os.path.join(bird_dir, 'Flying5.png'))
bird_fly_6 = pygame.image.load(os.path.join(bird_dir, 'Flying6.png'))
bird_fly_7 = pygame.image.load(os.path.join(bird_dir, 'Flying7.png'))
bird_fly_8 = pygame.image.load(os.path.join(bird_dir, 'Flying8.png'))
bird_fly_9 = pygame.image.load(os.path.join(bird_dir, 'Flying9.png'))
bird_files = [bird_fly_1, bird_fly_2, bird_fly_3, bird_fly_4, bird_fly_5, bird_fly_6, bird_fly_7, bird_fly_8,
              bird_fly_9]


font_default = pygame.font.Font(os.path.join(font_dir, 'Pixelar.ttf'), 30)
font_big = pygame.font.Font(os.path.join(font_dir, 'Pixelar.ttf'), 50)
font_small = pygame.font.Font(os.path.join(font_dir, 'Pixelar.ttf'), 25)


def save_data(data):
    with open(os.path.join(save_dir, 's.bin'), 'w') as save_file:
        json.dump(data, save_file)


def get_save_data():
    with open(os.path.join(save_dir, 's.bin')) as save_file:
        return json.load(save_file)


def get_vr_guy_files():
    return vr_guy_files


def get_ninja_frog_files():
    return ninja_frog_files


def get_mask_dude_files():
    return mask_dude_files


def get_pink_man_files():
    return pink_man_files


def get_turtle_files():
    return turtle_files


def get_bird_files():
    return bird_files

def get_dust_particle_file():
    return dust_particle


def get_ground_ends_file():
    return ground_ends


def get_grass_base_file():
    return grass_base


def get_green_sky():
    return green_sky


def get_cursor_files():
    return cursor_files


def get_icon_file():
    return icon


def get_font_default():
    return font_default


def get_font_big():
    return font_big


def get_font_small():
    return font_small


def get_music():
    return music


def get_jump_sound():
    return jump_sound


def get_game_over_sound():
    return game_over_sound
