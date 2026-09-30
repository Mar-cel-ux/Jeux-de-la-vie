import pygame

pygame.init()

screen_size=(1960,420)
screen =pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()
BUTTON_COLOR = (70, 130, 180)
TEXT_COLOR = (255, 255, 255)
start_game = True
game_tittle = "JEU DE LA VIE"

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

button_start = Button(x=880, y=185, width=200, height=50, text="Commencer")
while start_game:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start_game = False
        if button_start.is_click(event):
            print("Bouton cliqué !")

            show_surface = True

            screen.fill((30, 30, 30))

            if show_surface:
                surface = pygame.Surface((400, 300))
                surface.fill((255, 0, 0))
                screen.blit(surface, (100, 100))
            else:
                button_start.draw(screen, BUTTON_COLOR)

    screen.fill((30, 30, 30))
    button_start.draw(screen,BUTTON_COLOR)
    pygame.display.flip()

pygame.quit()
