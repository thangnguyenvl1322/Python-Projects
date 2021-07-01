# -*- coding: utf-8 -*-
import pygame
import sys
import random

pygame.init()
clock = pygame.time.Clock()
#game_font = pygame.font.Font('04B_19.ttf',40)



#Settings
resolution_x = 288
resolution_y = 512
framerate = 60
screen = pygame.display.set_mode((resolution_x,resolution_y))

#Games Variables:
gravity = 0.25
bird_movement = 0
game_active = True

score = 0
high_score = 0


#Assigning images to variables

bg_surface = pygame.image.load('C:/Users/thang/Desktop/flappy_bird/flappy-bird-assets-master/sprites/background-day.png').convert()
floor = pygame.image.load('C:/Users/thang/Desktop/flappy_bird/flappy-bird-assets-master/sprites/base.png').convert()

bird_surface = pygame.image.load('C:/Users/thang/Desktop/flappy_bird/flappy-bird-assets-master/sprites/yellowbird-midflap.png').convert_alpha()
bird_surface_before = pygame.image.load('C:/Users/thang/Desktop/flappy_bird/flappy-bird-assets-master/sprites/yellowbird-downflap.png').convert_alpha()
bird_surface_after = pygame.image.load('C:/Users/thang/Desktop/flappy_bird/flappy-bird-assets-master/sprites/yellowbird-upflap.png').convert_alpha()

bird_frame = [bird_surface_before, bird_surface, bird_surface_after]
bird_index = 0
bird_surface = bird_frame[bird_index]

bird_rect = bird_surface.get_rect(center = (100, 256))

BIRDFLAP = pygame.USEREVENT + 1
pygame.time.set_timer(BIRDFLAP, 200)


pipe_surface = pygame.image.load('C:/Users/thang/Desktop/flappy_bird/flappy-bird-assets-master/sprites/pipe-green.png')
pipe_list =[]

SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)



floor_x_position = 0

def create_pipe():
    random_height = random.randint(180, 350)
    bottom_pipe = pipe_surface.get_rect(midtop = (400, random_height))
    top_pipe = pipe_surface.get_rect(midbottom = (400, random_height - 120))
    return bottom_pipe, top_pipe

def move_pipe(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes

def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= 412:
            screen.blit(pipe_surface, pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface, False, True)
            screen.blit(flip_pipe, pipe)

def moving_floor():
    screen.blit(floor, (floor_x_position, 450))
    screen.blit(floor, (floor_x_position + 336 ,450))

def check_collision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            return False

    if bird_rect.top <= -75 or bird_rect.top >= 400:
        return False


    return True

def rotate_bird(surface):
    new_bird = pygame.transform.rotozoom(surface, bird_movement *-3, 1)
    return new_bird

def bird_animation():
    new_bird = bird_frame[bird_index]
    new_bird_rect = new_bird.get_rect(center = (100, bird_rect.centery))
    return new_bird, new_bird_rect

def score_display():
    score_surface = game_font.render('Score', True, (255, 255, 255))
    score_rect = score_surface.get_rect(center = (144, 100))
    screen.blit(score_surface, score_rect)




#Exit button code
while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:
                bird_movement = 0
                bird_movement -= 6

            if event.key == pygame.K_r and game_active == False:

                game_active = True
                pipe_list = []
                bird_rect.center = (100, 256)
                bird_movement = 0

        if event.type == SPAWNPIPE:
            pipe_list.extend(create_pipe())

        if event.type == BIRDFLAP:
            if bird_index < 2:
                bird_index += 1
            else:
                bird_index = 0

            bird_surface, bird_rect = bird_animation()


    #Displaying images onto the screen
    #_____________________________________
    screen.blit(bg_surface, (0,0))

    if game_active:
        #_____________________________________
        bird_movement += gravity

        rotated_bird = rotate_bird(bird_surface)

        bird_rect.centery += bird_movement
        screen.blit(rotated_bird, bird_rect)

        game_active = check_collision(pipe_list)

        #_____________________________________
        pipe_list = move_pipe(pipe_list)
        draw_pipes(pipe_list)

        #score_display()

    #_____________________________________
    floor_x_position -= 5
    moving_floor()
    if floor_x_position <= -336:
        floor_x_position = 0


    pygame.display.update()
    clock.tick(framerate)
