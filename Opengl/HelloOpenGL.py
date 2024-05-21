import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()

screen_width = 1000
screen_height = 800

screen = pygame.display.set_mode((screen_width,screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('OpenGL in Python')

def init_ortho():
    glMatrixMode(GL_PROJECTION) # 카메라, 세계가 투영되는 곳
    glLoadIdentity()
    gluOrtho2D(0, 1000, 800, 0)

def draw_star(size, x, y):
    glPointSize(size)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()

done = False
init_ortho()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW) # 기본적으로 무언가를 그리게 동작하도록 하는 곳이다
    glLoadIdentity()

    # 실제 무언가가 그려지는 부분
    draw_star(30, 30, 300)
    draw_star(5, 200, 250)
    draw_star(15, 250, 200)
    draw_star(10, 260, 150)

    pygame.display.flip()
    pygame.time.wait(100)
pygame.quit()
