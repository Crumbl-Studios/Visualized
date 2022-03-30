import pygame  # To identify event types

# Custom event names
terminate = "terminate"

mouse_motion = "mouse_motion"

mouse_button_down = "mouse_button_down"
mouse_button_up = "mouse_button_up"

left_mouse_button_down = "left_mouse_button_down"
left_mouse_button_up = "left_mouse_button_up"

scroll_mouse_button_down = "scroll_mouse_button_down"
scroll_mouse_button_up = "scroll_mouse_button_up"

right_mouse_button_down = "right_mouse_button_down"
right_mouse_button_up = "right_mouse_button_up"

user_event_1 = "user_event_1"
user_event_2 = "user_event_2"

key_down = "key_down"
enter_key_down = "enter_key_down"
up_down = "jump_key_down"
right_down = "forward_key_down"
left_down = "backward_key_down"
down_down = "down_key_down"
esc_down = "esc_key_down"

key_up = "key_up"
enter_key_up = "enter_key_up"
up_up = "jump_key_up"
right_up = "forward_key_up"
left_up = "backward_key_up"
down_up = "up_key_up"
esc_up = "esc_key_up"


# Function to return a list of all events in a frame
# Loops through pygame events, appends them to a list if they are needed, returns list
def get_events():
    events = []
    pygame.event.pump()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            events.append(terminate)

        if event.type == pygame.MOUSEMOTION:
            events.append(mouse_motion)

        if event.type == pygame.MOUSEBUTTONDOWN:
            events.append(mouse_button_down)
        if event.type == pygame.MOUSEBUTTONUP:
            events.append(mouse_button_up)

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            events.append(left_mouse_button_down)
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            events.append(left_mouse_button_up)

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 2:
            events.append(scroll_mouse_button_down)
        if event.type == pygame.MOUSEBUTTONUP and event.button == 2:
            events.append(scroll_mouse_button_up)

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            events.append(right_mouse_button_down)
        if event.type == pygame.MOUSEBUTTONUP and event.button == 3:
            events.append(right_mouse_button_up)
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

            if event.key == pygame.K_ESCAPE:
                events.append(esc_down)
            if event.key == pygame.K_RETURN:
                events.append(enter_key_down)

        if event.type == pygame.KEYUP:
            events.append(key_up)
            if event.key == pygame.K_w or event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                events.append(up_up)
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                events.append(right_up)
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                events.append(left_up)
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                events.append(down_up)

            if event.key == pygame.K_ESCAPE:
                events.append(esc_up)
            if event.key == pygame.K_RETURN:
                events.append(enter_key_up)

        if event.type == pygame.USEREVENT + 1:
            events.append(user_event_1)

        if event.type == pygame.USEREVENT + 2:
            events.append(user_event_2)
    return events
