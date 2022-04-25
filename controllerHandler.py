import pygame

class controller():
    def __init__(self):
        pygame.joystick.init()
        joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
        print("Controller module active")
    def controller_add(self):
        joystick_count = pygame.joystick.get_count()
        print("Joystick count: %d" %(joystick_count))
        try:
            self.joystick = pygame.joystick.Joystick(joystick_count-1) #Get controller data
            self.joy_name = self.joystick.get_name()
            self.joy_axes = self.joystick.get_numaxes()
            self.joy_hats = self.joystick.get_numhats()
            self.joy_buttons = self.joystick.get_numbuttons()
            print("==========CONTROLLER INFO===========\njoystick: %d\nname: %s\naxes: %d\nhats: %d\nbuttons: %d\n===================================" %(joystick_count,self.joy_name,self.joy_axes,self.joy_hats,self.joy_buttons))
            self.joystick.init() # "Log in" controllers (for Switch controllers)
            print("Controller joined")
        except pygame.error:
            print("No controller found")
    def get_button(number,controller):
        return joystick.get_button(number)