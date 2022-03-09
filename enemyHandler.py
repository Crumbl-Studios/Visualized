import pygame
import random


class Enemy(pygame.sprite.Sprite):
    def __init__(self, enemy_type, ground_level, flight_level,
                 screen_width, idle_animation, enemy_id_number, enemy_group=None, spawn_animation=None):
        super().__init__()

        if spawn_animation is None:
            spawn_animation = []
        self.index = 0
        self.enemy_type = enemy_type
        self.enemy_group = enemy_group
        self.id = enemy_id_number
        self.spawning = True
        self.spawn_animation = spawn_animation
        self.animation = idle_animation
        self.ground_level = ground_level
        self.flight_level = flight_level
        self.screen_width = screen_width
        self.image = self.animation[self.index]

        if self.enemy_type == "air":
            y_pos = self.flight_level
        elif self.enemy_type == "land":
            y_pos = self.ground_level
        else:
            y_pos = self.ground_level

        self.rect = self.image.get_rect()
        self.rect = self.image.get_rect(bottomleft=(random.randint(self.screen_width+self.rect.width+10,
                                                                   self.screen_width+self.rect.width+300), y_pos))
        self.mask = pygame.mask.from_surface(self.image)

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

    def move_enemy(self, speed_multiplier, delta_time):
        self.rect.x -= 340 * speed_multiplier * delta_time
        if self.rect.x == self.screen_width:
            self.spawning = True

    def destroy(self, enemy_group):
        if self.rect.x <= 0-self.rect.width:
            self.kill()
        for enemy in enemy_group:
            if enemy.rect.x in range(self.rect.x-75, self.rect.x+self.rect.width+75) and enemy.id != self.id:
                if self.rect.x < self.screen_width:
                    self.kill()

    def update(self, speed_multiplier, delta_time):
        self.destroy(self.enemy_group)
        self.animation_state(delta_time)
        self.move_enemy(speed_multiplier, delta_time)
