import pygame
pygame.init()

#Fenêtre du jeu
fenetre = pygame.display.set_mode((800,600))
pygame.display.set_caption("Street fighter")

# Couleurs
blanc = (255, 255, 255)
noir = (0, 0, 0)

# Police et texte
police = pygame.font.Font(pygame.font.match_font('algerian'), 50)  # None utilise la police par défaut, 50 est la taille
texte = "Let's talk and come to fight"  # Phrase à afficher
surface_texte = police.render(texte, True, noir)  # True pour activer l'anti-aliasing

# Position du texte
position_texte = surface_texte.get_rect(center=(800 // 2, 600 // 2))

#Boucle du jeu
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Remplir l'écran avec une couleur de fond
    fenetre.fill(blanc)

    # Afficher le texte
    fenetre.blit(surface_texte, position_texte)

    # Mettre à jour l'affichage
    pygame.display.flip()

pygame.quit()
