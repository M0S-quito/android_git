import pygame

colour = 0, 0, 255

class Obstacle:
    def __init__(self, x, size, GroundHeight):
        self.x = x
        self.size = size  # 튜플이 아닌 정수로 처리
        self.GroundHeight = GroundHeight

    def draw(self, gameDisplay):
        # 장애물 그리기
        pygame.draw.rect(gameDisplay, colour, [self.x, self.GroundHeight - self.size, self.size, self.size])

    def update(self, deltaTime, velocity):
        # 장애물 위치 업데이트
        self.x -= velocity * deltaTime

    def checkOver(self):
        # 장애물이 화면 밖으로 나가면 True 반환
        return self.x < 0