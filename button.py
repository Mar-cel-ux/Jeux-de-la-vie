import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))

bouton_rect = pygame.Rect(200, 150, 200, 60)
class Button :
    def __init__(self, nom, couleur):
        self.nom = nom
        self.couleur = couleur

    def action (self) :

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if bouton_rect.collidepoint(event.pos):
                        print("Bouton cliqué !")





