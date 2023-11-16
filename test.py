# Importing necessary libraries
import pygame
from pygame import mixer
import sys
import random

# Initializing pygame
pygame.init()

# Setting up the display
width = 400
height = 600
display = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# Loading sounds
sound1 = pygame.mixer.Sound('sounds\\sound1.wav')
sound2 = pygame.mixer.Sound('sounds\\sound2.mp3')
sound3 = pygame.mixer.Sound('sounds\\sound2.mp3')

# Setting up background colors
background = (23, 32, 42)
white = (236, 240, 241)
red = (176, 0, 0)
green = (7, 175, 12)

# Defining color codes for bricks
color = color = [(120, 40, 31), (148, 49, 38), (176, 58, 46), (203, 67, 53), (231, 76, 60), (236, 112, 99), (241, 148, 138), (245, 183, 177), (250, 219, 216), (253, 237, 236),
            (254, 249, 231), (252, 243, 207), (249, 231, 159), (247, 220, 111), (244, 208, 63), (241, 196, 15), (212, 172, 13), (183, 149, 11), (154, 125, 10), (125, 102, 8),
         (126, 81, 9), (156, 100, 12), (185, 119, 14), (202, 111, 30), (214, 137, 16), (243, 156, 18), (245, 176, 65), (248, 196, 113),(250, 215, 160), (253, 235, 208), (254, 245, 231),
         (232, 246, 243), (162, 217, 206), (162, 217, 206),
         (115, 198, 182), (69, 179, 157), (22, 160, 133),
         (19, 141, 117), (17, 122, 101), (14, 102, 85),
         (11, 83, 69),
         (21, 67, 96), (26, 82, 118), (31, 97, 141),
        (36, 113, 163), (41, 128, 185), (84, 153, 199),
        (127, 179, 213), (169, 204, 227), (212, 230, 241),
        (234, 242, 248),
         (251, 238, 230), (246, 221, 204), (237, 187, 153),
         (229, 152, 102), (220, 118, 51), (211, 84, 0),
         (186, 74, 0), (160, 64, 0), (135, 54, 0),
         (110, 44, 0)
         ] # List of RGB tuples for colors

# Initializing variables for brick dimensions, score, and speed
colorIndex = 0
brickH = 10
brickW = 100
score = 0
speed = 3

# Flags for tracking game state
setNR = False
perfect = False

# Handling file operations for the high score record
try:
    record = open('record.txt', 'x')
    record.close()
    record = open('record.txt', 'w')
    record.write('0')
    record.close()
except FileExistsError:
    pass

# Single Brick Class
class Brick:
    def __init__(self, x, y, color, speed):
        self.x = x
        self.y = y
        self.w = brickW
        self.h = brickH
        self.color = color
        self.speed = speed
        self.bounced = True  # Flag to track if the brick has bounced off an edge

    def draw(self):
        pygame.draw.rect(display, self.color, (self.x, self.y, self.w, self.h))

    def move(self):
        if self.bounced:
            while self.x + self.w > width:
                self.x -= self.speed
            self.bounced = False
        else:
            self.x -= self.speed
            if self.x + self.w > width or self.x < 0:
                self.speed *= -1
                self.bounced = True

# Complete Stack
class Stack:
    def __init__(self):
        global colorIndex
        self.stack = []
        self.initSize = 25
        for i in range(self.initSize):
            newBrick = Brick(width/2 - brickW/2, height - (i + 1) * brickH, color[colorIndex], 0)
            colorIndex += 1
            self.stack.append(newBrick)

    def show(self):
        for i in range(self.initSize):
            self.stack[i].draw()

    def move(self):
        for i in range(self.initSize):
            self.stack[i].move()

    def addNewBrick(self):
        global colorIndex, speed
        if colorIndex >= len(color):
            colorIndex = 0

        y = self.peek().y
        newBrick = Brick(width, y - brickH, color[colorIndex], speed)
        colorIndex += 1
        self.initSize += 1
        self.stack.append(newBrick)

    def peek(self):
        return self.stack[self.initSize - 1]

    def pushToStack(self, record):
        global brickW, score, setNR, perfect
        pygame.mixer.Sound.play(sound1)
        b = self.stack[self.initSize - 2]
        b2 = self.stack[self.initSize - 1]
        if b2.x <= b.x and not (b2.x + b2.w < b.x):
            self.stack[self.initSize - 1].w = self.stack[self.initSize - 1].x + self.stack[self.initSize - 1].w - b.x
            self.stack[self.initSize - 1].x = b.x
            if self.stack[self.initSize - 1].w > b.w:
                self.stack[self.initSize - 1].w = b.w
            self.stack[self.initSize - 1].speed = 0
            score += 1
            if not perfect and score > int(record):
                perfect = True
        elif b.x <= b2.x <= b.x + b.w:
            self.stack[self.initSize - 1].w = b.x + b.w - b2.x
            self.stack[self.initSize - 1].speed = 0
            score += 1
            if not perfect and score > int(record):
                perfect = True
        else:
            print(brickW)
            gameOver()
        for i in range(self.initSize):
            self.stack[i].y += brickH
        brickW = self.stack[self.initSize - 1].w
        if brickW < 1:
            gameOver()

# Game Over
def gameOver():
    mixer.music.pause()
    pygame.mixer.Sound.play(sound2)
    loop = True
    setNR = False
    perfect = False
    with open('record.txt', 'r') as file:
        record = file.read()
        if score > int(record):
            with open('record.txt', 'w') as file2:
                file2.write(str(score))
                setNR = True
    with open('record.txt', 'r') as file:
        record = file.read()
        font1 = pygame.font.SysFont("Agency FB", 60)
        font2 = pygame.font.SysFont("Forte", 30)
        text = font1.render("Game Over!", True, white)
        textRect = text.get_rect()
        textRect.center = (width/2, height/2 - 80)
        if setNR:
            text2 = font2.render("Record: " + str(record), True, green)
        else:
            text2 = font2.render("Record: " + str(record), True, red)
        display.blit(text2, (10, 50))
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    close()
                if event.key == pygame.K_r or event.key == pygame.K_SPACE:
                    gameLoop()
            if event.type == pygame.MOUSEBUTTONDOWN:
                gameLoop()
        display.blit(text, textRect)
        pygame.display.update()
        clock.tick()
    setNR = False

# Displaying the Score on Screen
def showScore():
    font = pygame.font.SysFont("Forte", 30)
    text1 = font.render("Score: " + str(score), True, white)
    display.blit(text1, (10, 10))

# Close the Window
def close():
    pygame.quit()
    sys.exit()

# The Main Game Loop
def gameLoop():
    global brickW, brickH, score, colorIndex, speed, start
    start = False
    loop = True
    brickH = 10
    brickW = 100
    colorIndex = 0
    speed = 3
    score = 0
    with open('record.txt', 'r') as file:
        record = file.read()
    mixer.music.load('sounds\\music.mp3')
    mixer.music.play(-1)
    stack = Stack()
    stack.addNewBrick()
    while loop:
        print(brickW)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    close()
                if event.key == pygame.K_r:
                    gameLoop()
                if event.key == pygame.K_SPACE:
                    stack.pushToStack(record)
                    stack.addNewBrick()
            if event.type == pygame.MOUSEBUTTONDOWN:
                stack.pushToStack(record)
                stack.addNewBrick()
        display.fill(background)
        stack.move()
        stack.show()
        showScore()
        pygame.display.update()
        clock.tick(60)

# Starting the game loop
gameLoop()
