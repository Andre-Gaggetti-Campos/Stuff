import pygame
import sys
import math

class Shapes:

    def __init__(self, Drawer):

        self.drawer = Drawer
        self.vertices = []

    def add_vertex(self, pos):

        self.vertices.append(list(pos))

    def render(self):

        shapes = int(len(self.vertices)/2)

        for i in range(shapes):

            pygame.draw.rect(self.drawer.screen, (0, 0, 0), (min(self.vertices[2*i][0], self.vertices[2*i+1][0]), min(self.vertices[2*i][1], self.vertices[2*i+1][1]),abs(self.vertices[2*i][0]-self.vertices[2*i+1][0]), abs(self.vertices[2*i][1]-self.vertices[2*i+1][1])), 1)

class Selector:

    def __init__(self, Drawer, size, speed):

        self.drawer = Drawer
        self.size = size
        self.speed = speed
        self.pos = [int(self.drawer.screen.get_width()/2), int(self.drawer.screen.get_height()/2)]
        self.color = (0, 0, 0)

    def change_color(self, color):

        self.color = color

    def update(self, velocity):

        x_velocity = velocity[0]
        y_velocity = velocity[1]

        if velocity[0] != 0 and velocity[1] != 0:

            x_velocity /= math.sqrt(self.speed)
            y_velocity /= math.sqrt(self.speed)


        if self.pos[0] + velocity[0] > 0 and self.pos[0] + velocity[0] < self.drawer.screen.get_width():

            self.pos[0] += x_velocity

        if self.pos[1] + velocity[1] > 0 and self.pos[1] + velocity[1] < self.drawer.screen.get_height():

            self.pos[1] += y_velocity

    def render(self):

        pygame.draw.rect(self.drawer.screen, self.color, (self.pos[0]-self.size/2, self.pos[1]-self.size/2, self.size, self.size))

class Drawer:

    def __init__(self):

        pygame.init()

        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption("shape drawer")

        self.shapes = Shapes(self)
        self.selector = Selector(self, 6, 5)
        self.selector.velocity = [0, 0]

        self.directions = {pygame.K_UP: [0, -self.selector.speed], pygame.K_DOWN: [0, self.selector.speed], pygame.K_RIGHT: [self.selector.speed, 0], pygame.K_LEFT: [-self.selector.speed, 0]}
        
    
    def run(self):

        while True:

            self.screen.fill((255, 255, 255))

            for event in pygame.event.get():

                if event.type == pygame.QUIT:

                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_SPACE:

                        self.shapes.add_vertex(self.selector.pos)

                    if event.key in self.directions:

                        v = self.directions[event.key]
                        self.selector.velocity[0] += v[0]
                        self.selector.velocity [1] += v[1]

                if event.type == pygame.KEYUP:

                    if event.key in self.directions:

                        v = self.directions[event.key]
                        self.selector.velocity[0] -= v[0]
                        self.selector.velocity [1] -= v[1]

            self.selector.update(self.selector.velocity)

            self.selector.render()
            self.shapes.render()

            pygame.display.update()
            #self.clock.tick(60)

Drawer().run()