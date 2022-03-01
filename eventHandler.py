import pygame

terminate = "terminate"

mouse_button_down = "mouse_button_down"
mouse_button_up = "mouse_button_up"

key_down = "key_down"
up_down = "jump_key_down"
right_down = "forward_key_down"
left_down = "backward_key_down"
down_down = "down_key_down"

key_up = "key_up"
up_up = "jump_key_up"
right_up = "forward_key_up"
left_up = "backward_key_up"
down_up = "up_key_up"
pygame.init()


def get_events():
    events = []
    pygame.event.pump()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            events.append(terminate)

        if event.type == pygame.MOUSEBUTTONDOWN:
            events.append(mouse_button_down)
        if event.type == pygame.MOUSEBUTTONUP:
            events.append(mouse_button_up)

        if event.type == pygame.KEYDOWN:
            events.append(key_down)
            if event.key == pygame.K_w or event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                events.append(up_down)
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                events.append(right_down)
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                events.append(left_down)
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                events.append(down_down)

        if event.type == pygame.KEYUP:
            events.append(key_up)
            if event.key == pygame.K_w or event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                events.append(up_up)
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                events.append(right_up)
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                events.append(left_up)
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                events.append(up_up)

    return events
