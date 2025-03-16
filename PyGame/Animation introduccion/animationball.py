#animacion de prueba - introduccion

import sys , pygame

pygame.init()

size = width , height = 320 , 240
speed = [2 , 2]
black = 0 , 0 , 0

window = pygame.display.set_mode(size)

pelota = pygame.image.load("F:\\Programacion\\Practicas\\PyGame\\assets\\intro_ball.gif")
pelotarect= pelota.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        
        pelotarect = pelotarect.move(speed)
        if pelotarect.left < 0 or pelotarect.right > width:
            speed[0] = -speed[0]
            
        if pelotarect.top < 0 or pelotarect.bottom > height:
            speed[1] = -speed[1]
            
        window.fill(black)
        window.blit(pelota, pelotarect)
        pygame.display.flip()