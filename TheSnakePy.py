import pygame
import random
from tkinter import *
from tkinter import messagebox
from pygame.locals import *

PIXEL_SIZE = 10
WINDOW_SIZE = (200, 200)
cntLEMON = int()


def collision(pos1, pos2):
    return pos1 == pos2


def off_limits(pos):
    if 0 <= pos[0] < WINDOW_SIZE[0] and 0 <= pos[1] < WINDOW_SIZE[1]:
        return False
    else:
        return True


def random_on_grid():
    x = random.randint(0, WINDOW_SIZE[0])
    y = random.randint(0, WINDOW_SIZE[1])
    return x // PIXEL_SIZE * PIXEL_SIZE, y // PIXEL_SIZE * PIXEL_SIZE


pygame.init()
screen = pygame.display.set_mode((WINDOW_SIZE))
pygame.display.set_caption('TheSnakePy')

snake_pos = [(150, 50), (160, 50), (170, 50)]
snake_surface = pygame.Surface((PIXEL_SIZE, PIXEL_SIZE))
snake_surface.fill((255, 255, 255))
snake_direction = K_LEFT

banana_surface = pygame.Surface((PIXEL_SIZE, PIXEL_SIZE))
banana_surface.fill((255, 255, 0))
banana_pos = random_on_grid()

apple_surface = pygame.Surface((PIXEL_SIZE, PIXEL_SIZE))
apple_surface.fill((255, 0, 0))
apple_pos = random_on_grid()

grape_surface = pygame.Surface((PIXEL_SIZE, PIXEL_SIZE))
grape_surface.fill((138, 43, 226))
grape_pos = random_on_grid()

lemon_surface = pygame.Surface((PIXEL_SIZE, PIXEL_SIZE))
lemon_surface.fill((0, 255, 0))
lemon_pos = random_on_grid()


def restart_game():
    global snake_pos
    global apple_pos
    global banana_pos
    global snake_direction
    snake_pos = [(150, 50), (160, 50), (170, 50)]
    snake_direction = K_LEFT
    apple_pos = random_on_grid()


while True:
    pygame.time.Clock().tick(15)
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()
        elif event.type == KEYDOWN:
            if event.key in [K_UP, K_DOWN, K_LEFT, K_RIGHT]:
                snake_direction = event.key

    screen.blit(banana_surface, banana_pos)
    screen.blit(grape_surface, grape_pos)
    screen.blit(apple_surface, apple_pos)

    if collision(apple_pos, snake_pos[0]):
        snake_pos.append((-10, -10))
        apple_pos = random_on_grid()
        cntLEMON += 1

    if collision(banana_pos, snake_pos[0]):
        snake_pos.append((-10, -10))
        banana_pos = random_on_grid()
        cntLEMON += 1

    if collision(grape_pos, snake_pos[0]):
        snake_pos.append((-10, -10))
        grape_pos = random_on_grid()
        cntLEMON += 1

    for pos in snake_pos:
        screen.blit(snake_surface, pos)

    if (cntLEMON % 5 == 0) or (cntLEMON % 3 == 0):
        screen.blit(lemon_surface, lemon_pos)

        if collision(lemon_pos, snake_pos[0]):
            Tk().wm_withdraw() #esse comando esconde a caixa do tkinter
            messagebox.showinfo('OPS! UM LIMÃO!', 'Você comeu um limão... Limões são azedos. FIM DE JOGO!')
            restart_game()

    # Aqui vamos checar se a cabeça da cobra esta em contato com alguma parte do corpo dela
    for i in range(len(snake_pos) - 1, 0, -1):
        if collision(snake_pos[0], snake_pos[i]):
            restart_game()
        snake_pos[i] = snake_pos[i - 1]

    # snake_pos[0] indica a posicção da cabeça da cobra
    if off_limits(snake_pos[0]):
        restart_game()

    if snake_direction == K_UP:
        snake_pos[0] = (snake_pos[0][0], snake_pos[0][1] - PIXEL_SIZE)
    elif snake_direction == K_DOWN:
        snake_pos[0] = (snake_pos[0][0], snake_pos[0][1] + PIXEL_SIZE)
    elif snake_direction == K_LEFT:
        snake_pos[0] = (snake_pos[0][0] - PIXEL_SIZE, snake_pos[0][1])
    elif snake_direction == K_RIGHT:
        snake_pos[0] = (snake_pos[0][0] + PIXEL_SIZE, snake_pos[0][1])

    pygame.display.update()
