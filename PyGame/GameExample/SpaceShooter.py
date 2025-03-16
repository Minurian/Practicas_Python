#Este juego tiene la finalidad de implementar y enseñar las bases de la libreria pygame

# 1. Importaremos las librerias
import pygame ,sys
from pygame.locals  import * # Llamamos a locals que es un componente fundamental que contiene constantes que nos ayudaran para el desarrollo de nuestra app 
import random

# 2. llamamos al motor de pygame este debe estar siempre y debe incluirse antes de comenzar a escribir cualquier codigo de pygame

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

# Predefined some colors    
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

screen_width = 400
screen_height = 600

screen = pygame.display.set_mode((screen_width,screen_height))
screen.fill(BLACK)
pygame.display.set_caption("Game") #Titulo

class Enemy1(pygame.sprite.Sprite):
    def __init__(self): #constructor de la clase
        super().__init__() # Llamado al constructor de la clase base
        self.image = pygame.image.load("F:\\Programacion\\Practicas\\PyGame\\GameExample\\Assets\\Images\\Enemy.png") # Carga la imagen del enemigo
        self.rect = self.image.get_rect() # Crea un rectangulo en la imagen que servira para limitar el espacion que abarca y poder crear colisiones
        self.rect.center = (random.randint(40, screen_width-40), 0) # Crea una funcion para que aparezcan los enemigos aleatoriamente 
        
    def move(self): # Define como se comportara el movimiento del enemigo
        self.rect.move_ip(0,2) # Define que el enemigo se movera 10 pixeles hacia abajo
        if(self.rect.bottom > 600): #Condicional que indica si el borde del enemigo pasa la coordenada 600 se volvera a reposicionar dicho enemigo
            self.rect.top = 0
            self.rect.center = (random.randint(30 , 370), 0) #Aca definira donde se ubicara nuevamente
    
    def draw (self, surface): # Dibuja al enemigo
        surface.blit(self.image, self.rect)
        
# class Enemy2(pygame.sprite.Sprite):
#     def __init__(self): #constructor de la clase
#         super().__init__() # Llamado al constructor de la clase base
#         self.image = pygame.image.load("F:\\Programacion\\Practicas\\PyGame\\GameExample\\Assets\\Images\\Enemy.png") # Carga la imagen del enemigo
#         self.rect = self.image.get_rect() # Crea un rectangulo en la imagen que servira para limitar el espacion que abarca y poder crear colisiones
#         self.rect.center = (random.randint(40, screen_width-40), 0) # Crea una funcion para que aparezcan los enemigos aleatoriamente 
        
#     def move(self): # Define como se comportara el movimiento del enemigo
#         self.rect.move_ip(0,5) # Define que el enemigo se movera 10 pixeles hacia abajo
#         if(self.rect.bottom > 600): #Condicional que indica si el borde del enemigo pasa la coordenada 600 se volvera a reposicionar dicho enemigo
#             self.rect.top = 0
#             self.rect.center = (random.randint(30 , 370), 0) #Aca definira donde se ubicara nuevamente
    
    def draw (self, surface): # Dibuja al enemigo
        surface.blit(self.image, self.rect)

class Player (pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load("F:\\Programacion\\Practicas\\PyGame\\GameExample\\Assets\\Images\\nave.png")
        self.rect = self.image.get_rect() # Crea un rectangulo en la imagen que servira para limitar el espacion que abarca y poder crear colisiones
                # obtener ancho y alto de pantalla
        screen_width = pygame.display.get_surface().get_size()[0]
        screen_height = pygame.display.get_surface().get_size()[1]
        self.player_group = pygame.sprite.Group()  # Crea un grupo solo para el jugador
        
        self.rect.center = (screen_width // 2 , screen_height // 2) # ubicacion del sprite. En este caso se hizo un calculo para que se posicionara al centro
        self.bullets = pygame.sprite.Group() # Grupo para las balas
        

    def update(self):
        pressed_keys = pygame.key.get_pressed()  # Define cuando se pulsa una tecla que hara en este caso trabajamos con las flechas del teclado
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)

        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < screen_width:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

    def disparar(self):
        bala = Bullet(self.rect.centerx, self.rect.top)
        self.bullets.add(bala)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        self.bullets.draw(surface) 
        

class Bullet (pygame.sprite.Sprite): #Creamos una clase para el disparo (bala)
    def __init__(self, x , y):
        super().__init__()
        self.image = pygame.image.load("F:\\Programacion\\Practicas\\PyGame\GameExample\\Assets\\Images\\bullett.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed_y = -10
    
    def update(self):
        self.rect.y += self.speed_y
        #Eliminamos la bala si sale de la pantalla
        if self.rect.bottom < 0:
            self.kill()
        

P1 = Player()
enemies = pygame.sprite.Group()
E1 = Enemy1()
enemies.add(E1)

def create_enemy():
    enemy = Enemy1()
    enemies.add(enemy)

create_enemy()

#Bucle principal

while True: 
    for event in pygame.event.get ():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                P1.disparar()
                print("Shoot!", P1.disparar())
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    P1.update()
    for enemy in enemies:
        enemy.move()
    P1.bullets.update()
    
    for bullet in P1.bullets:
        collided_enemies = pygame.sprite.spritecollide(bullet, enemies, True)
        if collided_enemies:
            bullet.kill()
            
    if random.randint(1, 10) == 1:
        create_enemy()
    
    screen.fill(BLACK)
    P1.draw(screen)
    enemies.draw(screen)
    
    pygame.display.update()
    FramePerSec.tick(FPS)