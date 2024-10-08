import pygame

dinocolour = 255, 255, 255
DINOHEIGHT = 40
DINOWIDTH = 20

class Dinosaur:
    def __init__(self, surfaceHeight):
        self.x = 60
        self.y = 0
        self.yvelocity = 0
        self.height = DINOHEIGHT
        self.width = DINOWIDTH
        self.surfaceHeight = surfaceHeight

    def jump(self):
        if self.y == 0:  # 공중에서 점프하지 않도록 지면에 있을 때만 점프
            self.yvelocity = 300

    def update(self, deltaTime):
        self.yvelocity += -500 * deltaTime  # 중력 적용
        self.y += self.yvelocity * deltaTime
        if self.y < 0:  # 공룡이 지면 아래로 내려가면 위치와 속도를 0으로
            self.y = 0
            self.yvelocity = 0

    def draw(self, display):
        # 공룡을 화면에 그리기
        pygame.draw.rect(display, dinocolour, [self.x, self.surfaceHeight - self.y - self.height, self.width, self.height])