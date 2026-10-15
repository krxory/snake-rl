import pygame
import sys
import math
import random
"""
Make food
Make snake collion with walls
make snake collision with fruit
make snake collosion with itself
"""




pygame.init()
screen = pygame.display.set_mode((1280,880))
clock = pygame.time.Clock()

grid_size = 80
screen_size = (1280,880)
block_size = (80,80)


class Game:
    def __init__(self):
        self.head = ()
        self.tail = ()
        self.body = [()]
        self.direction = (1,0)
        self.food = 0
        self.snake_size = 78
        self.move_delay = 180
        self.last_move = 0
        self.food_cord = ()
        self.food_avail = False
        self.used_blocks = []
        self.total_blocks = []
        self.valid_blocks = []
        self.food_amount = 0
        self.running = True

    def turn(self, action):
        if action == 0:
            if self.direction == (1,0) or self.direction == (-1,0):
                pass
            else:
                self.direction = (1,0)

        elif action == 1:
            if self.direction == (1,0) or self.direction == (-1,0):
                pass
            else:
                self.direction = (-1,0)

        elif action == 2:
            if self.direction == (0,1) or self.direction == (0,-1):
                pass
            else:
                self.direction = (0,1)

        elif action == 3:
            if self.direction == (0,1) or self.direction == (0,-1):
                pass
            else:
                self.direction = (0,-1)

    def start(self):
        self.head = (block_X[4],block_Y[5])
        self.body = [(block_X[2], block_Y[5]), (block_X[3], block_Y[5])]
        self.tail = (block_X[1], block_Y[5])
        for x in block_X:
            for y in block_Y:
                self.total_blocks.append((x,y))

    def move(self):

        if self.head == self.food_cord:
            self.food_amount+= 1
            self.food_avail = False
            self.food_method()

            self.body.append(self.head)

            self.head = (self.head[0] + int(80 * self.direction[0]), self.head[1] + int(-80 * self.direction[1]))


            self.tail = self.body[0]



        else:
            if self.head[0] >= 1201 or self.head[1] >= 801 or self.head[0] <= -1 or self.head[1] <= -1 or \
                self.head in self.used_blocks[1:]:
                self.running = False

            self.body.append(self.head)
            self.head = (self.head[0]+int(80*self.direction[0]) ,self.head[1]+int(-80*self.direction[1]))
            self.tail = self.body[0]
            del self.body[0]
            self.used_blocks = [self.head, self.tail]
            self.used_blocks.extend(self.body)
            self.valid_blocks = [block for block in self.total_blocks if block not in self.used_blocks]
            print(self.used_blocks)
            print(self.valid_blocks)

    def food_method(self):
        if not self.food_avail:
            food_block_cord = random.choice(self.valid_blocks)
            self.food_cord = (food_block_cord[0], food_block_cord[1])
            self.food_avail = True




blocks =  tuple([int(screen_size[0]/grid_size),int(screen_size[1]/grid_size)])

block_X = []
block_Y = []
for x in range(0, blocks[0]):
    block_X.append(x*grid_size)
for y in range(0, blocks[1]):
    block_Y.append(y*grid_size)



game = Game()
game.start()
game.move()
game.food_method()

is_pressed = None

while game.running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and is_pressed == False:
                action = 0
                is_pressed = True
                game.turn(action)
            elif event.key == pygame.K_LEFT and is_pressed == False:
                action = 1
                is_pressed = True
                game.turn(action)
            elif event.key == pygame.K_UP and is_pressed == False:
                action = 2
                is_pressed = True
                game.turn(action)
            elif event.key == pygame.K_DOWN and is_pressed == False:
                action = 3
                is_pressed = True
                game.turn(action)

    screen.fill("green")

    for block in game.total_blocks:
        pygame.draw.rect(screen, "black", rect=(block[0], block[1], grid_size, grid_size), width=2)

    pygame.draw.rect(screen, "blue", rect=(game.head[0], game.head[1], 78, 78))
    pygame.draw.rect(screen, "blue", rect=(game.tail[0], game.tail[1], 78, 78))
    for x in game.body:
        pygame.draw.rect(screen, "blue", rect=(x[0], x[1], 78, 78))

    now = pygame.time.get_ticks()
    if now - game.last_move >= game.move_delay:
        game.move()
        game.last_move = now
        is_pressed = False

    pygame.draw.rect(screen, color="red", rect=(game.food_cord[0]+2, game.food_cord[1]+1, 77, 77))




    pygame.display.flip()
    clock.tick(60)
pygame.quit()