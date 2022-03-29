# Third-party libraries
import pygame

# Custom Game Development Tools
import fileHandler
import uiHandler
import eventHandler
import particleHandler
import playerHandler
import enemyHandler
import coinHandler

# Standard libraries
import random
from sys import exit

pygame.init()

# Setup audio
pygame.mixer.music.load(fileHandler.get_music())
game_over_sound = fileHandler.get_game_over_sound()
jump_sound = fileHandler.get_jump_sound()
pause_sound = fileHandler.get_pause_sound()
hover_sound = fileHandler.get_hover_sound()
click_sound = fileHandler.get_click_sound()

pygame.mixer.music.set_volume(.5)
pause_sound.set_volume(.5)
hover_sound.set_volume(.5)
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
appear = fileHandler.get_appear_animation()
disappear = fileHandler.get_disappear_animation()

vr_guy_run = convert_animation(fileHandler.get_vr_guy_files()[0])
vr_guy_jump = fileHandler.get_vr_guy_files()[1].convert_alpha()
vr_guy_fall = fileHandler.get_vr_guy_files()[2].convert_alpha()
vr_guy = [vr_guy_run, vr_guy_jump, vr_guy_fall]

ninja_frog_run = convert_animation(fileHandler.get_ninja_frog_files()[0])
ninja_frog_jump = fileHandler.get_ninja_frog_files()[1].convert_alpha()
ninja_frog_fall = fileHandler.get_ninja_frog_files()[2].convert_alpha()
ninja_frog = [ninja_frog_run, ninja_frog_jump, ninja_frog_fall]

mask_dude_run = convert_animation(fileHandler.get_mask_dude_files()[0])
mask_dude_jump = fileHandler.get_mask_dude_files()[1].convert_alpha()
mask_dude_fall = fileHandler.get_mask_dude_files()[2].convert_alpha()
mask_dude = [mask_dude_run, mask_dude_jump, mask_dude_fall]

purple_man_run = convert_animation(fileHandler.get_purple_man_files()[0])
purple_man_jump = fileHandler.get_purple_man_files()[1].convert_alpha()
purple_man_fall = fileHandler.get_purple_man_files()[2].convert_alpha()
purple_man = [purple_man_run, purple_man_jump, purple_man_fall]

coin_animation = convert_animation(fileHandler.get_coin_files())
collected_animation = convert_animation(fileHandler.get_collected_files())

coin = fileHandler.get_coin_icon()
coin_rect = coin.get_rect()
coin_rect_2 = coin.get_rect()

coin_rect.midright = width-190, 30+4
coin_rect_2.midright = width-70, 30+4

coin_text_pos = width-220, 30
coin_text_pos_2 = width-100, 30

coin_text_color = "#f7e476"

collect_sound = fileHandler.get_collect_sound()

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
stone_floor = fileHandler.get_stone_floor_file().convert()
floor = grass_floor
floor_x = 0

# Initial sky setup
green_sky = fileHandler.get_green_sky().convert()
purple_sky = fileHandler.get_purple_sky().convert()
brown_sky = fileHandler.get_brown_sky().convert()
mint_sky = fileHandler.get_mint_sky().convert()
blue_purple_sky = fileHandler.get_blue_purple_sky().convert()
blue_purple_2_sky = fileHandler.get_blue_purple_2_sky().convert()

sky = green_sky
sky_x = 0

# Character, enemy, and coin group creation
characters = [appear, disappear, ninja_frog, purple_man, mask_dude, vr_guy]
player = pygame.sprite.GroupSingle(playerHandler.Player(screen, characters, jump_sound, 284))

enemy_group = pygame.sprite.Group()
enemy_id = 0  # To identify different enemies

coin_group = pygame.sprite.Group()
coin_id = 0
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

save_data_layout = {"score": 0, "coins": 0}  # Layout for player data to be saved in
previous_save_data = fileHandler.get_save_data(save_data_layout)  # Previously saved data
save_data = save_data_layout  # Current saved data

coins = previous_save_data["coins"]

# UI Setup
previous_game_state = ""  # Acts as a return-button
game_state = "title_screen"
selected = 0  # Identifies which button on screen is being hovered over

