# Third-party libraries
import pygame

# Custom Game Development Tools
import fileHandler
import uiHandler
import eventHandler
import particleHandler
import playerHandler
import enemyHandler


# Standard libraries
import random
from sys import exit

pygame.init()

# Setup audio
pygame.mixer.music.load(fileHandler.get_music())
game_over_sound = fileHandler.get_game_over_sound()
jump_sound = fileHandler.get_jump_sound()
pause_sound = fileHandler.get_pause_sound()
select_sound = fileHandler.get_select_sound()
click_sound = fileHandler.get_click_sound()

pygame.mixer.music.set_volume(.5)
pause_sound.set_volume(.5)
select_sound.set_volume(.5)
click_sound.set_volume(.5)
# pygame.mixer.music.play(-1, 1000)

# Setup pygame window
width = 800
height = 400
screen = pygame.display.set_mode((width, height))

icon = fileHandler.get_icon_file().convert()
pygame.display.set_caption('Visualized')
pygame.display.set_icon(icon)

# Initial cursor setup
pygame.mouse.set_visible(False)
cursors = fileHandler.get_cursor_files()
cursors[0] = cursors[0].convert_alpha()
cursors[1] = cursors[1].convert_alpha()
cursor_state = 0
cursor_img_rect = cursors[cursor_state].get_rect()


# Function to convert all frames of an animation
def convert_animation(animation):
    converted_animation = []
    i = -1
    for _ in animation:
        i += 1
        converted_animation.append(animation[i].convert_alpha())
    return converted_animation


# Setup character and enemy files
vr_guy_run = convert_animation(fileHandler.get_vr_guy_files()[0])
vr_guy_jump = fileHandler.get_vr_guy_files()[1].convert_alpha()
vr_guy_fall = fileHandler.get_vr_guy_files()[2].convert_alpha()

ninja_frog_run = convert_animation(fileHandler.get_ninja_frog_files()[0])
ninja_frog_jump = fileHandler.get_ninja_frog_files()[1].convert_alpha()
ninja_frog_fall = fileHandler.get_ninja_frog_files()[2].convert_alpha()

mask_dude_run = convert_animation(fileHandler.get_mask_dude_files()[0])
mask_dude_jump = fileHandler.get_mask_dude_files()[1].convert_alpha()
mask_dude_fall = fileHandler.get_mask_dude_files()[2].convert_alpha()

purple_man_run = convert_animation(fileHandler.get_purple_man_files()[0])
purple_man_jump = fileHandler.get_purple_man_files()[1].convert_alpha()
purple_man_fall = fileHandler.get_purple_man_files()[2].convert_alpha()

turtle_idle_1 = convert_animation(fileHandler.get_turtle_files()[0])
turtle_spawn = convert_animation(fileHandler.get_turtle_files()[1])

bird_fly = convert_animation(fileHandler.get_bird_files())

chameleon_run = convert_animation(fileHandler.get_chameleon_files())

mushroom_run = convert_animation(fileHandler.get_mushroom_files())

chicken_run = convert_animation(fileHandler.get_chicken_files())

radish_fly = convert_animation(fileHandler.get_radish_files())

ghost_idle = convert_animation(fileHandler.get_ghost_files())

bat_fly = convert_animation(fileHandler.get_bat_files())

# Setup font files
font_default = fileHandler.get_font_default()
font_big = fileHandler.get_font_big()
font_small = fileHandler.get_font_small()

# Initial terrain/floor setup
grass_floor = fileHandler.get_grass_floor_file().convert()
mythic_floor = fileHandler.get_mythic_floor_file().convert()
hay_floor = fileHandler.get_hay_floor_file().convert()
floor = grass_floor
floor_x = 0

# Initial sky setup
green_sky = fileHandler.get_green_sky().convert()
purple_sky = fileHandler.get_purple_sky().convert()
brown_sky = fileHandler.get_brown_sky().convert()
sky = green_sky
sky_x = 0

