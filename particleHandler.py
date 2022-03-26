import pygame  # To transform image
import random  # To randomize particle effects


class Particle:
    def __init__(self):
        self.particles = []  # List to hold each particle

    # Function to display and move particles
    def emit(self, screen, delta_time):
        if self.particles:  # If there is anything in the particles list:
            self.null_particles()  # Delete all faded particles from list
            for particle in self.particles:  # Loop through all particles in list
                # Shift particle spawn location
                particle[0][0] += random.randint(-20, 20)
                particle[0][1] += random.randint(-10, 10)

                # If the direction isn't set, make it random
                if particle[2] == [0, 0]:
                    particle[2] = [random.randint(-3, 3), random.randint(-3, 3)]
                elif particle[2][0] == 0:
                    particle[2][0] = random.randint(-3, 3)
                elif particle[2][1] == 0:
                    particle[2][1] = random.randint(-3, 3)

                # Move particle based off of direction parameters
                particle[0][0] += particle[2][0]
                particle[0][1] += particle[2][1]

                # Make particle smaller (fade out effect)
                particle[1] -= 50*delta_time

                # Make color gradually get darker
                proxy_color = (particle[3][0]-2500*delta_time, particle[3][1]-2500*delta_time,
                               particle[3][2]-2500*delta_time)
                if proxy_color[0] < 0 or proxy_color[1] < 0 or proxy_color[2] < 0:
                    pass
                else:
                    particle[3] = proxy_color
                # Display particle
                pygame.draw.circle(screen, particle[3], particle[0], int(particle[1]))

    # Function to create particles
    def add_particles(self, pos_x, pos_y, direction_x=0, direction_y=0, color=(255, 255, 255)):
        pos_x = pos_x
        pos_y = pos_y
        radius = 7
        particle_circle = [[pos_x, pos_y], radius, [direction_x, direction_y], color]
        self.particles.append(particle_circle)

    # Function to automatically remove particles
    def null_particles(self):
        particle_copy = [particle for particle in self.particles if particle[1] > 0]
        self.particles = particle_copy

    def delete_particles(self):
        self.particles = []
