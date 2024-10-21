import pygame,sys
import time
import random

pygame.init()
pygame.mixer.init()
gray = (137, 136, 140)      #RGB
black = (0,0,0)
red = (255,0,0)
green = (0,200,0)
blue = (0,0,200)
bright_red = (255,0,0)
bright_green = (0,255,0)
bright_blue = (0,0,255)
pause = False

# 背景圖片大小
display_width = 800
display_height = 600

# 背景音樂
pygame.time.delay(1000)
pygame.mixer.music.load("b-music.mp3")
pygame.mixer.music.play(-1)     # 無限循環

gamedisplayS = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("頭文字B")
clock = pygame.time.Clock()
carimg = pygame.image.load("car.png")
backgroundpic = pygame.image.load("download12.jpg")
yellow_strip = pygame.image.load("yellow strip.png")
strip = pygame.image.load("strip.jpg")
intro_background = pygame.image.load("background.jpg")
instruction_background = pygame.image.load("background2.jpg")
car_width = 51

# 遊戲首頁
def intro_loop():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
    
        gamedisplayS.blit(intro_background,(0,0))
        largetext = pygame.font.Font("Fonts/mingliu.ttf",115)
        largetext.set_bold(True)
        TextSurf,TextRect = text_object("頭 文 字 B",largetext)
        TextRect.center = (400,100)
        gamedisplayS.blit(TextSurf,TextRect)
        button("START",150,520,100,50,green,bright_green,"play")
        button("QUIT",550,520,100,50,red,bright_red,"quit")
        button("INSTRUCTION",300,520,200,50,blue,bright_blue,"intro")
        pygame.display.update()
        clock.tick(60)

# 按鈕
def button(msg,x,y,w,h,ic,ac,action=None):      # ac:action , ic:inaction
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global pause

    # 按下按鈕時觸發操作
    if x+w>mouse[0]>x and y+h>mouse[1] > y:
        pygame.draw.rect(gamedisplayS,ac,(x,y,w,h))
        if click[0] == 1 and action!=None:
            if action == "play":
                countdown()
            elif action == "quit":
                pygame.quit()
                quit()
                sys.exit()
            elif action == "intro":
                introduction()
            elif action == "menu":
                intro_loop()
            elif action == "pause":
                pause = True
                paused()
            elif action == "unpause":
                pause = False
                unpaused()
    else:
        pygame.draw.rect(gamedisplayS,ic,(x,y,w,h))

    # 按鈕上的字
    smalltext = pygame.font.Font("freesansbold.ttf",20)
    textsurf,textrect = text_object(msg,smalltext)
    textrect.center = ((x+(w/2)),(y+(h/2)))
    gamedisplayS.blit(textsurf,textrect)

# 計時開始
def countdown():
    countdown = True
    while countdown:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        for num in range(3,0,-1):
            gamedisplayS.fill(gray)
            background()
            largetext = pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect=text_object(str(num),largetext)
            TextRect.center = ((display_width/2),(display_height/2))
            gamedisplayS.blit(TextSurf,TextRect)
            pygame.display.update()
            clock.tick(1)
        game_loop()

# 按暫停
def paused():
    global pause
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        gamedisplayS.blit(instruction_background,(0,0))
        largetext = pygame.font.Font("Fonts/mingliu.ttf",115)
        largetext.set_bold(True)
        TextSurf,TextRect = text_object("暫停",largetext)
        TextRect.center = ((display_width/2),(display_height/2))
        gamedisplayS.blit(TextSurf,TextRect)
        button("CONTINUE",100,450,150,50,green,bright_green,"unpause")
        button("RESTART",300,450,150,50,blue,bright_blue,"play")
        button("MAIN MENU",500,450,200,50,red,bright_red,"menu")
        pygame.display.update()
        clock.tick(60)


# 沒按暫停
def unpaused():
    pass

