import pygame

pygame.init()
window = pygame.display.set_mode((700,500))
window.fill((237,152,183))

game = True
fps = pygame.time.Clock()

class GameObject():
    def __init__(self, img, x,y, width, height, speed):
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.hitbox = self.image.get_rect()
        self.hitbox.x = x 
        self.hitbox.y = y

    def show(self):
        window.blit(self.image,(self.hitbox))























while game:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            game = False
    pygame.display.update()
    fps.tick(70)