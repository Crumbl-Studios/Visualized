import pygame


def draw_box(screen, rx, ry, px, py, rgb=(255, 255, 255), transparent=False, alpha=100):
    box = pygame.Surface((rx, ry))
    if transparent:
        box.set_alpha(alpha)
    box.fill(rgb)
    screen.blit(box, (px, py))


def draw_text(screen, x, y, font, text, rgb=(0, 0, 0), aa=False):
    string = font.render(text, aa, rgb)   # Text to be drawn, and color.
    string_rect = string.get_rect()  # Grab the rectangle borders for the text.
    string_rect.center = (x, y)  # Coordinates for text to be drawn at.
    screen.blit(string, string_rect)  # Render 'string' to the screen at the position of 'string_rect'.


def draw_text_mid_right(screen, x, y, font, text, rgb=(0, 0, 0), aa=False):
    string = font.render(text, aa, rgb)   # Text to be drawn, and color.
    string_rect = string.get_rect()  # Grab the rectangle borders for the text.
    string_rect.midright = (x, y)  # Coordinates for text to be drawn at.
    screen.blit(string, string_rect)  # Render 'string' to the screen at the position of 'string_rect'.

def draw_text_mid_left(screen, x, y, font, text, rgb=(0, 0, 0), aa=False):
    string = font.render(text, aa, rgb)   # Text to be drawn, and color.
    string_rect = string.get_rect()  # Grab the rectangle borders for the text.
    string_rect.midleft = (x, y)  # Coordinates for text to be drawn at.
    screen.blit(string, string_rect)  # Render 'string' to the screen at the position of 'string_rect'.


def get_text_rect(x, y, font, text, rgb=(0, 0, 0), aa=False):
    string = font.render(text, aa, rgb)   # Text to be drawn, and color.
    string_rect = string.get_rect()  # Grab the rectangle borders for the text.
    string_rect.center = (x, y)  # Coordinates for text to be drawn at.
    return string_rect  # Return the rect for the string, so it can be used


class Button:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, screen):
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if self.clicked is False and pygame.mouse.get_pressed(3)[0] == 1:
                self.clicked = True
        if pygame.mouse.get_pressed(3)[0] == 0:
            self.clicked = False
        screen.blit(self.image, (self.rect.x, self.rect.y))
