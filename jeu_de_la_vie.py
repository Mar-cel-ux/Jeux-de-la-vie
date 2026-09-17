

import pygame

# init the game

pygame.init()
screen_size=(1280,720)
screen =pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()
start_game = True
game_tittle = "JEU DE LA VIE"

#personnalize the game
game_font = pygame.font.SysFont("Arial", 36)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
text = game_font.render("COMMENCER LE JEU", True, BLACK)
class Button:

    def __init__(self, x, y, width, height, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = game_font
        self.is_hovered = False

    def draw(self, surface):
        # Couleur : Vert clair si survolé, Vert foncé sinon
        color = (46, 204, 113) if self.is_hovered else (39, 174, 96)

        # Dessin du rectangle avec bords arrondis
        pygame.draw.rect(surface, color, self.rect, border_radius=8)

        # Dessin du texte centré
        text_surf = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

    def update(self, mouse_pos):
        self.is_hovered = self.rect.collidepoint(mouse_pos)

    def is_clicked(self, event):
        return (
            event.type == pygame.MOUSEBUTTONDOWN
            and event.button == 1
            and self.is_hovered
        )


#start the game

while start_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start_game = False

    screen.fill("red")
    pygame.display.set_caption(game_tittle)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
