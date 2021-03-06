# importing libraries
import pygame
import time
import random
import sys
import os
import tkinter
from tkinter import*
from tkinter import CENTER, ttk, messagebox
from tkinter import Tk, Label, Button
import tkinter.messagebox
from tkinter.ttk import *
import tkinter as tk
from tkinter.messagebox import showinfo
from playsound import playsound
 
 



icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

snake_speed = 25
# Window size
window_x = 860
window_y = 630


 
# defining colors
Purple = pygame.Color(128,0,128)
white = pygame.Color(255,255,255)
purple = pygame.Color(230,230,250)
pink = pygame.Color(255,192,203)
blue = pygame.Color(0, 0, 255)
 
# Initialising pygame
pygame.init()
clock = pygame.time.Clock()
clock.tick(30)
# Initialise game window

pygame.display.set_caption('Hungry Snake 5.0 by Jonathan Steadman!')
game_window = pygame.display.set_mode((window_x, window_y))


 
# FPS (frames per second) controller
fps = pygame.time.Clock()
 
# defining snake default position
snake_position = [100, 60]
 
# defining first 4 blocks of snake body
snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]
              ]
# fruit position
fruit_position = [random.randrange(1, (window_x//10)) * 10,
                  random.randrange(1, (window_y//10)) * 10]
 
fruit_spawn = True
 
# setting default snake direction towards
# right
direction = 'RIGHT'
change_to = direction
 
# initial score
score = 0
 
# displaying Score function#
def show_score(choice, color, font, size):
    pygame.init()
    # creating font object score_font
    score_font = pygame.font.SysFont("Ubuntu", 25)
     
    # create the display surface object
    # score_surface
    score_surface = score_font.render('Number of Points: ' + str(score), True, color)
     
    # create a rectangular object for the text
    # surface object
    score_rect = score_surface.get_rect()
     
    # displaying text
    pygame.init()
    game_window.blit(score_surface, score_rect)
 
# game over function
def game_over():
    pygame.font.init()
   
    # creating font object my_font
    my_font = pygame.font.SysFont('Ubuntu', 60)
     
    # creating a text surface on which text
    # will be drawn
    playsound('sounds/mixkit-audience-light-applause-354.wav', block=False)

    game_over_surface = my_font.render(
        'Well done you got ' + str(score) +" points.", True, purple)
     
    # create a rectangular object for the text
    # surface object
    game_over_rect = game_over_surface.get_rect()
     
    # setting position of the text
    game_over_rect.midtop = (window_x/2, window_y/3)
     
    # blit will draw the text on screen
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
        # after 4 seconds we will quit the program
    time.sleep(4)    
    os.execl(sys.executable, sys.executable, *sys.argv)
    # restart the program
    
 
# Main Function
while True:
     
    # handling key events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

            if event.key == pygame.K_ESCAPE:
                pygame.quit()
 
    # If two keys pressed simultaneously
    # we don't want snake to move into two
    # directions simultaneously
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
 
    # Moving the snake
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10
 
    # Snake body growing mechanism
    # if fruits and snakes collide then scores
    # will be incremented by 10
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 1
        fruit_spawn = False
        playsound('sounds/mixkit-human-male-enjoy-humm-129.wav', block=False)
    else:
        snake_body.pop()
         
    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x//10)) * 10,
                          random.randrange(1, (window_y//10)) * 10]
         
    fruit_spawn = True
    game_window.fill(Purple)
     
    for pos in snake_body:
        pygame.draw.rect(game_window, pink,
                         pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, white, pygame.Rect(
        fruit_position[0], fruit_position[1], 10, 10))
 
    # Game Over conditions
    if snake_position[0] < 0 or snake_position[0] > window_x-10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y-10:
        game_over()
 
    # Touching the snake body
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()
 
    # displaying score countinuously
    show_score(2, white, 'Ubuntu', 90)
 
    # Refresh game screen
    pygame.display.update()
    
 
    # Frame Per Second /Refresh Rate
    fps.tick(snake_speed)



