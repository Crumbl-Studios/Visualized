import pygame

import uiHandler
import eventHandler
import playerHandler
import fileHandler

from sys import exit

pygame.init()

pygame.mixer.music.load(fileHandler.get_music())
jump_sound = fileHandler.get_jump_sound()

pygame.mixer.music.set_volume(1)
# pygame.mixer.music.play()

width = 800
height = 400
screen = pygame.display.set_mode((width, height))

icon = fileHandler.get_icon_file().convert()
pygame.display.set_caption('Visualized')
pygame.display.set_icon(icon)

pygame.mouse.set_visible(False)
cursors = fileHandler.get_cursor_files()
cursors[0] = cursors[0].convert_alpha()
cursors[1] = cursors[1].convert_alpha()
cursor_state = 0
cursor_img_rect = cursors[cursor_state].get_rect()

ground_ends = fileHandler.get_ground_ends_file().convert()
grass_base = fileHandler.get_grass_base_file().convert()
grass_base_x = 2

green_sky = fileHandler.get_green_sky().convert()
green_sky_x = 0

iterator = -1
vr_guy_run = fileHandler.get_vr_guy_files()[0]
for frame in vr_guy_run:
    iterator += 1
    vr_guy_run[iterator].convert_alpha()

vr_guy_jump = fileHandler.get_vr_guy_files()[1].convert_alpha()
vr_guy_fall = fileHandler.get_vr_guy_files()[2].convert_alpha()

iterator = -1
ninja_frog_run = fileHandler.get_ninja_frog_files()[0]
for frame in ninja_frog_run:
    iterator += 1
    ninja_frog_run[iterator].convert_alpha()

ninja_frog_jump = fileHandler.get_ninja_frog_files()[1].convert_alpha()
ninja_frog_fall = fileHandler.get_ninja_frog_files()[2].convert_alpha()

iterator = -1
mask_dude_run = fileHandler.get_mask_dude_files()[0]
for frame in mask_dude_run:
    iterator += 1
    mask_dude_run[iterator].convert_alpha()

mask_dude_jump = fileHandler.get_mask_dude_files()[1].convert_alpha()
mask_dude_fall = fileHandler.get_mask_dude_files()[2].convert_alpha()

iterator = -1
pink_man_run = fileHandler.get_pink_man_files()[0]
for frame in pink_man_run:
    iterator += 1
    pink_man_run[iterator].convert_alpha()

pink_man_jump = fileHandler.get_pink_man_files()[1].convert_alpha()
pink_man_fall = fileHandler.get_pink_man_files()[2].convert_alpha()

turtle = fileHandler.get_turtle_files().convert_alpha()
turtle_rect = turtle.get_rect()
turtle_x = 810

font = fileHandler.get_font()
score = 0
speed_multiplier = 1
game_state = 1

character = 'mask_dude'
if character == 'vr_guy':
    player = pygame.sprite.GroupSingle(playerHandler.Player(vr_guy_run, vr_guy_fall, vr_guy_jump, jump_sound, 284))
elif character == 'ninja_frog':
    player = pygame.sprite.GroupSingle(playerHandler.Player(ninja_frog_run, ninja_frog_fall, ninja_frog_jump,
                                                            jump_sound, 284))
elif character == 'mask_dude':
    player = pygame.sprite.GroupSingle(playerHandler.Player(mask_dude_run, mask_dude_fall, mask_dude_jump,
                                                            jump_sound, 284))
elif character == 'pink_man':
    player = pygame.sprite.GroupSingle(playerHandler.Player(pink_man_run, pink_man_fall, pink_man_jump,
                                                            jump_sound, 284))
else:
    player = pygame.sprite.GroupSingle(playerHandler.Player(vr_guy_run, vr_guy_fall, vr_guy_jump, jump_sound, 284))

clock = pygame.time.Clock()
get_ticks_last_frame = 0

while 1:
    t = pygame.time.get_ticks()
    # deltaTime in seconds.
    delta_time = (t - get_ticks_last_frame) / 1000.0
    get_ticks_last_frame = t

    if game_state == 1:
        screen.fill("#FFFFFF")
        uiHandler.drawText(screen, width/2, 30, font, "Visualized")
        #game_state = 2

    if game_state == 2:
        if speed_multiplier < 1.5:
            speed_multiplier += .0001
        else:
            speed_multiplier = speed_multiplier

        score += 10 * delta_time
        '''
        events = eventHandler.getEvents()
    
        if "terminate" in events:
            pygame.quit()
            exit()
    
        if "mouse_button_down" in events:
            cursor_state = 1
        if "mouse_button_up" in events:
            cursor_state = 0
        '''
        screen.blit(green_sky, (green_sky_x, 0))
        screen.blit(grass_base, (grass_base_x, 284))
        screen.blit(ground_ends, (0, 284))
        screen.blit(ground_ends, (797, 284))

        turtle_x -= 340 * speed_multiplier * delta_time
        turtle_rect.bottomleft = (turtle_x, 284)
        if turtle_x <= -100:
            turtle_x = 810
        screen.blit(turtle, turtle_rect)

        grass_base_x -= 340 * speed_multiplier * delta_time
        green_sky_x -= 112.2 * speed_multiplier * delta_time
        if grass_base_x <= -790:
            grass_base_x = 2
        if green_sky_x <= -790:
            green_sky_x = 0

        uiHandler.drawTextMidRight(screen, width-20, 30, font, '%05d' % (int('00000')+score))

        cursor_img_rect.center = pygame.mouse.get_pos()

        if cursor_state == 1:
            screen.blit(cursors[1], cursor_img_rect)
        elif cursor_state == 0:
            screen.blit(cursors[0], cursor_img_rect)

        player.update(speed_multiplier, delta_time)
        player.draw(screen)

    if game_state == 3:
        score = 0
        game_state = 2
        # pygame.quit()
        # exit()

    pygame.display.flip()
    clock.tick(60)
