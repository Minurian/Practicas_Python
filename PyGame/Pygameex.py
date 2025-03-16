# Ejemplo para crear una pantalla en pygame

import pygame  # Importa la biblioteca pygame

pygame.init()  # Inicializa todos los módulos de pygame
window = pygame.display.set_mode((1280, 720))  # Crea una ventana con tamaño 1280x720
clock = pygame.time.Clock()  # Crea un objeto Clock para controlar el tiempo
running = True  # Variable para mantener el bucle principal en ejecución

while running: 
    # Bucle principal del juego que se ejecuta mientras 'running' sea True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # Cambia 'running' a False para salir del bucle y cerrar la ventana
window.fill("Purple")

pygame.display.flip()

clock.tick(60) # limita fps a 60 




