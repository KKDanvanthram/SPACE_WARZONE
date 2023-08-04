import pygame
pygame.init()
from pygame import mixer

pygame.font.init()

pygame.init()

WIDTH, HEIGHT = 1080,1080

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('BattleGrounds!!!')

WHITE = (255,255,255)

BLACK=(0,0,0)

BLUE=(0,0,255)

WINNER_FONT=pygame.font.SysFont('arial',100)

RED=(255,0,0)

YELLOW=(255,255,0)

GREEN=(0,255,0)

FPS=60

YELLOW_HIT=pygame.USEREVENT+1

RED_HIT=pygame.USEREVENT+2

VEL=5

MAX_BULLETs = 1

RDM=(100,60,20)

BULLET_VEL=10

HEALTH_FONT = pygame.font.SysFont('comicsans',20)

BORDER=pygame.Rect(WIDTH//2-5,0,10,HEIGHT)

SPACESHIP_WIDTH,SPACESHIP_HEIGHT= 50,40
YELLOW_SPACESHIP_IMAGE=pygame.image.load('gun1.png')
YELLOW_SPACESHIP =pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE,(100,60)),0)
RED_SPACESHIP_IMAGE=pygame.image.load('gun.png')
RED_SPACESHIP=pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE,(100,60)),0)
SPACE = pygame.image.load('download.jpg')
SPACE1=pygame.transform.scale(SPACE,(WIDTH,HEIGHT))

def draw_window(red,yellow,red_bullets,yellow_bullets,red_health,yellow_health):
    WIN.fill(WHITE)
    WIN.blit(SPACE1, (0,0))

    red_health_text=HEALTH_FONT.render('Health:'+str(red_health),1,RED)
    yellow_health_text = HEALTH_FONT.render('Health:' + str(yellow_health), 1, YELLOW)
    WIN.blit(red_health_text,(725,0))
    WIN.blit(yellow_health_text,(0,0))
    WIN.blit(YELLOW_SPACESHIP,(yellow.x,yellow.y))
    WIN.blit(RED_SPACESHIP,(red.x,red.y))
    for bullet in red_bullets:
        pygame.draw.rect(WIN,RED,bullet)
    for bullet in yellow_bullets:
        pygame.draw.rect(WIN,GREEN,bullet)
    pygame.display.update()

def draw_winner(text):
    draw_text=WINNER_FONT.render(text,1,BLUE)
    WIN.blit(draw_text,(WIDTH//2-draw_text.get_width()//2,HEIGHT//2-draw_text.get_height()//2))
    pygame.display.update()
    pygame.time.delay(5000)
def yellow_handle_movement(keys_pressed,yellow):
    if keys_pressed[pygame.K_a] and yellow.x - VEL > 0:
        yellow.x -= VEL
    if keys_pressed[pygame.K_d] and yellow.x + VEL < BORDER.x-95:
        yellow.x += VEL
    if keys_pressed[pygame.K_w] and yellow.y - VEL > 0:
        yellow.y -= VEL
    if keys_pressed[pygame.K_s] and yellow.y + VEL < HEIGHT-45:
        yellow.y += VEL


def red_handle_movement(keys_pressed,red):
    if keys_pressed[pygame.K_LEFT] and red.x -VEL > 450:
        red.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL <800:
        red.x += VEL
    if keys_pressed[pygame.K_UP] and red.y - VEL > 0:
        red.y -= VEL
    if keys_pressed[pygame.K_DOWN] and red.y - VEL < HEIGHT-58:
        red.y += VEL

def handle_bullets(yellow_bullets,red_bullets,yellow, red):
    for bullet in yellow_bullets:
        bullet.x+=BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet)
    for bullet in red_bullets:
        bullet.x-=BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x<0:
            red_bullets.remove(bullet)
mixer.music.load('App1.wav')
mixer.music.play(-1)



def main():
    red = pygame.Rect(700, 300,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    red_bullets = []
    yellow_bullets=[]
    red_health=5
    yellow_health=5

    clock=pygame.time.Clock()
    run=True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                pygame.quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LCTRL and len(yellow_bullets)<MAX_BULLETs:
                    bullet=pygame.Rect(yellow.x+yellow.width,yellow.y+yellow.height//2-2,10,5)
                    yellow_bullets.append(bullet)

                if event.key==pygame.K_RCTRL and len(red_bullets)< MAX_BULLETs:
                    bullet=pygame.Rect(red.x,red.y+red.height//2-2,10,5)
                    red_bullets.append(bullet)
            if event.type==RED_HIT:
                red_health-=1

            if event.type==YELLOW_HIT:
                yellow_health-=1

        winner_text=""
        if red_health<=0:
            winner_text='YELLOW WINS'

        if yellow_health<=0:
            winner_text='RED WINS'

        if winner_text!="":
            draw_winner(winner_text)
            break

        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed,yellow)
        red_handle_movement(keys_pressed,red)
        handle_bullets(yellow_bullets,red_bullets,yellow , red)
        draw_window(red,yellow,red_bullets,yellow_bullets,red_health,yellow_health)
    main()

if __name__=="__main__":
    main()
    pygame.quit()
