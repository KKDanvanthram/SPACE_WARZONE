from tkinter import *
import pygame
import pyttsx3
from pygame import mixer
pygame.init()
from PIL import ImageTk,Image
import mysql.connector as sq
db=sq.connect(user='root',passwd='1234',host='localhost')
cur=db.cursor()
cur.execute('create database if not exists kkd')
cur.execute('use kkd')
cur.execute('create table if not exists user(name varchar(20),passwd varchar(20))')
cur.execute('create table if not exists game(red_player varchar(20),yellow_player varchar(20),winner varchar(20),point_diff varchar(20))')
from tkinter import messagebox
def diff():
    engine = pyttsx3.init()
    engine.say('Choose Your Difficulty wisely')
    engine.runAndWait()
def game_easy():
    try:
        import pygame

        pygame.font.init()

        pygame.init()

        WIDTH, HEIGHT = 900, 500

        WIN = pygame.display.set_mode((WIDTH, HEIGHT))

        pygame.display.set_caption('BattleGrounds!!! GAMEMODE=EASY')

        WHITE = (255, 255, 255)

        BLACK = (0, 0, 0)

        BLUE = (0, 0, 255)

        WINNER_FONT = pygame.font.SysFont('comicsans', 100)

        RED = (255, 0, 0)

        YELLOW = (255, 255, 0)

        GREEN = (0, 255, 0)

        FPS = 60
        YELLOW_HIT = pygame.USEREVENT + 1

        RED_HIT = pygame.USEREVENT + 2

        VEL = 5

        MAX_BULLETs = 3

        RDM = (100, 60, 20)

        BULLET_VEL = 7

        HEALTH_FONT = pygame.font.SysFont('comicsans', 20)

        BORDER = pygame.Rect(WIDTH // 2 - 5, 0, 10, HEIGHT)

        GUN_WIDTH, GUN_HEIGHT = 50, 40

        YELLOW_GUN_IMAGE = pygame.image.load('gun1.png')

        YELLOW_GUN = pygame.transform.rotate(pygame.transform.scale(YELLOW_GUN_IMAGE, (100, 60)), 0)

        RED_GUN_IMAGE = pygame.image.load('gun.png')

        RED_GUN = pygame.transform.rotate(pygame.transform.scale(RED_GUN_IMAGE, (100, 60)), 0)

        BG = pygame.image.load('download.jpg')

        BG1 = pygame.transform.scale(BG, (WIDTH, HEIGHT))

        def draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
            WIN.fill(WHITE)
            WIN.blit(BG1, (0, 0))

            red_health_text = HEALTH_FONT.render('Health:' + str(red_health),True, YELLOW)
            yellow_health_text = HEALTH_FONT.render('Health:' + str(yellow_health), 1, RED
                                                    )
            WIN.blit(red_health_text, (725, 0))
            WIN.blit(yellow_health_text, (0, 0))
            WIN.blit(YELLOW_GUN, (yellow.x, yellow.y))
            WIN.blit(RED_GUN, (red.x, red.y))
            for bullet in red_bullets:
                pygame.draw.rect(WIN, RED, bullet)
            for bullet in yellow_bullets:
                pygame.draw.rect(WIN, GREEN, bullet)
            pygame.display.update()

        def draw_winner(text):
            draw_text = WINNER_FONT.render(text, 1, BLUE)
            WIN.blit(draw_text, (WIDTH // 2 - draw_text.get_width() // 2, HEIGHT // 2 - draw_text.get_height() // 2))
            pygame.display.update()
            pygame.time.delay(5000)

        def yellow_movement(keys_pressed, yellow):
            if keys_pressed[pygame.K_a] and yellow.x - VEL > 0:
                yellow.x -= VEL
            if keys_pressed[pygame.K_d] and yellow.x + VEL < BORDER.x - 95:
                yellow.x += VEL
            if keys_pressed[pygame.K_w] and yellow.y - VEL > 0:
                yellow.y -= VEL
            if keys_pressed[pygame.K_s] and yellow.y + VEL < HEIGHT - 45:
                yellow.y += VEL

        def red_movement(keys_pressed, red):
            if keys_pressed[pygame.K_LEFT] and red.x - VEL > 450:
                red.x -= VEL
            if keys_pressed[pygame.K_RIGHT] and red.x + VEL < 800:
                red.x += VEL
            if keys_pressed[pygame.K_UP] and red.y - VEL > 0:
                red.y -= VEL
            if keys_pressed[pygame.K_DOWN] and red.y - VEL < HEIGHT - 58:
                red.y += VEL

        def handle_bullets(yellow_bullets, red_bullets, yellow, red):
            for bullet in yellow_bullets:
                bullet.x += BULLET_VEL
                if red.colliderect(bullet):
                    pygame.event.post(pygame.event.Event(RED_HIT))
                    yellow_bullets.remove(bullet)
                elif bullet.x > WIDTH:
                    yellow_bullets.remove(bullet)
            for bullet in red_bullets:
                bullet.x -= BULLET_VEL
                if yellow.colliderect(bullet):
                    pygame.event.post(pygame.event.Event(YELLOW_HIT))
                    red_bullets.remove(bullet)
                elif bullet.x < 0:
                    red_bullets.remove(bullet)

        def main():
            red = pygame.Rect(700, 300, GUN_WIDTH, GUN_HEIGHT)
            yellow = pygame.Rect(100, 300, GUN_WIDTH, GUN_HEIGHT)
            red_bullets = []
            yellow_bullets = []
            red_health = 5
            yellow_health = 5

            clock = pygame.time.Clock()
            run = True
            while run:
                clock.tick(FPS)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                        pygame.quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETs:
                            bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height // 2 - 2, 10, 5)
                            yellow_bullets.append(bullet)

                        if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETs:
                            bullet = pygame.Rect(red.x, red.y + red.height // 2 - 2, 10, 5)
                            red_bullets.append(bullet)
                    if event.type == RED_HIT:
                        red_health -= 1

                    if event.type == YELLOW_HIT:
                        yellow_health -= 1
                winner_text = ""
                if red_health <= 0:
                    winner_text = e.get() + ' WINS'
                    st=f"insert into game values('{e.get()}','{e1.get()}','{e.get()}','{red_health-yellow_health}')"
                    cur.execute(st)
                    db.commit()

                if yellow_health <= 0:
                    winner_text = e1.get() + ' WINS'
                    st=f"insert into game values('{e.get()}','{e1.get()}','{e1.get()}','{-red_health+yellow_health}')"
                    cur.execute(st)
                    db.commit()

                if winner_text != "":
                    draw_winner(winner_text)
                    break

                keys_pressed = pygame.key.get_pressed()
                yellow_movement(keys_pressed, yellow)
                red_movement(keys_pressed, red)
                handle_bullets(yellow_bullets, red_bullets, yellow, red)
                draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health)
            main()

        if __name__ == "__main__":
            main()
    except pygame.error:
        pass


def prt():
    Label(root, text='Welcome ' + e.get(),font='arial').grid(row=6,column=0)
    Label(root,text='Welcome '+e1.get(),font='arial').grid(row=6,column=2)
def fig():
    my_img = ImageTk.PhotoImage(Image.open('Fantom.png'))
    mylabel = Label(top, image=my_img)
    mylabel.pack()
def mass():
    diff()
    global top
    top = Toplevel()
    top.resizable(False,False)
    appwidth = 270
    appheight = 290
    top.config(bg='grey')
    original_width = top.winfo_screenwidth()
    original_height = top.winfo_screenheight()
    top.geometry(f'{appwidth}x{appheight}+{int(original_width / 2) - int(appwidth / 2)}+{int(original_height / 2) - int(appheight / 2)}')
    top.title("Let's Gooo!!!!")
    top.iconbitmap('kkdjjj.ico')
    my_img = ImageTk.PhotoImage(Image.open('Fantom.png'))
    mylabel = Label(top, image=my_img)
    mylabel.pack()
    Label(top,text='Choose Your Level Wisely:]').pack()
    btn2=Button(top,text='Easy',command=game_easy,padx=25,fg='red',bg='black')
    btn2.pack()
    btn3=Button(top,text='Medium',command=game_medium,padx=25,fg='red',bg='black')
    btn3.pack()
    btn4=Button(top,text='Hard',command=game_hard,padx=25,fg='red',bg='black')
    btn4.pack()
    fig()
    top.mainloop()

def game_medium():
    try:
        import pygame

        pygame.font.init()

        pygame.init()

        WIDTH, HEIGHT = 900, 500

        WIN = pygame.display.set_mode((WIDTH, HEIGHT))

        pygame.display.set_caption('BattleGrounds!!! GAMEMODE=MEDIUM')

        WHITE = (255, 255, 255)

        BLACK = (0, 0, 0)

        BLUE = (0, 0, 255)

        WINNER_FONT = pygame.font.SysFont('comicsans', 100)

        RED = (255, 0, 0)

        YELLOW = (255, 255, 0)

        GREEN = (0, 255, 0)

        FPS = 60

        YELLOW_HIT = pygame.USEREVENT + 1

        RED_HIT = pygame.USEREVENT + 2

        VEL = 7

        MAX_BULLETs = 3

        RDM = (100, 60, 20)

        BULLET_VEL = 10

        HEALTH_FONT = pygame.font.SysFont('comicsans', 20)

        BORDER = pygame.Rect(WIDTH // 2 - 5, 0, 10, HEIGHT)

        GUN_WIDTH, GUN_HEIGHT = 50, 40

        YELLOW_GUN_IMAGE = pygame.image.load('gun1.png')

        YELLOW_GUN = pygame.transform.rotate(pygame.transform.scale(YELLOW_GUN_IMAGE, (100, 60)), 0)

        RED_GUN_IMAGE = pygame.image.load('gun.png')

        RED_GUN = pygame.transform.rotate(pygame.transform.scale(RED_GUN_IMAGE, (100, 60)), 0)

        BG = pygame.image.load('download.jpg')

        BG1 = pygame.transform.scale(BG, (WIDTH, HEIGHT))

        def draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
            WIN.fill(WHITE)
            WIN.blit(BG1, (0, 0))

            red_health_text = HEALTH_FONT.render('Health:' + str(red_health), 1,YELLOW)
            yellow_health_text = HEALTH_FONT.render('Health:' + str(yellow_health), 1, RED)
            WIN.blit(red_health_text, (725, 0))
            WIN.blit(yellow_health_text, (0, 0))
            WIN.blit(YELLOW_GUN, (yellow.x, yellow.y))
            WIN.blit(RED_GUN, (red.x, red.y))
            for bullet in red_bullets:
                pygame.draw.rect(WIN, RED, bullet)
            for bullet in yellow_bullets:
                pygame.draw.rect(WIN, GREEN, bullet)
            pygame.display.update()

        def draw_winner(text):
            draw_text = WINNER_FONT.render(text, 1, BLUE)
            WIN.blit(draw_text, (WIDTH // 2 - draw_text.get_width() // 2, HEIGHT // 2 - draw_text.get_height() // 2))
            pygame.display.update()
            pygame.time.delay(5000)

        def yellow_movement(keys_pressed, yellow):
            if keys_pressed[pygame.K_a] and yellow.x - VEL > 0:
                yellow.x -= VEL
            if keys_pressed[pygame.K_d] and yellow.x + VEL < BORDER.x - 95:
                yellow.x += VEL
            if keys_pressed[pygame.K_w] and yellow.y - VEL > 0:
                yellow.y -= VEL
            if keys_pressed[pygame.K_s] and yellow.y + VEL < HEIGHT - 45:
                yellow.y += VEL

        def red_movement(keys_pressed, red):
            if keys_pressed[pygame.K_LEFT] and red.x - VEL > 450:
                red.x -= VEL
            if keys_pressed[pygame.K_RIGHT] and red.x + VEL < 800:
                red.x += VEL
            if keys_pressed[pygame.K_UP] and red.y - VEL > 0:
                red.y -= VEL
            if keys_pressed[pygame.K_DOWN] and red.y - VEL < HEIGHT - 58:
                red.y += VEL

        def handle_bullets(yellow_bullets, red_bullets, yellow, red):
            for bullet in yellow_bullets:
                bullet.x += BULLET_VEL
                if red.colliderect(bullet):
                    pygame.event.post(pygame.event.Event(RED_HIT))
                    yellow_bullets.remove(bullet)
                elif bullet.x > WIDTH:
                    yellow_bullets.remove(bullet)
            for bullet in red_bullets:
                bullet.x -= BULLET_VEL
                if yellow.colliderect(bullet):
                    pygame.event.post(pygame.event.Event(YELLOW_HIT))
                    red_bullets.remove(bullet)
                elif bullet.x < 0:
                    red_bullets.remove(bullet)

        def main():
            red = pygame.Rect(700, 300, GUN_WIDTH, GUN_HEIGHT)
            yellow = pygame.Rect(100, 300, GUN_WIDTH, GUN_HEIGHT)
            red_bullets = []
            yellow_bullets = []
            red_health = 5
            yellow_health = 5

            clock = pygame.time.Clock()
            run = True
            while run:
                clock.tick(FPS)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                        pygame.quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETs:
                            bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height // 2 - 2, 10, 5)
                            yellow_bullets.append(bullet)

                        if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETs:
                            bullet = pygame.Rect(red.x, red.y + red.height // 2 - 2, 10, 5)
                            red_bullets.append(bullet)
                    if event.type == RED_HIT:
                        red_health -= 1

                    if event.type == YELLOW_HIT:
                        yellow_health -= 1
                winner_text = ""
                if red_health <= 0:
                    winner_text = e.get() + ' WINS'
                    st=f"insert into game values('{e.get()}','{e1.get()}','{e.get()}','{red_health-yellow_health}')"
                    cur.execute(st)
                    db.commit()

                if yellow_health <= 0:
                    winner_text = e1.get() + ' WINS'
                    st=f"insert into game values('{e.get()}','{e1.get()}','{e1.get()}','{-red_health+yellow_health}')"
                    cur.execute(st)
                    db.commit()

                if winner_text != "":
                    draw_winner(winner_text)
                    break

                keys_pressed = pygame.key.get_pressed()
                yellow_movement(keys_pressed, yellow)
                red_movement(keys_pressed, red)
                handle_bullets(yellow_bullets, red_bullets, yellow, red)
                draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health)
            main()

        if __name__ == "__main__":
            main()
    except pygame.error:
        pass
def game_hard():
    try:

        import pygame

        pygame.font.init()

        pygame.init()

        WIDTH, HEIGHT = 900, 500

        WIN = pygame.display.set_mode((WIDTH, HEIGHT))

        pygame.display.set_caption('BattleGrounds!!! GAMEMODE=HARD')

        WHITE = (255, 255, 255)

        BLACK = (0, 0, 0)

        BLUE = (0, 0, 255)

        WINNER_FONT = pygame.font.SysFont('comicsans', 100)

        RED = (255, 0, 0)

        YELLOW = (255, 255, 0)

        GREEN = (0, 255, 0)

        FPS = 60
        YELLOW_HIT = pygame.USEREVENT + 1

        RED_HIT = pygame.USEREVENT + 2

        VEL = 10

        MAX_BULLETs = 3

        RDM = (100, 60, 20)

        BULLET_VEL = 15

        HEALTH_FONT = pygame.font.SysFont('comicsans', 20)

        BORDER = pygame.Rect(WIDTH // 2 - 5, 0, 10, HEIGHT)

        GUN_WIDTH, GUN_HEIGHT = 50, 40

        YELLOW_GUN_IMAGE = pygame.image.load('gun1.png')

        YELLOW_GUN = pygame.transform.rotate(pygame.transform.scale(YELLOW_GUN_IMAGE, (100, 60)), 0)

        RED_GUN_IMAGE = pygame.image.load('gun.png')

        RED_GUN = pygame.transform.rotate(pygame.transform.scale(RED_GUN_IMAGE, (100, 60)), 0)

        BG = pygame.image.load('download.jpg')

        BG1 = pygame.transform.scale(BG, (WIDTH, HEIGHT))

        def draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
            WIN.fill(WHITE)
            WIN.blit(BG1, (0, 0))

            red_health_text = HEALTH_FONT.render('Health:' + str(red_health), 1,YELLOW)
            yellow_health_text = HEALTH_FONT.render('Health:' + str(yellow_health), 1, RED)
            WIN.blit(red_health_text, (725, 0))
            WIN.blit(yellow_health_text, (0, 0))
            WIN.blit(YELLOW_GUN, (yellow.x, yellow.y))
            WIN.blit(RED_GUN, (red.x, red.y))
            for bullet in red_bullets:
                pygame.draw.rect(WIN, RED, bullet)
            for bullet in yellow_bullets:
                pygame.draw.rect(WIN, GREEN, bullet)
            pygame.display.update()

        def draw_winner(text):
            draw_text = WINNER_FONT.render(text, 1, BLUE)
            WIN.blit(draw_text, (WIDTH // 2 - draw_text.get_width() // 2, HEIGHT // 2 - draw_text.get_height() // 2))
            pygame.display.update()
            pygame.time.delay(5000)

        def yellow_movement(keys_pressed, yellow):
            if keys_pressed[pygame.K_a] and yellow.x - VEL > 0:
                yellow.x -= VEL
            if keys_pressed[pygame.K_d] and yellow.x + VEL < BORDER.x - 95:
                yellow.x += VEL
            if keys_pressed[pygame.K_w] and yellow.y - VEL > 0:
                yellow.y -= VEL
            if keys_pressed[pygame.K_s] and yellow.y + VEL < HEIGHT - 45:
                yellow.y += VEL

        def red_movement(keys_pressed, red):
            if keys_pressed[pygame.K_LEFT] and red.x - VEL > 450:
                red.x -= VEL
            if keys_pressed[pygame.K_RIGHT] and red.x + VEL < 800:
                red.x += VEL
            if keys_pressed[pygame.K_UP] and red.y - VEL > 0:
                red.y -= VEL
            if keys_pressed[pygame.K_DOWN] and red.y - VEL < HEIGHT - 58:
                red.y += VEL

        def handle_bullets(yellow_bullets, red_bullets, yellow, red):
            for bullet in yellow_bullets:
                bullet.x += BULLET_VEL
                if red.colliderect(bullet):
                    pygame.event.post(pygame.event.Event(RED_HIT))
                    yellow_bullets.remove(bullet)
                elif bullet.x > WIDTH:
                    yellow_bullets.remove(bullet)
            for bullet in red_bullets:
                bullet.x -= BULLET_VEL
                if yellow.colliderect(bullet):
                    pygame.event.post(pygame.event.Event(YELLOW_HIT))
                    red_bullets.remove(bullet)
                elif bullet.x < 0:
                    red_bullets.remove(bullet)

        def main():
            red = pygame.Rect(700, 300, GUN_WIDTH, GUN_HEIGHT)
            yellow = pygame.Rect(100, 300, GUN_WIDTH, GUN_HEIGHT)
            red_bullets = []
            yellow_bullets = []
            red_health = 10
            yellow_health = 10

            clock = pygame.time.Clock()
            run = True
            while run:
                clock.tick(FPS)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                        pygame.quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETs:
                            bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height // 2 - 2, 10, 5)
                            yellow_bullets.append(bullet)

                        if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETs:
                            bullet = pygame.Rect(red.x, red.y + red.height // 2 - 2, 10, 5)
                            red_bullets.append(bullet)
                    if event.type == RED_HIT:
                        red_health -= 1

                    if event.type == YELLOW_HIT:
                        yellow_health -= 1
                winner_text = ""
                if red_health <= 0:
                    winner_text = e.get() + ' WINS'
                    st=f"insert into game values('{e.get()}','{e1.get()}','{e.get()}','{red_health-yellow_health}')"
                    cur.execute(st)
                    db.commit()

                if yellow_health <= 0:
                    winner_text = e1.get() + ' WINS'
                    st=f"insert into game values('{e.get()}','{e1.get()}','{e1.get()}','{-red_health+yellow_health}')"
                    cur.execute(st)
                    db.commit()

                if winner_text != "":
                    draw_winner(winner_text)
                    break

                keys_pressed = pygame.key.get_pressed()
                yellow_movement(keys_pressed, yellow)
                red_movement(keys_pressed, red)
                handle_bullets(yellow_bullets, red_bullets, yellow, red)
                draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health)
            main()

        if __name__ == "__main__":
            main()
    except pygame.error:
        pass

def popup():

    response = messagebox.askquestion('Sub Menu', 'Enter Gaming World???')
    if response=='no':
        root.quit()
    else:
        mass()
def game_quit():
    root.quit()
def fig1():
    my_img = ImageTk.PhotoImage(Image.open('mus1.png'))
    mylabel = Label(mus, image=my_img)
    mylabel.pack()
def custom():
    global a
    global cus
    cus=Toplevel()
    cus.resizable(False,False)
    appwidth = 500
    appheight = 360
    cus.config(bg='gray')
    original_width = cus.winfo_screenwidth()
    original_height = cus.winfo_screenheight()
    cus.geometry(f'{appwidth}x{appheight}+{int(original_width / 2) - int(appwidth / 2)}+{int(original_height / 2) - int(appheight / 2)}')
    cus.title("Custom Setting#")
    cus.iconbitmap('kkdjjj.ico')
    Label(cus,text="Speed",fg='black',bg='grey').grid(row=0,column=0)
    speed=Entry(cus,width=50,borderwidth=5)
    speed.grid(row=0,column=1)
    a=speed.get()
    Button(cus,text='Submit',command=append).grid(row=1)
    

    cus.mainloop()



def music():
    global mus
    mus=Toplevel()
    mus.resizable(False, False)
    appwidth = 255
    appheight = 360
    mus.config(bg='black')
    original_width = mus.winfo_screenwidth()
    original_height = mus.winfo_screenheight()
    mus.geometry(f'{appwidth}x{appheight}+{int(original_width / 2) - int(appwidth / 2)}+{int(original_height / 2) - int(appheight / 2)}')
    mus.title("Music!!!")
    mus.iconbitmap('mus1.ico')
    my_img = ImageTk.PhotoImage(Image.open('mus1.png'))
    mylabel = Label(mus, image=my_img)
    mylabel.pack()
    btn_mus1=Button(mus,text="Music_1: Beats",bg='red',padx=25,command=music1,height=1, width=14, bd=6)
    btn_mus1.pack()
    Button(mus,text='Music_2: Sike',bg='red',command=music2,padx=29, height=1, width=13, bd=6).pack()
    Button(mus,text='Music_3: Chill',bg='red',command=music3,padx=29,height=1, width=13, bd=6).pack()
    Button(mus,text='Music_4: Dreamz',bg='red',command=music4,padx=29,height=1, width=13, bd=6).pack()
    Label(mus,text='Music By: DanvanthramKK',bg='red',font='arial').pack()
    fig1()
    mus.mainloop()
def music1():
    mixer.music.load('App1.wav')
    mixer.music.play(-1)
def music2():
    mixer.music.load('App2.wav')
    mixer.music.play(-1)
def music3():
    mixer.music.load('App3.wav')
    mixer.music.play(-1)
def music4():
    mixer.music.load('App4.wav')
    mixer.music.play(-1)
def crazy():
    engine = pyttsx3.init()
    engine.say('Welcome To K K D Gaming')
    engine.runAndWait()
def main_rootk():
    crazy()
    global root
    global e
    global e1
    root=Tk()
    root.title('Main Menu')
    appwidth=900
    appheight=400
    root.config(bg='grey')
    original_width=root.winfo_screenwidth()
    original_height=root.winfo_screenheight()
    root.geometry(f'{appwidth}x{appheight}+{int(original_width/2)-int(appwidth/2)}+{int(original_height/2)-int(appheight/2)}')
    root.iconbitmap('kkdjjj.ico')
    Label(root,text='Welcome To KKD Gaming',bg='grey',font=('algerian',20)).grid(row=0,column=1,columnspan=3)
    Label(root,text='Enter Name of Player 1',bg='grey').grid(row=1)
    e=Entry(root,width=50,borderwidth=5)
    e.grid(row=1,column=1)
    Label(root,text='Enter Name of Player 2',bg='grey').grid(row=2)
    e1=Entry(root,width=50,borderwidth=5)
    e1.grid(row=2,column=1)
    btn=Button(root,text='Submit',command=prt,padx=20,fg='red',bg='black',height=1, width=15, bd=6)
    btn.grid(row=3,column=1)
    btn1 = Button(root, text='Do you want to play', command=popup, padx=40,fg='red',bg='black',height=1, width=13, bd=6)
    btn1.grid(row=5, column=1)
    btn_quit=Button(root,text="Quit Game",padx=35,command=game_quit,fg='red',bg='black',height=1, width=13, bd=6)
    btn_quit.grid(row=6,column=1)
    l1=Label(root,padx=50,font='arial',bg='grey')
    l1.grid(row=1,column=7,rowspan=2)
    btn_music=Button(root,text='Hear Custom Music',command=music,padx=40,fg='red',bg='black',height=1, width=13, bd=6)
    btn_music.grid(row=10,column=1)
    root.mainloop()
ak=10
def Ok():
    name=[]
    pcode=[]
    uname=entry1.get()
    password=entry2.get()
    cur.execute('select name from user')
    getname=cur.fetchall()
    for i in getname:
        for j in i:
            name.append(j)
    cur.execute('select passwd from user')
    getpc=cur.fetchall()
    for i in getpc:
        for j in i:
            pcode.append(j)
    if uname in name:
        for i in name:
            if i==uname:
                ind=name.index(i)
                if password==pcode[ind]:
                    log.destroy()
                    main_rootk()
                elif password!=pcode[ind]:
                    messagebox.showinfo('','Incorrect password')
    elif uname=='' or password=='':
        messagebox.showinfo('','Blank not allowed')
    else:
        messagebox.showinfo('','Incorrect user name')
def create():
    global entry11
    global entry21
    global sign
    sign=Tk()
    sign.title('Sign In')
    sign.iconbitmap('kkdjjj.ico')
    Label(sign, text='Username').place(x=20, y=20)
    Label(sign, text='Password').place(x=20, y=70)
    sign.geometry('300x200')
    entry11=Entry(sign,bd=5)
    entry11.place(x=140,y=20)
    entry21=Entry(sign,bd=5)
    entry21.place(x=140,y=70)
    entry21.config(show='*')
    Button(sign, text='Register', command=adding).place(x=200,y=100)
    sign.mainloop()
                    
def adding():
    st=f"insert into user values('{entry11.get()}','{entry21.get()}')"
    cur.execute(st) 
    db.commit()
    sign.destroy()
    log.destroy()
    start()
def change():
    global chan
    global entry12
    global entry22
    chan=Tk()
    chan.geometry('300x200')
    chan.title('Change Password')
    chan.iconbitmap('kkdjjj.ico')
    Label(chan, text='Username').place(x=20, y=20)
    Label(chan, text='New Password').place(x=20, y=70)
    entry12=Entry(chan,bd=5)
    entry12.place(x=140,y=20)
    entry22=Entry(chan,bd=5)
    entry22.place(x=140,y=70)
    entry22.config(show='*')
    Button(chan,text='Update Password',command=update_pas).place(x=10,y=100)
    chan.mainloop()
def update_pas():
    st=f"update user set passwd='{entry22.get()}' where name='{entry12.get()}'"
    cur.execute(st)
    db.commit()
    chan.destroy()
    log.destroy()
    start()
def delete_user():
    global du
    du=Tk()
    global entry4
    global entry5
    du.geometry('300x200')
    du.title('Delete User')
    du.iconbitmap('kkdjjj.ico')
    Label(du, text='Username').place(x=20, y=20)
    Label(du, text='Password').place(x=20, y=70)
    entry4=Entry(du,bd=5)
    entry4.place(x=140,y=20)
    entry5=Entry(du,bd=5)
    entry5.place(x=140,y=70)
    entry5.config(show='*')
    Button(du,text='Delete Use',command=del_user).place(x=10,y=100)
    du.mainloop()
def del_user():
    name=[]
    pcode=[]
    uname=entry4.get()
    password=entry5.get()
    cur.execute('select name from user')
    getname=cur.fetchall()
    for i in getname:
        for j in i:
            name.append(j)
    cur.execute('select passwd from user')
    getpc=cur.fetchall()
    for i in getpc:
        for j in i:
            pcode.append(j)
    if uname in name:
        for i in name:
            if i==uname:
                ind=name.index(i)
                if password==pcode[ind]:
                    st=f"delete from user where name='{uname}'"
                    cur.execute(st)
                    db.commit()
                    du.destroy()
                    log.destroy()
                    start()
                elif password!=pcode[ind]:
                    messagebox.showinfo('','Incorrect password')
    elif uname=='' or password=='':
        messagebox.showinfo('','Blank not allowed')
    else:
        messagebox.showinfo('','Incorrect user name')
    
def stats():
    log.destroy()
    s='yes'
    while s=='yes':
        print('1.search by player')
        print('2.Most Wins by a player')
        print('3.Display every game')
        ch=int(input('enter your choice:'))
        al=[]
        if ch==1:
            ename=input('Enter player name:')
            st=f"select * from game where red_player='{ename}' or yellow_player='{ename}'"
            cur.execute(st)
            data=cur.fetchall()
            for i in data:
                for j in i:
                    al.append(j)
            if ename in al:
                pass
            else:
                print('No user found')
                continue
            
            print('\n')
            print('red_player','  yellow_player','  winner  ','point_difference',end='      ')
            print('\n')
            for i in data:
                for j in i:
                    print(j,end='      ')
                print('\n')
        elif ch==2:
            store=[]
            cur.execute('select winner from game')
            data=cur.fetchall()
            for i in data:
                for j in i:
                    store.append(j)
            
            index=0
            max=0
            for i in store:
                count=store.count(i)
                if count>max:
                    max=count
                    index=store.index(i)
            print(store[index],'has most wins with',max)
                    
        elif ch==3:
            cur.execute('select * from game')
            data=cur.fetchall()
            print('\n')
            print('red_player','  yellow_player','  winner  ','point_difference',end='      ')
            print('\n')
            for i in data:
                for j in i:
                    print(j,end='      ')
                print('\n')
            
            
        else:
            print('invalid choice')
        s=input('Enter do you want to continue')
    start()
def user_pas():
    cur.execute('select * from user')
    data=cur.fetchall()
    a='*'
    print(a*80)
    print('User Name','     Password',end="  ")
    print('\n')
    for i in data:
        for j in i:
            print(j,end='       ')
        print('\n')
    start()  
def adminok():
    name=[]
    pcode=[]
    uname=entry8.get()
    password=entry9.get()
    cur.execute('select name from admin')
    getname=cur.fetchall()
    for i in getname:
        for j in i:
            name.append(j)
    cur.execute('select passwd from admin')
    getpc=cur.fetchall()
    for i in getpc:
        for j in i:
            pcode.append(j)
    if uname in name:
        for i in name:
            if i==uname:
                ind=name.index(i)
                if password==pcode[ind]:
                    show.destroy()
                    user_pas()
                elif password!=pcode[ind]:
                    messagebox.showinfo('','Incorrect Admin password')
    elif uname=='' or password=='':
        messagebox.showinfo('','Blank not allowed')
    else:
        messagebox.showinfo('','Incorrect Admin user name')
def show_pas():
    global show
    log.destroy()
    show=Tk()
    show.title('Admin Login')
    show.iconbitmap('kkdjjj.ico')
    show.geometry('500x200')


    global entry8
    global entry9

    Label(show, text='Admin Username').place(x=20, y=20)
    Label(show, text='Admin Password').place(x=20, y=70)

    entry8=Entry(show,bd=5, width=50)
    entry8.place(x=140,y=20)

    entry9=Entry(show,bd=5, width=50)
    entry9.place(x=140,y=70)
    entry9.config(show='*')
    Button(show,text='Admin sign in',command=adminok,height=3,width=13,bd=6).place(x=10,y=115)
    show.mainloop()
            
            
def start():
    
    global log
    log=Tk()
    log.title('Login')
    log.iconbitmap('kkdjjj.ico')
    log.geometry('500x300')


    global entry1
    global entry2

    Label(log, text='Username').place(x=20, y=20)
    Label(log, text='Password').place(x=20, y=70)

    entry1=Entry(log,bd=5, width=50)
    entry1.place(x=140,y=20)

    entry2=Entry(log,bd=5, width=50)
    entry2.place(x=140,y=70)
    entry2.config(show='*')
    Button(log, text='Admin Log In',command=show_pas, height=3, width=13, bd=6).place(x=290,y=180)
    Button(log, text='Stats', command=stats, height=3, width=13, bd=6).place(x=290,y=115)
    Button(log, text='Delete user', command=delete_user,height=3, width=13, bd=6).place(x=10,y=180)
    Button(log, text='change password',command=change,height=3, width=13, bd=6).place(x=150,y=115)
    Button(log, text='Login', command=Ok, height=3, width=13, bd=6).place(x=10, y=115)
    Button(log, text='   Sign Up    ', command=create,height=3, width=13, bd=6).place(x=150,y=180)
    log.mainloop()
start()




