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

# Button system (unfortunately i couldnt get command buttons to work properly, so a "gamemode" changing variant had to be placed in main) 
class button:
    def draw_command_button(screen,x, y, image,command,parameter = ""): 
        self = pygame.draw.rect(screen,(255,255,255),[x-50,y,100,50])
        # self.rect = self.image.get_rect()
        clicked = False
        pos = pygame.mouse.get_pos()
        if self.collidepoint(pos):
            if clicked is False and pygame.mouse.get_pressed(3)[0] == 1:
                clicked = True
                lambda command,parameter : command(parameter)
            if pygame.mouse.get_pressed(3)[0] == 0:
                clicked = False
        screen.blit(image, (x-50,y))

