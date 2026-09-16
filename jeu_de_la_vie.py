

import pygame

# init the game

pygame.init()
screen =pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
start_game = True
game_tittle = "JEU DE LA VIE"

#personnalize the game
game_font = pygame.font.SysFont("Arial", 36)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
text = game_font.render("COMMENCER LE JEU", True, BLACK)
button_rect = pygame.Rect(300, 250, 200, 50)
button_border = text.get_rect(center=button_rect.center)


#start the game

while start_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start_game = False

    screen.fill("gray")
    pygame.display.set_caption(game_tittle)
    screen.blit(text, button_border)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
