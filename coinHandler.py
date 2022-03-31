import pygame  # To use rect datatypes, masking, etc..
import random  # Randomize spawning


class Coin(pygame.sprite.Sprite):
    def __init__(self, coin_type, ground_level, flight_level,
                 screen_width, idle_animation, collected_animation, collect_sound, coin_id_number, coin_group=None,
                 spawn_animation=None):
        super().__init__()
        # Setup variables
        if spawn_animation is None:
            spawn_animation = []
        self.index = 0
        self.coin_type = coin_type
        self.coin_group = coin_group
        self.id = coin_id_number
        self.collect_sound = collect_sound
        self.collect_sound_played = False
        self.hit = False
        self.collected_animation = collected_animation
        self.spawning = True
        self.spawn_animation = spawn_animation
        self.animation = idle_animation
        self.ground_level = ground_level
        self.flight_level = flight_level
        self.screen_width = screen_width
        self.image = self.animation[self.index]

        if self.coin_type == "air":
            y_pos = self.flight_level
        elif self.coin_type == "land":
            y_pos = self.ground_level
        else:
            y_pos = self.ground_level

        self.rect = self.image.get_rect()
        self.rect = self.image.get_rect(bottomleft=(random.randint(self.screen_width+self.rect.width+10,
                                                                   self.screen_width+self.rect.width+300), y_pos))
        self.mask = pygame.mask.from_surface(self.image)

    # Function to handle animations
    def animation_state(self, delta_time):
        self.index += 15*delta_time
        if len(self.spawn_animation) != 0 and self.spawning:
            if self.index >= len(self.spawn_animation):
                self.spawning = False
            self.image = self.spawn_animation[int(self.index)]

        else:
            if self.index >= len(self.animation):
                self.index = 0
            self.image = self.animation[int(self.index)]
        self.mask = pygame.mask.from_surface(self.image)

    # Function to handle coin moving
    def move_coin(self, speed_multiplier, delta_time):
        self.rect.x -= 340 * speed_multiplier * delta_time
        if self.rect.collidepoint(self.screen_width, self.ground_level) or\
                self.rect.collidepoint(self.screen_width, self.flight_level):
            self.spawning = True

    def disappear(self, delta_time):
        if not self.collect_sound_played:
            pygame.mixer.Sound.play(self.collect_sound)
            self.collect_sound_played = True

        self.index += 15*delta_time
        if self.index >= len(self.collected_animation):
            self.image = pygame.Surface((1, 1), pygame.SRCALPHA)
            self.rect.bottomright = (0, 0)
        else:
            self.image = self.collected_animation[int(self.index)]

    # Function to null out enemies
    def destroy(self, coin_group):
        if self.rect.x <= 0-self.rect.width:  # If coin is off-screen:
            self.kill()  # Kill it
        for coin in coin_group:  # Loop through enemies
            # If a different coin is overlapping this one (Needs adjusting!)
            if coin.rect.x in range(self.rect.x-75, self.rect.x+self.rect.width+75) and coin.id != self.id:
                if self.rect.x < self.screen_width:  # Makes sure coin is to the right of the screen
                    self.kill()  # Kill it

    def update(self, speed_multiplier, delta_time, player_rect):
        self.destroy(self.coin_group)
        if self.hit:
            self.disappear(delta_time)
        else:
            self.animation_state(delta_time)
        self.move_coin(speed_multiplier, delta_time)
