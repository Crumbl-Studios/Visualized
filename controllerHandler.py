import pygame
import math

class controller():
    def __init__(self):
        pygame.joystick.init()
        joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
        print("Controller module active, scanning for controller")
        self.axis_data = []
        controller.controller_add(self)
    def controller_add(self):
        joystick_count = pygame.joystick.get_count()
        print("Joystick count: %d" %(joystick_count))
        try:
            self.joystick = pygame.joystick.Joystick(joystick_count-1) #Get controller data
            self.joy_name = self.joystick.get_name()
            self.joy_axes = self.joystick.get_numaxes()
            self.joy_hats = self.joystick.get_numhats()
            self.joy_buttons = self.joystick.get_numbuttons()
            self.battery = self.joystick.get_power_level()
            print("==========CONTROLLER INFO===========\njoystick: %d\nname: %s\naxes: %d\nhats: %d\nbuttons: %d\nbattery: %s\n===================================" %(joystick_count,self.joy_name,self.joy_axes,self.joy_hats,self.joy_buttons,self.battery))
            self.joystick.init() # "Log in" controllers (for Switch controllers)
            for i in range(self.joy_axes):
                self.axis_data.append(i)
            print("Controller joined")
        except pygame.error:
            print("No controller found")
    def get_button(number,self):
        return self.joystick.get_button(number)

    def get_axisVal(self):
        for i in range(self.joy_axes):
            self.axis_data[i] = math.floor(self.joystick.get_axis(i)*10)

    def rumbleFor(self,length = 0,startStrength = 0.0,endStrength = 1.0):
        try:
            rumble = self.joystick.rumble(startStrength,endStrength,length)
            if rumble == True:
                print("Rumble success")
            else:
                print("Error, or controller does not support haptics")
        except AttributeError:
            print("Haptic failed because no controller connected")