import pygame  # To use rect datatypes, masking, sound effects, etc..
import particleHandler  # To add particle effects

dust_particle = particleHandler.Particle()  # particle object


class Player(pygame.sprite.Sprite):
    def __init__(self, screen, run, fall, jump, jump_sound, ground_level):
        super().__init__()
        # Setup variables
        self.gravity = 0
        self.ground_level = ground_level
        self.jump_state = 0
        self.jump_sound = jump_sound
        self.time_jumping = 0

        self.run_animation = run
        self.fall = fall
        self.jump = jump
        self.index = 0

        self.screen = screen
        self.image = self.run_animation[self.index]
        self.rect = self.image.get_rect(bottomleft=(10, ground_level))
        self.mask = pygame.mask.from_surface(self.image)

    # Function to handle jumping
    def player_input(self, events):
        self.jump_ended = 0 #Define jump ended variable to make avoid crashes
        if "jump_key_down" in events or "mouse_button_down" in events:
            if self.jump_state == 0:  # If you're not already jumping:
                self.jump_state = 1  # Set jumping to be true
                self.index = 0  # To make sure  run animation resets once player is on floor
                self.time_jumping = pygame.time.get_ticks()  # To display particles for an amount of time after jump
                self.gravity = -890  # Sets gravity as negative so player goes upward
                pygame.mixer.Sound.play(self.jump_sound)  # Play jumping sound
        # If you let go of jump button, and you are jumping:
        if "jump_key_up" in events or "mouse_button_up" in events and self.jump_state == 1:
            self.gravity += 525  # Boost the player downwards
            self.jump_ended = pygame.time.get_ticks() #Record the time the jump ended

    # Function to handle gravity
    def apply_gravity(self, delta_time):
        self.gravity += 2000*delta_time  # Makes sure gravity is always going up at a linear rate
        self.rect.y += self.gravity*delta_time  # Adds gravity to the y position of player (goes down)
        if self.rect.bottom >= self.ground_level:  # If going through the floor
            self.rect.bottom = self.ground_level  # Set player to be on floor
        if self.rect.bottom == self.ground_level:  # If on the floor:
            self.jump_state = 0  # Set jumping to false
            self.gravity = 0  # Set gravity as 0 (so player does not go through floor)

    # Function to handle animations
    def animation_state(self, speed_multiplier, delta_time):
        if self.gravity < 0:  # If gravity is negative (jumping):
            self.image = self.jump  # Change player image to the jumping one
        elif self.gravity > 0:  # If gravity is positive (falling):
            self.image = self.fall  # Change player image to the falling one
        elif self.gravity == 0:  # If gravity is 0 (on floor)
            self.index += 15 * speed_multiplier * delta_time  # Used to index through the images of animation
            if self.index >= len(self.run_animation):  # If index is longer than animation length:
                self.index = 0  # Restart animation
            self.image = self.run_animation[int(self.index)]  # Changes player image to the index of the animation
            self.mask = pygame.mask.from_surface(self.image)  # Create a pixel perfect collision mask of image

    # Function to handle particles
    def particle_display(self, screen, delta_time):
        if pygame.time.get_ticks() - self.time_jumping <= 200:  # While player jumped within less than .2 seconds ago:
            dust_particle.add_particles(self.rect.midbottom[0], self.ground_level, 0, -10)  # Add more particles
            dust_particle.add_particles(self.rect.midbottom[0], self.ground_level, 0, -10)  # Add more particles
            dust_particle.add_particles(self.rect.midbottom[0], self.ground_level, 0, -10)  # Add more particles

            dust_particle.emit(screen, delta_time)  # Display said particles
        else:
            if pygame.time.get_ticks() - self.jump_ended >= 200: # Delay addded to give particles time to disperse, so particles dont get deleted when buttons get deleted
                dust_particle.delete_particles()  # Delete all particles after .2 sec of jump, or before jumping happened

    # Function to update player every frame
    def update(self, speed_multiplier, delta_time, events):
        self.player_input(events)
        self.apply_gravity(delta_time)
        self.animation_state(speed_multiplier, delta_time)
        self.particle_display(self.screen, delta_time)