outline_color = "#000000"
selected_box_color = "#2596be"
selected_text_color = "#ffffff"
box_color = "#ffffff"
text_color = "#2596be"

settings_button = uiHandler.Button(font_small, 45, 45, 10, 10, 6, hover_sound=hover_sound, click_sound=click_sound,
                                   text="S", active=False)
play_button = uiHandler.Button(font_small, 100, 45, width/2-50, height/2+60, 6, hover_sound=hover_sound,
                               click_sound=click_sound,
                               text="Play", active=False)
shop_button = uiHandler.Button(font_small, 100, 45, width/2-50, height/2+120, 6, hover_sound=hover_sound,
                               click_sound=click_sound,
                               text="Shop", active=False)

resume_button = uiHandler.Button(font_default, 100, 50, width/2-50, height/2, 6, hover_sound=hover_sound,
                                 click_sound=click_sound, text="Resume", active=False)
restart_button = uiHandler.Button(font_default, 100, 50, width/2-50, height/2+60, 6, hover_sound=hover_sound,
                                  click_sound=click_sound, text="Restart", active=False)
quit_button = uiHandler.Button(font_default, 100, 50, width/2-50, height/2+120, 6, hover_sound=hover_sound,
                               click_sound=click_sound, text="Quit", active=False)

credits_button = uiHandler.Button(font_default, 150, 50, width/2-75, height/2, 6, hover_sound=hover_sound,
                                  click_sound=click_sound, text="Credits", active=False)
reset_saves_button = uiHandler.Button(font_default, 150, 50, width/2-75, height/2+60, 6,
                                      hover_sound=hover_sound, click_sound=click_sound,
                                      text="Reset saves", active=False)
back_button = uiHandler.Button(font_default, 150, 50, width/2-75, height/2+120, 6, hover_sound=hover_sound,
                               click_sound=click_sound, text="Return", active=False)

skies_button = uiHandler.Button(font_small, 100, 45, width/2-50, height/2-25, 6, hover_sound=hover_sound,
                                click_sound=click_sound,
                                text="Skies", active=False)
char_button = uiHandler.Button(font_small, 100, 45, width/2-50, height/2+35, 6, hover_sound=hover_sound,
                               click_sound=click_sound,
                               text="Characters", active=False)
return_button = uiHandler.Button(font_small, 100, 45, width/2-50, height/2+95, 6, hover_sound=hover_sound,
                                 click_sound=click_sound,
                                 text="Return", active=False)

back_shops = uiHandler.Button(font_small, 100, 45, 15, 15, 6, hover_sound=hover_sound, click_sound=click_sound,
                              text="Back", active=False)

esc_hit = False
esc_hit_time = 0

get_ticks_last_frame = 0  # Used to calculate delta-time

death_time = 0

