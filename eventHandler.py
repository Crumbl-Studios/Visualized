import pygame  # To identify event types
import controllerHandler #To apply haptics, and join controllers

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

lb_down = "lb_down"
rb_down = "rb_down"

# Controller setup
control = controllerHandler.controller()
start_pos = []

# Function to return a list of all events in a frame
# Loops through pygame events, appends them to a list if they are needed, returns list
def get_events():
    global control
    events = []
    axis_data = []
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

        if event.type == pygame.JOYDEVICEADDED:
            print("Controller connected")
            controllerHandler.controller.controller_add(control)
        if event.type == pygame.JOYDEVICEREMOVED:
            print("Controller disconnected")
            controllerHandler.contollerPlugged = False
        
        if event.type == pygame.JOYBUTTONDOWN:
            controllerHandler.controller.rumbleFor(control,50,0.25,0.25)
            if controllerHandler.controller.get_button(1,control) or controllerHandler.controller.get_button(7,control):
                events.append(left_mouse_button_down)
            if controllerHandler.controller.get_button(0,control) or controllerHandler.controller.get_button(9,control):
                events.append(esc_down)
            if controllerHandler.controller.get_button(4,control):
                events.append(lb_down)
            if controllerHandler.controller.get_button(5,control):
                events.append(rb_down)
        
        if event.type == pygame.JOYBUTTONUP:
            events.append(left_mouse_button_up)
            events.append(esc_up)

    # Controller mouse controls (continuous)
    try:   
        controllerHandler.controller.get_axisVal(control)
        start_pos = pygame.mouse.get_pos()
        pygame.mouse.set_pos([start_pos[0]+control.axis_data[0]*10,start_pos[1]+control.axis_data[1]*10])
    except AttributeError:
        pass

    return events
