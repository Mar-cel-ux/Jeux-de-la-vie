import pygame
import time 

pygame.init()

screen_size=(840,420)
screen =pygame.display.set_mode(screen_size,pygame.RESIZABLE)
clock = pygame.time.Clock()
BUTTON_COLOR = (70, 130, 180)
RED_COLOR = (255, 0 , 0)
TEXT_COLOR = (255, 255, 255)
start_game = True
game_tittle = "JEU DE LA VIE"

def game_icon():
    icon_game = pygame.image.load("cheval.png")
    pygame.display.set_icon(icon_game)

class Button:
    def __init__(self,x=0, y=0, width=100, height=50, text=""):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = pygame.font.SysFont(None, 36)
        
    def is_click(self,event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
        return False
        
    	
    def draw(self,surface ,color):
        pygame.draw.rect(surface, color, self.rect)
        if self.text:
            text_surface = self.font.render(self.text, True, TEXT_COLOR)
            text_rect = text_surface.get_rect(center=self.rect.center)
            surface.blit(text_surface, text_rect)

button_start = Button(x=185, y=185, width=200, height=50, text="Commencer")
button_exit =  Button(x = 185, y = 300, width=200, height=50, text="Quitter" )
while start_game:

    for event in pygame.event.get():

        if button_start.is_click(event):
            print("cliquer")
            screen.fill(RED_COLOR)
            pygame.display.flip()
            time.sleep(5)
        if button_exit.is_click(event):
            start_game = False

    game_icon()
    screen.fill((30, 30, 30))
    button_start.draw(screen,BUTTON_COLOR)
    button_exit.draw(screen,BUTTON_COLOR)
    pygame.display.flip()

pygame.quit()

class Cellules :
    def __init__(self,etat,couleur)
        self.etat = etat
        self.couleur = couleur