enemy_timer = pygame.USEREVENT+1  # Creates a timer to be used with enemy spawning
while 1:
    ticks = pygame.time.get_ticks()
    delta_time = (ticks-get_ticks_last_frame)/1000.0
    get_ticks_last_frame = ticks

    events = eventHandler.get_events()

    if "terminate" in events:
        if previous_save_data["score"] <= save_data["score"]:
            fileHandler.save_data(save_data)
        pygame.quit()
        exit()

    if "left_mouse_button_down" in events:
        cursor_state = 1
    if "left_mouse_button_up" in events:
        cursor_state = 0

    if game_state == "title_screen":
        sky = green_sky
        sky_x -= 112.2*speed_multiplier*delta_time
        if sky_x <= -700:
            sky_x = 0
        screen.blit(sky, (sky_x, 0))

        uiHandler.draw_text(screen, width/2, height/2, font_big, "Visualized")

        settings_button.active = True
        settings_button.update(screen, cursor_img_rect, events)

        play_button.active = True
        play_button.update(screen, cursor_img_rect, events)

        shop_button.active = True
        shop_button.update(screen, cursor_img_rect, events)

        if settings_button.clicked_up or "esc_key_down" in events:
            pygame.mixer.Sound.play(click_sound)
            settings_button.active = False
            events.clear()
            previous_game_state = game_state
            game_state = "settings"

        if shop_button.clicked_up:
            pygame.mixer.Sound.play(click_sound)
            settings_button.active = False
            events.clear()
            previous_game_state = game_state
            game_state = "shop"
        # uiHandler.draw_text(screen, width/2, height/2+150, font_default, "Press Escape for settings")

        cursor_img_rect.center = pygame.mouse.get_pos()
        if cursor_state == 1:
            screen.blit(cursors[1], cursor_img_rect)
        elif cursor_state == 0:
            screen.blit(cursors[0], cursor_img_rect)

        if play_button.clicked_up:
            pygame.mixer.Sound.play(click_sound)
            events.clear()
            previous_game_state = game_state
            game_state = "game"

    if game_state == "game":
        if speed_multiplier < speed_multiplier_limit:
            speed_multiplier += .01*delta_time
        else:
            speed_multiplier = speed_multiplier

        score += 10*delta_time

        if level == 1:
            player.sprite.character = 1
            speed_multiplier_limit = 1.5
            spawn_rate = 1500
            floor = grass_floor
            sky = green_sky
            if not timer_set:
                pygame.time.set_timer(enemy_timer, spawn_rate)
                timer_set = True
        elif level == 2:
            player.sprite.character = 2
            speed_multiplier_limit = 1.75
            spawn_rate = 1312
            floor = mythic_floor
            sky = purple_sky
            if not timer_set:
                pygame.time.set_timer(enemy_timer, spawn_rate)
                timer_set = True
        elif level == 3:
            player.sprite.character = 3
            speed_multiplier_limit = 2
            spawn_rate = 937
            floor = hay_floor
            sky = brown_sky
            if not timer_set:
                pygame.time.set_timer(enemy_timer, spawn_rate)
                timer_set = True
        elif level == 4:
            player.sprite.character = 4
            speed_multiplier_limit = 2.25
            spawn_rate = 937
            floor = stone_floor
            sky = blue_purple_sky
            if not timer_set:
                pygame.time.set_timer(enemy_timer, spawn_rate)
                timer_set = True
        if 0 < score < 250:
            level = 1
            if level_set != 0:
                level_set = 0
                timer_set = False
        elif 250 < score < 750:
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
            enemy_id += 1
            if level == 1:
                randint = random.randint(0, 5)
                if randint == 0 or randint == 1:
                    enemy_group.add(enemyHandler.Enemy("land", 284, 180, width, mushroom_run, enemy_id,
                                                       enemy_group=enemy_group))
                elif randint == 2 or randint == 3:
                    enemy_group.add(enemyHandler.Enemy("land", 284, 180, width, chameleon_run, enemy_id,
                                                       enemy_group=enemy_group))
                elif randint == 4:
                    coin_id += 1
                    coin_group.add(coinHandler.Coin("land", 284, 180, width, coin_animation, collected_animation, collect_sound, coin_id,
                                                    coin_group=coin_group))
                elif randint == 5:
                    coin_id += 1
                    coin_group.add(coinHandler.Coin("air", 284, 180, width, coin_animation, collected_animation, collect_sound, coin_id,
                                                    coin_group=coin_group))
            if level == 2:
                randint = random.randint(0, 5)
                if randint == 0 or randint == 1:
                    enemy_group.add(enemyHandler.Enemy("land", 284, 180, width, ghost_idle, enemy_id,
                                                       enemy_group=enemy_group))
                elif randint == 2 or randint == 3:
                    enemy_group.add(enemyHandler.Enemy("air", 284, 180, width, bat_fly, enemy_id,
                                                       enemy_group=enemy_group))
                elif randint == 4:
                    coin_id += 1
                    coin_group.add(coinHandler.Coin("land", 284, 180, width, coin_animation, collected_animation, collect_sound, coin_id,
                                                    coin_group=coin_group))
                elif randint == 5:
                    coin_id += 1
                    coin_group.add(coinHandler.Coin("air", 284, 180, width, coin_animation, collected_animation, collect_sound, coin_id,
                                                    coin_group=coin_group))
            if level == 3:
                randint = random.randint(0, 5)
                if randint == 0 or randint == 1:
                    enemy_group.add(enemyHandler.Enemy("land", 284, 180, width, chicken_run, enemy_id,
                                                       enemy_group=enemy_group))
                elif randint == 2 or randint == 3:
                    enemy_group.add(enemyHandler.Enemy("air", 284, 180, width, radish_fly, enemy_id,
                                                       enemy_group=enemy_group))
                elif randint == 4:
                    coin_id += 1
                    coin_group.add(coinHandler.Coin("land", 284, 180, width, coin_animation, collected_animation, collect_sound, coin_id,
                                                    coin_group=coin_group))
                elif randint == 5:
                    coin_id += 1
                    coin_group.add(coinHandler.Coin("air", 284, 180, width, coin_animation, collected_animation, collect_sound, coin_id,
                                                    coin_group=coin_group))
            if level == 4:
                randint = random.randint(0, 11)
                if randint == 0:
                    enemy_group.add(enemyHandler.Enemy("land", 284, 180, width, mushroom_run, enemy_id,
                                                       enemy_group=enemy_group))
                elif randint == 1:
                    enemy_group.add(enemyHandler.Enemy("land", 284, 180, width, chameleon_run, enemy_id,
                                                       enemy_group=enemy_group))
                elif randint == 2:
                    enemy_group.add(enemyHandler.Enemy("land", 284, 180, width, chicken_run, enemy_id,
                                                       enemy_group=enemy_group))
                elif randint == 3:
                    enemy_group.add(enemyHandler.Enemy("air", 284, 180, width, radish_fly, enemy_id,
                                                       enemy_group=enemy_group))
                elif randint == 4:
                    enemy_group.add(enemyHandler.Enemy("land", 284, 180, width, ghost_idle, enemy_id,
                                                       enemy_group=enemy_group))
                elif randint == 5:
                    enemy_group.add(enemyHandler.Enemy("air", 284, 180, width, bat_fly, enemy_id,
                                                       enemy_group=enemy_group))
                elif randint == 6 or randint == 7:
                    enemy_group.add(enemyHandler.Enemy("land", 284, 180, width, turtle_idle_1, enemy_id,
                                                       enemy_group=enemy_group))
                elif randint == 8 or randint == 9:
                    enemy_group.add(enemyHandler.Enemy("air", 284, 180, width, bird_fly, enemy_id,
                                                       enemy_group=enemy_group))
                elif randint == 10:
                    coin_id += 1
                    coin_group.add(coinHandler.Coin("land", 284, 180, width, coin_animation, collected_animation, collect_sound, coin_id,
                                                    coin_group=coin_group))
                elif randint == 11:
                    coin_id += 1
                    coin_group.add(coinHandler.Coin("air", 284, 180, width, coin_animation, collected_animation, collect_sound, coin_id,
                                                    coin_group=coin_group))

        floor_x -= 340*speed_multiplier*delta_time
        sky_x -= 112.2*speed_multiplier*delta_time
        if floor_x <= -790:
            floor_x = 2
        if sky_x <= -700:
            sky_x = 0

        if score % 250 < 0.1:
            coins += 5

        score_text, score_text_rect = uiHandler.get_text(font_big, '%05d' % (int('00000')+score))
        score_text_rect.midright = width-20, 30
        screen.blit(score_text, score_text_rect)

        screen.blit(coin, coin_rect)
        coin_text, coin_text_rect = uiHandler.get_text(font_big, '%05d' % (int('00000')+coins),
                                                         rgb=coin_text_color)
        coin_text_rect.midright = coin_text_pos
        screen.blit(coin_text, coin_text_rect)

        # noinspection PyTypeChecker
        if pygame.sprite.spritecollide(player.sprite, coin_group, False, pygame.sprite.collide_mask):
            coins += 1
        elif pygame.sprite.spritecollide(player.sprite, enemy_group, False, pygame.sprite.collide_mask):
            pygame.mixer.Sound.play(game_over_sound)
            death_time = pygame.time.get_ticks()/1000

            previous_game_state = game_state
            game_state = "game_over"

        save_data = {"score": score, "coins": coins}

        player.sprite.ai_handler(True, enemy_group)
        player.update(speed_multiplier, delta_time, enemy_group, events)
        player.draw(screen)

        enemy_group.draw(screen)
        enemy_group.update(speed_multiplier, delta_time)

        coin_group.draw(screen)
        coin_group.update(speed_multiplier, delta_time, player.sprite.rect)
        if "esc_key_down" in events:
            pygame.mixer.Sound.play(pause_sound)

            previous_game_state = game_state
            game_state = "pause_menu"
            esc_hit = True

        cursor_img_rect.center = pygame.mouse.get_pos()

        if cursor_state == 1:
            screen.blit(cursors[1], cursor_img_rect)
        elif cursor_state == 0:
            screen.blit(cursors[0], cursor_img_rect)

    if game_state == "pause_menu":
        screen.blit(sky, (sky_x, 0))

        if previous_game_state == "game":
            player.draw(screen)
            enemy_group.draw(screen)
            screen.blit(floor, (floor_x, 284))

            score_text, score_text_rect = uiHandler.get_text(font_big, '%05d' % (int('00000')+score))
            score_text_rect.midright = width-20, 30
            screen.blit(score_text, score_text_rect)

        screen.blit(coin, coin_rect)
        coin_text, coin_text_rect = uiHandler.get_text(font_big, '%05d' % (int('00000')+coins),
                                                         rgb=coin_text_color)
        coin_text_rect.midright = coin_text_pos
        screen.blit(coin_text, coin_text_rect)

        uiHandler.draw_text(screen, width/2, height/2-75, font_big, "Game Paused")

        if "down_key_down" in events:
            selected += 1
            if "enter_key_down" not in events:
                pygame.mixer.Sound.play(hover_sound)

        if "jump_key_down" in events:
            selected -= 1
            if "enter_key_down" not in events:
                pygame.mixer.Sound.play(hover_sound)

        if selected == 3:
            selected = 0
        if selected == -1:
            selected = 2

        resume_button.active = True
        restart_button.active = True
        quit_button.active = True

        resume_button.update(screen, cursor_img_rect, events)
        restart_button.update(screen, cursor_img_rect, events)
        quit_button.update(screen, cursor_img_rect, events)

        if resume_button.hover:
            selected = 0
        elif restart_button.hover:
            selected = 1
        elif quit_button.hover:
            selected = 2

        if selected == 0:
            resume_button.hover = True

            if "enter_key_down" in events or resume_button.clicked_up:
                pygame.mixer.Sound.play(click_sound)
                game_state = previous_game_state
        elif selected == 1:
            restart_button.hover = True

            if "enter_key_down" in events or restart_button.clicked_up:
                pygame.mixer.Sound.play(click_sound)
                score = 0
                speed_multiplier = speed_multiplier_default
                spawn_rate = spawn_rate_default
                sky = green_sky
                floor = grass_floor
                player.sprite.rect.y = 284
                enemy_group.empty()

                previous_game_state = game_state
                game_state = "game"
        elif selected == 2:
            quit_button.hover = True

            if "enter_key_down" in events or quit_button.clicked_up:
                pygame.mixer.Sound.play(click_sound)
                score = 0
                speed_multiplier = speed_multiplier_default
                spawn_rate = spawn_rate_default
                sky = green_sky
                floor = grass_floor
                player.sprite.rect.y = 284
                enemy_group.empty()

                previous_game_state = game_state
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

    if game_state == "game_over":
        if previous_save_data["score"] <= save_data["score"]:
            fileHandler.save_data(save_data)
            previous_save_data = save_data

        sky_x -= 112.2*speed_multiplier*delta_time
        if sky_x <= -700:
            sky_x = 0
        screen.blit(sky, (sky_x, 0))

        uiHandler.draw_text(screen, width/2, height/2, font_big, "Game Over")
        uiHandler.draw_text(screen, width/2, height/2+50, font_default,
                            'Score: '+'%05d' % (int('00000')+score))
        uiHandler.draw_text(screen, width/2, height/2+75, font_small,
                            'High score: '+'%05d' % (int('00000')+int(previous_save_data["score"])))

        uiHandler.draw_text(screen, width/2, height/2+125, font_default, "Press jump to restart")
        uiHandler.draw_text(screen, width/2, height/2+150, font_default, "Press escape to return to title")

        if "jump_key_down" in events or "left_mouse_button_down" in events or player.sprite.ai and \
                pygame.time.get_ticks()/1000-death_time >= 1:
            pygame.mixer.Sound.play(click_sound)
            score = 0
            speed_multiplier = speed_multiplier_default
            spawn_rate = spawn_rate_default
            sky = green_sky
            floor = grass_floor
            player.sprite.rect.y = 284
            timer_set = False
            enemy_group.empty()

            previous_game_state = game_state
            game_state = "game"

        if "esc_key_down" in events:
            pygame.mixer.Sound.play(click_sound)
            score = 0
            speed_multiplier = speed_multiplier_default
            spawn_rate = spawn_rate_default
            floor = grass_floor
            player.sprite.rect.y = 284
            enemy_group.empty()

            previous_game_state = game_state
            game_state = "title_screen"

        cursor_img_rect.center = pygame.mouse.get_pos()
        if cursor_state == 1:
            screen.blit(cursors[1], cursor_img_rect)
        elif cursor_state == 0:
            screen.blit(cursors[0], cursor_img_rect)

    if game_state == "settings":
        sky = mint_sky
        sky_x -= 112.2*speed_multiplier*delta_time
        if sky_x <= -700:
            sky_x = 0
        screen.blit(sky, (sky_x, 0))

        uiHandler.draw_text(screen, width/2, height/6, font_big, "Settings")

        if "down_key_down" in events:
            selected += 1
            if "enter_key_down" not in events:
                pygame.mixer.Sound.play(hover_sound)

        if "jump_key_down" in events:
            selected -= 1
            if "enter_key_down" not in events:
                pygame.mixer.Sound.play(hover_sound)

        if selected == 3:
            selected = 0
        if selected == -1:
            selected = 2

        credits_button.active = True
        reset_saves_button.active = True
        back_button.active = True

        credits_button.update(screen, cursor_img_rect, events)
        reset_saves_button.update(screen, cursor_img_rect, events)
        back_button.update(screen, cursor_img_rect, events)

        if credits_button.hover:
            selected = 0
        elif reset_saves_button.hover:
            selected = 1
        elif back_button.hover:
            selected = 2

        if selected == 0:
            credits_button.hover = True
            if "enter_key_down" in events or credits_button.clicked_up:
                pygame.mixer.Sound.play(click_sound)
                credits_button.active = False
                reset_saves_button.active = False
                back_button.active = False

                previous_game_state = game_state
                game_state = "credits"
        elif selected == 1:
            reset_saves_button.hover = True

            if "enter_key_down" in events or reset_saves_button.clicked_up:
                pygame.mixer.Sound.play(click_sound)
                fileHandler.save_data(save_data_layout)
        elif selected == 2:
            back_button.hover = True

            if "enter_key_down" in events or back_button.clicked_up:
                pygame.mixer.Sound.play(click_sound)
                credits_button.active = False
                reset_saves_button.active = False
                back_button.active = False

                previous_game_state = game_state
                game_state = "title_screen"
        if "esc_key_down" in events:
            pygame.mixer.Sound.play(click_sound)
            credits_button.active = False
            reset_saves_button.active = False
            back_button.active = False

            previous_game_state = game_state
            game_state = "title_screen"

        cursor_img_rect.center = pygame.mouse.get_pos()
        if cursor_state == 1:
            screen.blit(cursors[1], cursor_img_rect)
        elif cursor_state == 0:
            screen.blit(cursors[0], cursor_img_rect)

    if game_state == "credits":
        sky = mint_sky
        sky_x -= 112.2*speed_multiplier*delta_time
        if sky_x <= -700:
            sky_x = 0
        screen.blit(sky, (sky_x, 0))
        uiHandler.draw_text(screen, width/2, height/6, font_big, "Credits")
        uiHandler.draw_text(screen, width/2, height/4+125, font_default, "Author: Eshan Tahir")
        uiHandler.draw_text(screen, width/2, height/4+150, font_default, "Contributor: RJ Carter")
        uiHandler.draw_text(screen, width/2, height/3+150, font_default, "© 2022")
        uiHandler.draw_text(screen, width/2, height/2+150, font_default, "Press esc to exit")
        cursor_img_rect.center = pygame.mouse.get_pos()
        if cursor_state == 1:
            screen.blit(cursors[1], cursor_img_rect)
        elif cursor_state == 0:
            screen.blit(cursors[0], cursor_img_rect)

        if "esc_key_down" in events:
            pygame.mixer.Sound.play(click_sound)

            previous_game_state = game_state
            game_state = "settings"

    if game_state == "shop":
        sky = green_sky
        sky_x -= 112.2*speed_multiplier*delta_time
        if sky_x <= -700:
            sky_x = 0
        screen.blit(sky, (sky_x, 0))
        uiHandler.draw_text(screen, width/2, height/6, font_big, "Shop")

        skies_button.active = True
        skies_button.update(screen, cursor_img_rect, events)

        char_button.active = True
        char_button.update(screen, cursor_img_rect, events)

        return_button.active = True
        return_button.update(screen, cursor_img_rect, events)

        screen.blit(coin, coin_rect_2)
        coin_text, coin_text_rect = uiHandler.get_text(font_big, '%05d' % (int('00000')+coins),
                                                         rgb=coin_text_color)
        coin_text_rect.midright = coin_text_pos_2
        screen.blit(coin_text, coin_text_rect)

        cursor_img_rect.center = pygame.mouse.get_pos()
        if cursor_state == 1:
            screen.blit(cursors[1], cursor_img_rect)
        elif cursor_state == 0:
            screen.blit(cursors[0], cursor_img_rect)

        if skies_button.clicked_up:
            pygame.mixer.Sound.play(click_sound)
            settings_button.active = False
            events.clear()
            previous_game_state = game_state
            game_state = "sky_shop"

        if char_button.clicked_up:
            pygame.mixer.Sound.play(click_sound)
            settings_button.active = False
            events.clear()
            previous_game_state = game_state
            game_state = "char_shop"

        if return_button.clicked_up or "esc_key_down" in events:
            pygame.mixer.Sound.play(click_sound)
            settings_button.active = False
            events.clear()
            previous_game_state = game_state
            game_state = "title_screen"

    if game_state == "sky_shop":
        sky = green_sky
        sky_x -= 112.2*speed_multiplier*delta_time
        if sky_x <= -700:
            sky_x = 0
        screen.blit(sky, (sky_x, 0))

        screen.blit(coin, coin_rect_2)
        coin_text, coin_text_rect = uiHandler.get_text(font_big, '%05d' % (int('00000')+coins),
                                                         rgb=coin_text_color)
        coin_text_rect.midright = coin_text_pos_2
        screen.blit(coin_text, coin_text_rect)

        uiHandler.draw_text(screen, width/2, height/6, font_big, "The Sky Shop")

        back_shops.active = True
        back_shops.update(screen, cursor_img_rect, events)

        cursor_img_rect.center = pygame.mouse.get_pos()
        if cursor_state == 1:
            screen.blit(cursors[1], cursor_img_rect)
        elif cursor_state == 0:
            screen.blit(cursors[0], cursor_img_rect)

        if "esc_key_down" in events:
            pygame.mixer.Sound.play(click_sound)

        if back_shops.clicked_up or "esc_key_down" in events:
            pygame.mixer.Sound.play(click_sound)
            settings_button.active = False
            events.clear()
            previous_game_state = game_state
            game_state = "shop"

    if game_state == "char_shop":
        sky = green_sky
        sky_x -= 112.2*speed_multiplier*delta_time
        if sky_x <= -700:
            sky_x = 0
        screen.blit(sky, (sky_x, 0))

        screen.blit(coin, coin_rect_2)

        coin_text, coin_text_rect = uiHandler.get_text(font_big, '%05d' % (int('00000')+coins),
                                                         rgb=coin_text_color)
        coin_text_rect.midright = coin_text_pos_2
        screen.blit(coin_text, coin_text_rect)
        uiHandler.draw_text(screen, width/2, height/6, font_big, "The Character Shop")

        back_shops.active = True
        back_shops.update(screen, cursor_img_rect, events)

        cursor_img_rect.center = pygame.mouse.get_pos()
        if cursor_state == 1:
            screen.blit(cursors[1], cursor_img_rect)
        elif cursor_state == 0:
            screen.blit(cursors[0], cursor_img_rect)

        if back_shops.clicked_up or "esc_key_down" in events:
            pygame.mixer.Sound.play(click_sound)
            settings_button.active = False
            events.clear()
            previous_game_state = game_state
            game_state = "shop"

    pygame.display.flip()
    clock.tick(60)
