import pygame
pygame.init()
WHITE = (255,255,255)
BLACK = (0,0,0)

class Survivor(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([40,60])
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.color_key = WHITE
        self.color = BLACK
        
        pygame.draw.rect(self.image, self.color_key, [0,0,10,10])

        def draw(self, screen):
            screen.blit(self.image, self.rect)

class Companion(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([60,40])
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.color_key = WHITE
        self.color = BLACK
        
        pygame.draw.rect(self.image, self.color_key, [0,0,10,10])

        def draw(self, screen):
            screen.blit(self.image, self.rect)

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([40,40])
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.color_key = WHITE
        self.color = BLACK
        

        
        pygame.draw.rect(self.image, self.color_key, [0,0,10,10])

        def draw(self, screen):
            screen.blit(self.image, self.rect)

class Mouse_hit_box(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10,10])
        self.rect = self.image.get_rect()
        self.rect.center = (pygame.mouse.get_pos())
        self.color_key = WHITE
        self.color = BLACK
        
        

        def draw(self, screen):
            screen.blit(self.image, self.rect)