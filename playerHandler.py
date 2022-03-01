import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, run, fall, jump, jump_sound, ground_level):
        super().__init__()
        self.gravity = 0
        self.ground_level = ground_level
        self.jump_state = 0
        self.jump_sound = jump_sound

        self.run_animation = run
        self.fall = fall
        self.jump = jump
        self.index = 0
        self.image = self.run_animation[self.index]
        self.rect = self.image.get_rect(bottomleft=(10, ground_level))

    def player_input(self, events):
        events = events
        if "jump_key_down" in events:
            if self.jump_state == 0:
                self.jump_state = 1
                self.gravity = -23
                pygame.mixer.Sound.play(self.jump_sound)
        if "jump_key_up" in events and self.jump_state == 1:
            self.gravity += 10

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= self.ground_level:
            self.rect.bottom = self.ground_level
        if self.rect.bottom == self.ground_level:
            self.jump_state = 0
            self.gravity = 0

    def animation_state(self, speed_multiplier, delta_time):
        if self.gravity < 0:
            self.image = self.jump
        elif self.gravity > 0:
            self.image = self.fall
        elif self.gravity == 0:
            self.index += 15 * speed_multiplier * delta_time
            if self.index >= len(self.run_animation):
                self.index = 0
            self.image = self.run_animation[int(self.index)]

    def update(self, speed_multiplier, delta_time, events):
        self.player_input(events)
        self.apply_gravity()
        self.animation_state(speed_multiplier, delta_time)
