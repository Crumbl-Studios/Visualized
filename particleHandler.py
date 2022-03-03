class Particle:
    def __init__(self):
        self.particles = []

    def emit(self, screen, particle_file):
        if self.particles:
            self.delete_particles()
            for particle in self.particles:
                particle[0][0] += particle[2][0]
                particle[0][1] += particle[2][1]
                particle[1] -= 0.5
                #particle_file.transform.scale *= 0.2
                screen.blit(particle_file, particle[0])
                #pygame.draw.circle(screen, pygame.Color('White'), particle[0], int(particle[1]))

    def add_particles(self, pos_x, pos_y, direction_x, direction_y):
        pos_x = pos_x
        pos_y = pos_y
        radius = 10
        particle_circle = [[pos_x, pos_y], radius, [direction_x, direction_y]]
        self.particles.append(particle_circle)

    def delete_particles(self):
        particle_copy = [particle for particle in self.particles if particle[1] > 0]
        self.particles = particle_copy