# Load in dust-particle for effects
dust_particle_file = fileHandler.get_dust_particle_file()

# Character and enemy group creation
character = 'purple_man'
if character == 'vr_guy':
    player = pygame.sprite.GroupSingle(playerHandler.Player(screen, dust_particle_file, vr_guy_run, vr_guy_fall,
                                                            vr_guy_jump, jump_sound, 284))
elif character == 'ninja_frog':
    player = pygame.sprite.GroupSingle(playerHandler.Player(screen, dust_particle_file, ninja_frog_run, ninja_frog_fall,
                                                            ninja_frog_jump, jump_sound, 284))
elif character == 'mask_dude':
    player = pygame.sprite.GroupSingle(playerHandler.Player(screen, dust_particle_file, mask_dude_run, mask_dude_fall,
                                                            mask_dude_jump, jump_sound, 284))
elif character == 'purple_man':
    player = pygame.sprite.GroupSingle(playerHandler.Player(screen, dust_particle_file, purple_man_run, purple_man_fall,
                                                            purple_man_jump, jump_sound, 284))
else:
    player = pygame.sprite.GroupSingle(playerHandler.Player(screen, dust_particle_file, vr_guy_run, vr_guy_fall,
                                                            vr_guy_jump, jump_sound, 284))


enemy_group = pygame.sprite.Group()
enemy_id_number = 0  # To identify different enemies

# Setup pygame clock
clock = pygame.time.Clock()

# Initial level system setup
score = 0
high_score = score

level = 1
speed_multiplier_default = 1
speed_multiplier = speed_multiplier_default
speed_multiplier_limit = 1.5

spawn_rate_default = 1500
spawn_rate = spawn_rate_default

timer_set = False
level_set = False

saved_save_data = {"score": 0}  # Previously saved score
save_data = {"score": 0}  # Current saved score

# UI Setup
previous_game_state = ""  # Acts as a return-button
game_state = "title_screen"
selected = 0  # Identifies which button on screen is being hovered over

selected_box_color = "#2596be"
selected_text_color = "#ffffff"
box_color = "#ffffff"
text_color = "#2596be"

esc_hit = False
esc_hit_time = 0

get_ticks_last_frame = 0  # Used to calculate delta-time

death_time = 0

enemy_timer = pygame.USEREVENT + 1  # Creates a timer to be used with enemy spawning

