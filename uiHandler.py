import pygame

# Function to create rectangles
def get_rectangle(screen, rx, ry, rgb=(255, 255, 255), transparent=False, alpha=100):
    square = pygame.Surface((rx, ry))
    if transparent:
        square.set_alpha(alpha)
    square.fill(rgb)
    return square

# Function to create text
def get_text(screen, x, y, font, text, rgb=(0, 0, 0), aa=False):
    rendered_text = font.render(text, aa, rgb)   # Text to be drawn, and color.
    text_rect = text.get_rect()  # Grab the rectangle borders for the text.
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
