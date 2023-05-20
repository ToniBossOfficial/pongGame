from pygame import *

init()

# Set up the drawing window
window_width = 1000
window_heigth = 700
window = display.set_mode([window_width, window_heigth])
clock = time.Clock()

#parent class for sprites
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height, speedX=0, speedY=0):
       super().__init__()
       self.image = transform.scale(image.load(player_image), (wight, height)) #e.g. 55,55 - parameters
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
       self.speedX=speedX
       self.speedY=speedY


    def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))
    def goUp(self):
       
       self.rect.y -= self.speed
    def goDown(self):
       self.rect.y += self.speed
    def move(self):
       self.rect.y += self.speedY
       self.rect.x += self.speedX
BallWidth = 100
BallHeigth = 100

Ball = GameSprite("assets/ball.png", window_width/2-BallWidth/2, window_heigth/2-BallHeigth/2, 0, BallWidth, BallHeigth,6,6)

BarriersHeigth = window_heigth/2
BarriersWidth = 80
BarriersX = 50

Barrier1 = GameSprite("assets/barrier.png",BarriersX , window_heigth/2-BallHeigth/2, 6, BarriersWidth, BarriersHeigth)
Barrier2 = GameSprite("assets/barrier.png",window_width-BarriersX-BarriersWidth , window_heigth/2-BallHeigth/2, 6, BarriersWidth, BarriersHeigth)
FPS = 60

Game = True
loose = False
while Game:

    window.fill((255,255,0))

    Ball.reset()
    Barrier1.reset()
    Barrier2.reset()
    

    keys=key.get_pressed()
    if not loose:
        Ball.move()
        if keys[K_DOWN]:
            if Barrier2.rect.y < window_heigth-BarriersHeigth-Barrier2.speed:
                Barrier2.goDown()
        elif keys[K_UP]:
            if Barrier2.rect.y > 0 + Barrier2.speed:
                Barrier2.goUp()
        if keys[K_w]:
            if Barrier1.rect.y > 0 + Barrier1.speed:
                Barrier1.goUp()
        elif keys[K_s]:
            if Barrier1.rect.y < window_heigth-BarriersHeigth-Barrier1.speed:
                Barrier1.goDown()

        Barriers = [Barrier1,Barrier2]
        ball_hit_list = sprite.spritecollide(Ball, Barriers, False)
        for hit in ball_hit_list:
            Ball.speedY*=-1
            Ball.speedX*=-1
        if Ball.rect.y<10:
            Ball.speedY*=-1
        elif Ball.rect.y>window_heigth-BallHeigth-10:
            Ball.speedY*=-1
    
    if Ball.rect.x < Barrier1.rect.x or Ball.rect.x > Barrier2.rect.x + 5:
        loose = True
        Ball.speedX *= -1
        

    for e in event.get():
        


        if e.type == QUIT:
            exit()

    display.update()
    clock.tick(FPS)