# 介紹
def introduction():
    introduction = True
    while introduction:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        gamedisplayS.blit(instruction_background,(0,0))
        largetext = pygame.font.Font("freesansbold.ttf",80)
        smalltext = pygame.font.Font("Fonts/mingliu.ttf",40)
        mediumtext = pygame.font.Font("freesansbold.ttf",60)
        chinesetext = pygame.font.Font("Fonts/mingliu.ttf",30)
        textSurf,textRect = text_object("躲避車輛以獲得分數，難度將隨等級上升而增加 !",chinesetext)
        textRect.center = ((400),(175))
        TextSurf,TextRect = text_object("INSTRUCTION",largetext)
        TextRect.center = ((400),(100))
        gamedisplayS.blit(TextSurf,TextRect)
        gamedisplayS.blit(textSurf,textRect)
        stextSurf,stextRect = text_object("左鍵 : 左轉",smalltext)
        stextRect.center = ((150),(400))
        hTextSurf,hTextRect = text_object("右鍵 : 右轉" ,smalltext)
        hTextRect.center = ((150),(450))
        atextSurf,atextRect = text_object("A : 加速",smalltext)
        atextRect.center = ((150),(500))
        rtextSurf,rtextRect = text_object("B : 結束遊戲 ",smalltext)
        rtextRect.center = ((150),(550))
        ptextSurf,ptextRect = text_object("P : 暫停  ",smalltext)
        ptextRect.center = ((150),(350))
        sTextSurf,sTextRect = text_object("CONTROLS",mediumtext)
        sTextRect.center = ((200),(275))
        gamedisplayS.blit(sTextSurf,sTextRect)
        gamedisplayS.blit(stextSurf,stextRect)
        gamedisplayS.blit(hTextSurf,hTextRect)
        gamedisplayS.blit(atextSurf,atextRect)
        gamedisplayS.blit(rtextSurf,rtextRect)
        gamedisplayS.blit(ptextSurf,ptextRect)
        button("BACK",600,450,100,50,blue,bright_blue,"menu")
        pygame.display.update()
        clock.tick(60)

# 文字物件
def text_object(text,font):
    textsurface = font.render(text,True,black)
    return  textsurface,textsurface.get_rect()      # 渲染好的文字圖像 , 文字圖像的矩形邊界

# 結束訊息展示
def message_display(text):
    largetext = pygame.font.Font("freesansbold.ttf",80)
    textsurf,textrect = text_object(text,largetext)
    textrect.center = ((display_width/2),(display_height/2))
    gamedisplayS.blit(textsurf,textrect)
    pygame.display.update()
    time.sleep(3)

# 遊戲結束
def crash():
    message_display("GAME OVER")
    intro_loop()

# 主背景
def background():
    gamedisplayS.blit(backgroundpic,(0,0))
    gamedisplayS.blit(backgroundpic,(700,0))
    gamedisplayS.blit(yellow_strip,(380,0))
    gamedisplayS.blit(yellow_strip,(380,100))
    gamedisplayS.blit(yellow_strip,(380,200))
    gamedisplayS.blit(yellow_strip,(380,300))
    gamedisplayS.blit(yellow_strip,(380,400))
    gamedisplayS.blit(yellow_strip,(380,500))
    gamedisplayS.blit(strip,(120,0))
    gamedisplayS.blit(strip,(680,0))

# 玩家車子
def car(x,y):
    gamedisplayS.blit(carimg,(x,y))

# 障礙物(路上車輛)
def obstacle(obs_start_x,obs_start_y,obs):
    obs_pic = pygame.image.load(f"car{obs}.jpg")
    gamedisplayS.blit(obs_pic,(obs_start_x,obs_start_y))

# 記分板
def score_system(passed,score):
    font = pygame.font.SysFont(None,25)
    text = font.render(f"DODGED: {passed}",True,black)
    score = font.render(f"SCORE: {score}",True,red)
    gamedisplayS.blit(text,(0,50))
    gamedisplayS.blit(score,(0,30))

