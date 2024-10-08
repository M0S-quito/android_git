import pygame
from dinosaur import Dinosaur  # 'dinosaur' 파일에서 Dinosaur 클래스를 가져옵니다
from obstacle import Obstacle
import random

# Pygame 초기화
pygame.init()

# 화면 크기 설정
size = width, height = 640, 480
gameDisplay = pygame.display.set_mode(size)
pygame.display.set_caption("Dinosaur Game")  # 게임 창 제목 설정

# 색상 및 변수 설정
xPos = 0
yPos = 0
black = 0, 0, 0
white = 255, 255, 255
GROUND_HEIGHT = height - 100

# 공룡 객체 생성
dinosaur = Dinosaur(GROUND_HEIGHT)

# 시간 계산 변수
lastFrame = pygame.time.get_ticks()

# 장애물 관련 변수 설정
MINGAP = 200
VELOCITY = 300
MAXGAP = 600
obstacles = []
lastObstacle = width

# 장애물 생성
for i in range(4):
    lastObstacle += MINGAP + (MAXGAP - MINGAP) * random.random()  # 장애물 간의 거리를 무작위로 설정
    obstacles.append(Obstacle(lastObstacle, random.randint(20, 50), GROUND_HEIGHT))

# 게임 루프
running = True
while running:
    # 현재 시간과 프레임 계산
    t = pygame.time.get_ticks()
    deltaTime = (t - lastFrame) / 1000.0
    lastFrame = t

    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                dinosaur.jump()  # 스페이스바를 누르면 공룡이 점프

    # 화면 색상 채우기
    gameDisplay.fill(black)

    # 공룡 업데이트 및 그리기
    dinosaur.update(deltaTime)
    dinosaur.draw(gameDisplay)

    # 장애물 업데이트 및 그리기
    for obs in obstacles:
        obs.update(deltaTime, VELOCITY)
        obs.draw(gameDisplay)
        if obs.checkOver():
            lastObstacle += MINGAP + (MAXGAP - MINGAP) * random.random()
            obs.x = lastObstacle

    # 장애물 위치 업데이트
    lastObstacle -= VELOCITY * deltaTime

    # 지면 그리기
    pygame.draw.rect(gameDisplay, white, [0, GROUND_HEIGHT, width, height - GROUND_HEIGHT])

    # Pygame 디스플레이 업데이트
    pygame.display.flip()

# Pygame 종료
pygame.quit()