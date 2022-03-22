import pygame


# Function to draw rectangles
def draw_rectangle(screen, rx, ry, px, py, rgb=(255, 255, 255), transparent=False, alpha=100):
    rectangle = pygame.Surface((rx, ry))
    if transparent:
        rectangle.set_alpha(alpha)
    rectangle.fill(rgb)
    screen.blit(rectangle, (px, py))


# Function to create rectangles
def get_rectangle(rx, ry, rgb=(255, 255, 255), transparent=False, alpha=100):
    rectangle = pygame.Surface((rx, ry))
    if transparent:
        rectangle.set_alpha(alpha)
    rectangle.fill(rgb)
    return rectangle, rectangle.get_rect()


# Function to draw text
def draw_text(screen, x, y, font, text, rgb=(0, 0, 0), aa=False):
    string = font.render(text, aa, rgb)   # Text to be drawn, and color.
    string_rect = string.get_rect()  # Grab the rectangle borders for the text.
    string_rect.center = (x, y)  # Coordinates for text to be drawn at.
    screen.blit(string, string_rect)  # Render 'string' to the screen at the position of 'string_rect'.


# Function to create text
def get_text(font, text, rgb=(0, 0, 0), aa=False):
    rendered_text = font.render(text, aa, rgb)   # Text to be drawn, and color.
    text_rect = rendered_text.get_rect()  # Grab the rectangle borders for the text.
    return rendered_text, text_rect


# Skeleton of a function to create buttons
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
