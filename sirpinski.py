import pygame
from random import randint, choice
import sys
import math
from time import sleep
#sets recursion limit higher than python's default-->THE INTERNET SAID IT COULD BE DANGEROUS
sys.setrecursionlimit(200000)

#constants
#colors
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
#circle stuff
H, K = 350, 350
RADIUS = 350
ITERATIONS = 18000
#empty list for lines of polygon with limits
possible_lines = []


#Iinitialize pygame; set window size; set window caption
pygame.init()
window = pygame.display.set_mode((700, 700))
pygame.display.set_caption("sierpinski's triangle")
#font
#print(pygame.font.get_fonts()) <-- list of available fonts
font = pygame.font.SysFont('ヒラキノ角コシックw8', 32, False, False)

#iterations to do:
iterations = 180000

#pause game functionality
def pause_game(event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            pause = True
            while pause:
                for action in pygame.event.get():
                    if action.type == pygame.KEYDOWN:
                        if action.key == pygame.K_SPACE:
                            pause = False

#class for dots of shape, save some hassle
class Dot:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
        self.color = BLUE
        self.size = 1


    #draws dot as pygame circle
    def draw(self):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.size)

    #finds midpoint between called dot and dot in parameter
    def find_midpoint(self, dot_b):
        return [(self.x + dot_b.x)/2, (self.y + dot_b.y)/2]

#polygon class for making shape
class Polygon:
    def __init__(self, sides):
        self.sides = sides
        self.points = []
        self.angle_between = int((360/sides)+0.5)
        self.find_points()


    def find_points(self):
        #gets points of polygon--rotates clockwise
        one_segment = math.pi * 2 / self.sides
        points = [(math.sin(one_segment * i) * RADIUS, math.cos(one_segment * i) * RADIUS) for i in range(self.sides)]
        points = [[sum(pair) for pair in zip(point, [H, K])] for point in points]

        for point in points:
            #appends Dot object to points
            self.points.append(Dot(point[0], point[1]))

class linear_line:
    def __init__(self, dot1, dot2):
        self.dot1 = dot1
        self.dot2 = dot2
        #make slope and y-int of line
        self.m = (dot2.y - dot1.y) / (dot2.x - dot1.x)
        self.b = self.dot1.y - (self.m * self.dot1.x)
        self.lower_limit = 0
        self.higher_limit = 0

        #sets limits of equation
        if self.dot1.x < self.dot2.x:
            self.lower_limit = self.dot1.x
            self.higher_limit = self.dot2.x
        else:
            self.lower_limit = self.dot2.x
            self.higher_limit = self.dot1.x

    #returns tuple of if x will work fits and corresponding y val
    def saucy(self, x):
        if x > self.higher_limit or x < self.lower_limit:
            return [False,  (self.m * x) + self.b]
        return [True, (self.m * x) + self.b]


#uses recurion to draw dot then use that dot in the next iteration
def sirpinski(iteration, temp, polygon_obj):
    if iteration <= 0:
        return 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        #--cannot quit game while its paused--
        pause_game(event)

    #draws and displays dot
    temp.draw()
    pygame.display.update()
    #finds midpoint and puts it as new point
    mid_point = temp.find_midpoint(choice(polygon_obj.points))
    sirpinski(iteration-1, Dot(mid_point[0], mid_point[1]), polygon_obj)


#start of game
p = Polygon(int(input("enter how many sides of polygon: ")))
print("press enter on pygame window to begin\npress space on pygame window to pause process")

for i in range(1, len(p.points)):
    possible_lines.append(linear_line(p.points[i-1], p.points[i]))

rand_x = randint(10, 690)
line = choice(possible_lines)
#finds line that fits x
while line.saucy(rand_x)[0] != True:
    line = choice(possible_lines)

#creates initial dot
temp = Dot(rand_x, line.saucy(rand_x)[1])


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        pause_game(event)
        #if return pressed screen is cleared, random point chosen and sierpinski alg begins
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                window.fill(BLACK)
                # draw initial points: A B C
                for point in p.points:
                    point.color = (255, 0, 0)
                    point.size = 5
                    point.draw()

                sirpinski(ITERATIONS, temp, p)