dust_particle = particleHandler.Particle()  # Creates a particle object
while 1:
    t = pygame.time.get_ticks()
    delta_time = (t - get_ticks_last_frame) / 1000.0
    get_ticks_last_frame = t

    events = eventHandler.get_events()

    if "terminate" in events:
        if saved_save_data["score"] <= save_data["score"]:
            fileHandler.save_data(save_data)
        pygame.quit()
        exit()

    if "mouse_button_down" in events:
        cursor_state = 1
    if "mouse_button_up" in events:
        cursor_state = 0

    if game_state == "title_screen":
        saved_save_data = fileHandler.get_save_data(saved_save_data)

        sky_x -= 112.2 * speed_multiplier * delta_time
        if sky_x <= -700:
            sky_x = 0
        screen.blit(sky, (sky_x, 0))

        uiHandler.draw_text(screen, width / 2, height / 2, font_big, "Visualized")
        uiHandler.draw_text(screen, width / 2, height / 2 + 125, font_default, "Press jump to start")

        cursor_img_rect.center = pygame.mouse.get_pos()
        if cursor_state == 1:
            screen.blit(cursors[1], cursor_img_rect)
        elif cursor_state == 0:
            screen.blit(cursors[0], cursor_img_rect)

        if "jump_key_down" in events:
            pygame.mixer.Sound.play(click_sound)
            events.clear()
            previous_game_state = "title_screen"
            game_state = "game"

    if game_state == "game":
        if speed_multiplier < speed_multiplier_limit:
            speed_multiplier += .01*delta_time
        else:
            speed_multiplier = speed_multiplier

        score += 10 * delta_time

        if level == 1:
            speed_multiplier_limit = 1.5
            spawn_rate = 1500
            floor = grass_floor
            sky = green_sky
            if not timer_set:
                pygame.time.set_timer(enemy_timer, spawn_rate)
                timer_set = True
        elif level == 2:
            speed_multiplier_limit = 1.75
            spawn_rate = 1312
            floor = hay_floor
            sky = brown_sky
            if not timer_set:
                pygame.time.set_timer(enemy_timer, spawn_rate)
                timer_set = True
        elif level == 3:
            speed_multiplier_limit = 2
            spawn_rate = 937
            floor = mythic_floor
            sky = purple_sky
            if not timer_set:
                pygame.time.set_timer(enemy_timer, spawn_rate)
                timer_set = True
        elif level == 4:
            speed_multiplier_limit = 2.25
            spawn_rate = 750
            floor = mythic_floor
            sky = purple_sky
            if not timer_set:
                pygame.time.set_timer(enemy_timer, spawn_rate)
                timer_set = True

        if 250 < score < 750:
            level = 2
            if level_set != 1:
                level_set = 1
                timer_set = False
        elif 750 < score < 2000:
            level = 3
            if level_set != 2:
                level_set = 2
                timer_set = False
        elif 2000 < score:
            level = 4
            if level_set != 3:
                level_set = 3
                timer_set = False
        else:
            level = 1

        screen.blit(sky, (sky_x, 0))
        screen.blit(floor, (floor_x, 284))

        if "user_event_1" in events:
            enemy_id_number += 1
            if level == 1:
                randint = random.randint(0, 1)
                if randint == 0:
                    enemy_group.add(enemyHandler.Enemy("land", 284, 180, width, mushroom_run, enemy_id_number,
                                                       enemy_group=enemy_group))
                elif randint == 1:
                    enemy_group.add(enemyHandler.Enemy("land", 284, 180, width, chameleon_run, enemy_id_number,
                                                       enemy_group=enemy_group))
            if level == 2:
                randint = random.randint(0, 1)
                if randint == 0:
                    enemy_group.add(enemyHandler.Enemy("land", 284, 180, width, chicken_run, enemy_id_number,
                                                       enemy_group=enemy_group))
                elif randint == 1:
                    enemy_group.add(enemyHandler.Enemy("air", 284, 180, width, radish_fly, enemy_id_number,
                                                       enemy_group=enemy_group))
            if level == 3:
                randint = random.randint(0, 1)
                if randint == 0:
                    enemy_group.add(enemyHandler.Enemy("land", 284, 180, width, ghost_idle, enemy_id_number,
                                                       enemy_group=enemy_group))
                elif randint == 1:
                    enemy_group.add(enemyHandler.Enemy("air", 284, 180, width, bat_fly, enemy_id_number,
                                                       enemy_group=enemy_group))
            if level == 4:
                randint = random.randint(0, 7)
                if randint == 0:
                    enemy_group.add(enemyHandler.Enemy("land", 284, 180, width, mushroom_run, enemy_id_number,
                                                       enemy_group=enemy_group))
                elif randint == 1:
                    enemy_group.add(enemyHandler.Enemy("land", 284, 180, width, chameleon_run, enemy_id_number,
                                                       enemy_group=enemy_group))
                elif randint == 2:
                    enemy_group.add(enemyHandler.Enemy("land", 284, 180, width, chicken_run, enemy_id_number,
                                                       enemy_group=enemy_group))
                elif randint == 3:
                    enemy_group.add(enemyHandler.Enemy("air", 284, 180, width, radish_fly, enemy_id_number,
                                                       enemy_group=enemy_group))
                elif randint == 4:
                    enemy_group.add(enemyHandler.Enemy("land", 284, 180, width, ghost_idle, enemy_id_number,
                                                       enemy_group=enemy_group))
                elif randint == 5:
                    enemy_group.add(enemyHandler.Enemy("air", 284, 180, width, bat_fly, enemy_id_number,
                                                       enemy_group=enemy_group))
                elif randint == 6:
                    enemy_group.add(enemyHandler.Enemy("land", 284, 180, width, turtle_idle_1, enemy_id_number,
                                                       enemy_group=enemy_group))
                elif randint == 7:
                    enemy_group.add(enemyHandler.Enemy("air", 284, 180, width, bird_fly, enemy_id_number,
                                                       enemy_group=enemy_group))

        floor_x -= 340 * speed_multiplier * delta_time
        sky_x -= 112.2 * speed_multiplier * delta_time
        if floor_x <= -790:
            floor_x = 2
        if sky_x <= -700:
            sky_x = 0

        score_text, score_text_rect = uiHandler.get_text(font_big, '%05d' % (int('00000') + score))
        score_text_rect.midright = width - 20, 30
        screen.blit(score_text, score_text_rect)

        # noinspection PyTypeChecker
        if pygame.sprite.spritecollide(player.sprite, enemy_group, False, pygame.sprite.collide_mask):
            pygame.mixer.Sound.play(game_over_sound)
            death_time = pygame.time.get_ticks()/1000

            previous_game_state = "game"
            game_state = "game_over"

        save_data = {"score": score}

        player.update(speed_multiplier, delta_time, events)
        player.draw(screen)

        enemy_group.draw(screen)
        enemy_group.update(speed_multiplier, delta_time)

    if game_state == "pause_menu":
        screen.blit(sky, (sky_x, 0))

        if previous_game_state == "game":
            player.draw(screen)
            enemy_group.draw(screen)
            screen.blit(floor, (floor_x, 284))

            score_text, score_text_rect = uiHandler.get_text(font_big, '%05d' % (int('00000') + score))
            score_text_rect.midright = width - 20, 30
            screen.blit(score_text, score_text_rect)

        uiHandler.draw_text(screen, width / 2, height / 2 - 75, font_big, "Game Paused")

        if "down_key_down" in events:
            selected += 1
            if "enter_key_down" not in events:
                pygame.mixer.Sound.play(select_sound)

        if "jump_key_down" in events:
            selected -= 1
            if "enter_key_down" not in events:
                pygame.mixer.Sound.play(select_sound)

        if selected == 3:
            selected = 0
        if selected == -1:
            selected = 2

        if selected == 0:
            uiHandler.draw_rectangle(screen, 105, 55, width / 2 - 52.5, height / 2 - 2.5, transparent=False,
                                     rgb="#000000")

            uiHandler.draw_rectangle(screen, 100, 50, width / 2 - 50, height / 2, transparent=False,
                                     rgb=selected_box_color)
            uiHandler.draw_text(screen, width / 2, height / 2 + 25, font_default, "Resume", rgb=selected_text_color)

            uiHandler.draw_rectangle(screen, 100, 50, width/2-50, height/2+60, transparent=False, rgb=box_color)
            uiHandler.draw_text(screen, width/2, height/2+85, font_default, "Restart", rgb=text_color)

            uiHandler.draw_rectangle(screen, 100, 50, width/2-50, height/2+120, transparent=False, rgb=box_color)
            uiHandler.draw_text(screen, width/2, height/2+145, font_default, "Quit", rgb=text_color)

            if "enter_key_down" in events:
                pygame.mixer.Sound.play(click_sound)
                game_state = previous_game_state

        elif selected == 1:
            uiHandler.draw_rectangle(screen, 105, 55, width / 2 - 52.5, height / 2 + 60 - 2.5, transparent=False,
                                     rgb="#000000")

            uiHandler.draw_rectangle(screen, 100, 50, width/2-50, height/2, transparent=False, rgb=box_color)
            uiHandler.draw_text(screen, width/2, height/2+25, font_default, "Resume", rgb=text_color)

            uiHandler.draw_rectangle(screen, 100, 50, width/2-50, height/2+60, transparent=False,
                                     rgb=selected_box_color)
            uiHandler.draw_text(screen, width/2, height/2+85, font_default, "Restart", rgb=selected_text_color)

            uiHandler.draw_rectangle(screen, 100, 50, width/2-50, height/2+120, transparent=False, rgb=box_color)
            uiHandler.draw_text(screen, width/2, height/2+145, font_default, "Quit", rgb=text_color)
            if "enter_key_down" in events:
                pygame.mixer.Sound.play(click_sound)
                score = 0
                speed_multiplier = speed_multiplier_default
                spawn_rate = spawn_rate_default
                sky = green_sky
                floor = grass_floor
                player.sprite.rect.y = 284
                enemy_group.empty()

                game_state = "game"

        elif selected == 2:
            uiHandler.draw_rectangle(screen, 105, 55, width / 2 - 52.5, height / 2 + 120 - 2.5, transparent=False,
                                     rgb="#000000")

            uiHandler.draw_rectangle(screen, 100, 50, width/2-50, height/2, transparent=False, rgb=box_color)
            uiHandler.draw_text(screen, width/2, height/2+25, font_default, "Resume", rgb=text_color)

            uiHandler.draw_rectangle(screen, 100, 50, width/2-50, height/2+60, transparent=False, rgb=box_color)
            uiHandler.draw_text(screen, width/2, height/2+85, font_default, "Restart", rgb=text_color)

            uiHandler.draw_rectangle(screen, 100, 50, width/2-50, height/2+120, transparent=False,
                                     rgb=selected_box_color)
            uiHandler.draw_text(screen, width/2, height/2+145, font_default, "Quit", rgb=selected_text_color)
            if "enter_key_down" in events:
                pygame.mixer.Sound.play(click_sound)
                score = 0
                speed_multiplier = speed_multiplier_default
                spawn_rate = spawn_rate_default
                sky = green_sky
                floor = grass_floor
                player.sprite.rect.y = 284
                enemy_group.empty()

                game_state = "title_screen"

        if "esc_key_down" in events and esc_hit is False:
            pygame.mixer.Sound.play(click_sound)
            events.clear()
            game_state = previous_game_state

        cursor_img_rect.center = pygame.mouse.get_pos()

        if cursor_state == 1:
            screen.blit(cursors[1], cursor_img_rect)
        elif cursor_state == 0:
            screen.blit(cursors[0], cursor_img_rect)

        esc_hit = False

    if "esc_key_down" in events:
        pygame.mixer.Sound.play(pause_sound)

        previous_game_state = game_state
        game_state = "pause_menu"
        esc_hit = True

    if game_state == "game_over":
        if saved_save_data["score"] <= save_data["score"]:
            fileHandler.save_data(save_data)
            saved_save_data = save_data

        sky_x -= 112.2 * speed_multiplier * delta_time
        if sky_x <= -700:
            sky_x = 0
        screen.blit(sky, (sky_x, 0))

        uiHandler.draw_text(screen, width / 2, height / 2, font_big, "Game Over")
        uiHandler.draw_text(screen, width / 2, height / 2 + 50, font_default, 'Score: '+'%05d' % (int('00000') + score))
        uiHandler.draw_text(screen, width / 2, height / 2 + 75, font_small,
                            'High score: '+'%05d' % (int('00000') + int(saved_save_data["score"])))

        uiHandler.draw_text(screen, width / 2, height / 2 + 125, font_default, "Press jump to restart")

        if "jump_key_down" in events and pygame.time.get_ticks()/1000 - death_time >= 1:
            pygame.mixer.Sound.play(click_sound)
            score = 0
            speed_multiplier = speed_multiplier_default
            spawn_rate = spawn_rate_default
            sky = green_sky
            floor = grass_floor
            player.sprite.rect.y = 284
            enemy_group.empty()

            game_state = "game"

        cursor_img_rect.center = pygame.mouse.get_pos()
        if cursor_state == 1:
            screen.blit(cursors[1], cursor_img_rect)
        elif cursor_state == 0:
            screen.blit(cursors[0], cursor_img_rect)

    pygame.display.flip()
    clock.tick(60)