# 遊戲主循環
def game_loop():
    # 車子起始位置
    x = (display_width*0.475)
    y = (display_height*0.8)
    x_change = 0
    # 障礙物
    obstacle_speed = 9
    obs = 1
    obs_start_x = random.randrange(200,(display_width-200))
    obs_start_y = -750
    obs_width = 56
    obs_height = 125
    passed = 0
    level = 0
    score = 0
    y2 = 7

    bumped = False
    while not bumped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
            # 按鍵連動
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_a:
                    obstacle_speed += 2
                if event.key == pygame.K_b:
                    obstacle_speed -= 2
                if event.key == pygame.K_p:
                    global pause
                    pause = True
                    paused()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
        x+=x_change

        # 背景隨車輛移動(可改進)
        gamedisplayS.fill(gray)
        rel_y = y2%backgroundpic.get_rect().width
        gamedisplayS.blit(backgroundpic,(0,rel_y - y2%backgroundpic.get_rect().width))
        gamedisplayS.blit(backgroundpic,(700,rel_y - y2%backgroundpic.get_rect().width))
        if rel_y < 800:
            gamedisplayS.blit(backgroundpic,(0,rel_y))
            gamedisplayS.blit(backgroundpic,(700,rel_y))
            gamedisplayS.blit(yellow_strip,(380,rel_y))
            gamedisplayS.blit(yellow_strip,(380,rel_y + 100))
            gamedisplayS.blit(yellow_strip,(380,rel_y + 200))
            gamedisplayS.blit(yellow_strip,(380,rel_y + 300))
            gamedisplayS.blit(yellow_strip,(380,rel_y + 400))
            gamedisplayS.blit(yellow_strip,(380,rel_y + 500))
            gamedisplayS.blit(yellow_strip,(380,rel_y - 100))
            gamedisplayS.blit(strip,(120,rel_y - 200))
            gamedisplayS.blit(strip,(120,rel_y + 20))
            gamedisplayS.blit(strip,(120,rel_y + 30))
            gamedisplayS.blit(strip,(680,rel_y - 100))
            gamedisplayS.blit(strip,(680,rel_y + 20))
            gamedisplayS.blit(strip,(680,rel_y + 30))
        y2 += obstacle_speed

        # 障礙物邏輯
        obs_start_y -= (obstacle_speed/4)
        obstacle(obs_start_x,obs_start_y,obs)
        obs_start_y += obstacle_speed

        # 呼叫玩家車和記分板
        car(x,y)
        score_system(passed,score)

        # 暫停按鈕
        button("Pause",650,0,150,50,blue,bright_blue,"pause")
        pygame.display.update()
        clock.tick(60)

        # 碰撞邏輯
        if x > display_width - (car_width + 110) or x < 110:
            crash()
            bumped = True
        
        if y < obs_start_y + obs_height:
            if x > obs_start_x and x < obs_start_x + obs_width or x + car_width > obs_start_x and x + car_width < obs_start_x + obs_width:
                crash()
                bumped = True

        if bumped == True:  # 如果發生碰撞
            break  # 結束遊戲循環

        # 障礙物的重生位置；更新得分；提升等級跟難度   
        if obs_start_y > display_height:
            obs_start_y = 0-obs_height
            obs_start_x = random.randrange(170,(display_width-170))
            obs = random.randrange(1,7)
            passed += 1
            score = passed*10
            if int(passed)%10 == 0:
                level += 1
                obstacle_speed += 2
                largetext=pygame.font.Font("freesansbold.ttf",80)
                textsurf,textrect=text_object(f"LEVEL{level}",largetext)
                textrect.center=((display_width/2),(display_height/2))
                gamedisplayS.blit(textsurf,textrect)
                pygame.display.update()
                time.sleep(3)
        
intro_loop()