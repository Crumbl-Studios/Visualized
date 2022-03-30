import pygame  # To use rect datatypes, masking, sound effects, etc..
import particleHandler  # To add particle effects

dust_particle = particleHandler.Particle()  # particle object


class Player(pygame.sprite.Sprite):
    def __init__(self, screen, characters_animations, jump_sound, ground_level):
        super().__init__()
        # Setup variables
        self.gravity = 0
        self.ground_level = ground_level
        self.jumping = False
        self.jump_sound = jump_sound
        self.time_jumping = 0
        self.jump_ended = 0  # Define jump ended variable to make avoid crashes
        self.hit_floor = False
        self.hit_floor_time = 0

        self.ai = False  # Controls whether AI is on or off, accessible by: player.sprite.ai
        self.jump_down = False
        self.jump_up = False

        self.character = 1
        self.characters_animations = characters_animations
        self.appear = characters_animations[0]
        self.disappear = characters_animations[1]

        self.character_1 = characters_animations[2]
        self.character_2 = characters_animations[3]
        self.character_3 = characters_animations[4]
        self.character_4 = characters_animations[5]

        self.character_1_run = self.character_1[0]
        self.character_1_jump = self.character_1[1]
        self.character_1_fall = self.character_1[2]

        self.character_2_run = self.character_2[0]
        self.character_2_jump = self.character_2[1]
        self.character_2_fall = self.character_2[2]

        self.character_3_run = self.character_3[0]
        self.character_3_jump = self.character_3[1]
        self.character_3_fall = self.character_3[2]

        self.character_4_run = self.character_4[0]
        self.character_4_jump = self.character_4[1]
        self.character_4_fall = self.character_4[2]

        self.index = 0

        self.screen = screen
        self.image = self.character_1_run[self.index]
        self.rect = self.image.get_rect(bottomleft=(10, ground_level))
        self.mask = pygame.mask.from_surface(self.image)

    def ai_handler(self, state, enemy_group=None):
        self.ai = state
        if state and enemy_group is not None:
            for enemy in enemy_group:
                if enemy.rect.bottomleft[0]-self.rect.bottomright[0] > 0:
                    if enemy.rect.bottomleft[0] in range(self.rect.bottomright[0], self.rect.bottomright[0]+50):
                        if enemy.enemy_type == "land":
                            if not self.jump_down:
                                self.jump_down = True
                                self.jump_up = False
                        elif enemy.enemy_type == "air":
                            if not self.jump_up:
                                self.jump_up = True
                                self.jump_down = False
                    elif enemy.rect.bottomleft[0] in range(self.rect.bottomright[0], self.rect.bottomright[0]+51):
                        self.jump_up = True
                        self.jump_down = False
                elif enemy.rect.bottomright[0]-self.rect.bottomleft[0] < 0:
                    if not self.jump_up:
                        self.jump_up = True
                        self.jump_down = False

    def input(self, events):
        if "jump_key_down" in events or "left_mouse_button_down" in events:
            self.jump_down = True
            self.jump_up = False

        elif "jump_key_up" in events or "left_mouse_button_up" in events:
            self.jump_up = True
            self.jump_down = False

    # Function to handle jumping
    def player_movement(self):
        if self.jump_down:
            if not self.jumping:  # If you're not already jumping:
                self.jumping = True  # Set jumping to be true
                self.index = 0  # To make sure  run animation resets once player is on floor
                self.time_jumping = pygame.time.get_ticks()  # To display particles for an amount of time after jump
                self.gravity = -890  # Sets gravity as negative so player goes upward
                pygame.mixer.Sound.play(self.jump_sound)  # Play jumping sound
                self.jump_down = False
        # If you let go of jump button, and you are jumping:
        if self.jump_up and self.jumping:
            self.gravity += 525  # Boost the player downwards
            self.jump_ended = pygame.time.get_ticks()  # Record the time the jump ended
            self.jump_up = False

    # Function to handle gravity
    def apply_gravity(self, delta_time):
        self.gravity += 2000*delta_time  # Makes sure gravity is always going up at a linear rate
        self.rect.y += self.gravity*delta_time  # Adds gravity to the y position of player (goes down)
        if self.rect.bottom >= self.ground_level:  # If going through the floor
            self.rect.bottom = self.ground_level  # Set player to be on floor
        if self.rect.bottom == self.ground_level:  # If on the floor:
            self.jumping = False  # Set jumping to false
            self.gravity = 0  # Set gravity as 0 (so player does not go through floor)

    # Function to handle animations
    def animation_state(self, speed_multiplier, delta_time):
        if self.character == 1:
            if self.gravity < 0:  # If gravity is negative (jumping):
                self.image = self.character_1_jump  # Change player image to the jumping one
                self.hit_floor = False
            elif self.gravity > 0:  # If gravity is positive (falling):
                self.image = self.character_1_fall  # Change player image to the falling one
                self.hit_floor = False
            elif self.gravity == 0:  # If gravity is 0 (on floor)
                if not self.hit_floor:
                    self.hit_floor_time = pygame.time.get_ticks()
                    self.hit_floor = True
                self.index += 15 * speed_multiplier * delta_time  # Used to index through the images of animation
                if self.index >= len(self.character_1_run):  # If index is longer than animation length:
                    self.index = 0  # Restart animation
                self.image = self.character_1_run[int(self.index)]  # Changes player image to the index of the animation
                self.mask = pygame.mask.from_surface(self.image)  # Create a pixel perfect collision mask of image
        elif self.character == 2:
            if self.gravity < 0:  # If gravity is negative (jumping):
                self.image = self.character_2_jump  # Change player image to the jumping one
                self.hit_floor = False
            elif self.gravity > 0:  # If gravity is positive (falling):
                self.image = self.character_2_fall  # Change player image to the falling one
                self.hit_floor = False
            elif self.gravity == 0:  # If gravity is 0 (on floor)
                if not self.hit_floor:
                    self.hit_floor_time = pygame.time.get_ticks()
                    self.hit_floor = True
                self.index += 15 * speed_multiplier * delta_time  # Used to index through the images of animation
                if self.index >= len(self.character_2_run):  # If index is longer than animation length:
                    self.index = 0  # Restart animation
                self.image = self.character_2_run[int(self.index)]  # Changes player image to the index of the animation
                self.mask = pygame.mask.from_surface(self.image)  # Create a pixel perfect collision mask of image
        elif self.character == 3:
            if self.gravity < 0:  # If gravity is negative (jumping):
                self.image = self.character_3_jump  # Change player image to the jumping one
                self.hit_floor = False
            elif self.gravity > 0:  # If gravity is positive (falling):
                self.image = self.character_3_fall  # Change player image to the falling one
                self.hit_floor = False
            elif self.gravity == 0:  # If gravity is 0 (on floor)
                if not self.hit_floor:
                    self.hit_floor_time = pygame.time.get_ticks()
                    self.hit_floor = True
                self.index += 15 * speed_multiplier * delta_time  # Used to index through the images of animation
                if self.index >= len(self.character_3_run):  # If index is longer than animation length:
                    self.index = 0  # Restart animation
                self.image = self.character_3_run[int(self.index)]  # Changes player image to the index of the animation
                self.mask = pygame.mask.from_surface(self.image)  # Create a pixel perfect collision mask of image
        elif self.character == 4:
            if self.gravity < 0:  # If gravity is negative (jumping):
                self.image = self.character_4_jump  # Change player image to the jumping one
                self.hit_floor = False
            elif self.gravity > 0:  # If gravity is positive (falling):
                self.image = self.character_4_fall  # Change player image to the falling one
                self.hit_floor = False
            elif self.gravity == 0:  # If gravity is 0 (on floor)
                if not self.hit_floor:
                    self.hit_floor_time = pygame.time.get_ticks()
                    self.hit_floor = True
                self.index += 15 * speed_multiplier * delta_time  # Used to index through the images of animation
                if self.index >= len(self.character_4_run):  # If index is longer than animation length:
                    self.index = 0  # Restart animation
                self.image = self.character_4_run[int(self.index)]  # Changes player image to the index of the animation
                self.mask = pygame.mask.from_surface(self.image)  # Create a pixel perfect collision mask of image

    def appear(self, speed_multiplier, delta_time):
        return None

    def disappear(self, speed_multiplier, delta_time):
        return None

    # Function to handle particles
    def particle_display(self, screen, delta_time, speed_multiplier):
        # While player jumped within less than .2 seconds ago:
        if pygame.time.get_ticks() - self.time_jumping <= 200 or pygame.time.get_ticks() - self.hit_floor_time <= 200:
            dust_particle.add_particles(self.rect.midbottom[0], self.ground_level, 0, -10)  # Add more particles
            dust_particle.add_particles(self.rect.midbottom[0], self.ground_level, 0, -10)  # Add more particles
            dust_particle.add_particles(self.rect.midbottom[0], self.ground_level, 0, -10)  # Add more particles

            dust_particle.emit(screen, delta_time, speed_multiplier)  # Display said particles
        else:
            # Delay added to give particles time to disperse, so particles dont get deleted when buttons get deleted
            if pygame.time.get_ticks() - self.jump_ended >= 200 or pygame.time.get_ticks() - self.hit_floor_time >= 200:
                # Delete all particles after .2 sec of jump, or before jumping happened
                dust_particle.delete_particles()

    # Function to update player every frame
    def update(self, speed_multiplier, delta_time, enemy_group, events):
        print(self.hit_floor, self.hit_floor_time)
        self.ai_handler(self.ai, enemy_group)
        self.input(events)
        self.player_movement()
        self.apply_gravity(delta_time)
        self.animation_state(speed_multiplier, delta_time)
        self.particle_display(self.screen, delta_time, speed_multiplier)


