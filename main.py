import pygame
import time
import random

pygame.init()
gray = (137, 136, 140)      #RGB
black = (0,0,0)
red = (255,0,0)

display_width = 800
display_height = 600

gamedisplayS = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("頭文字燒")
clock = pygame.time.Clock()
carimg = pygame.image.load("car.png")
backgroundpic = pygame.image.load("download12.jpg")
yellow_strip = pygame.image.load("yellow strip.png")
strip = pygame.image.load("strip.jpg")
intro_background = pygame.image.load("background.jpg")
instruction_background = pygame.image.load("background2.jpg")
car_width = 51


def text_object(text,font):
    textsurface = font.render(text,True,black)
    return  textsurface,textsurface.get_rect()


def message_display(text):
    largetext = pygame.font.Font("freesansbold.ttf",80)
    textsurf,textrect = text_object(text,largetext)
    textrect.center = ((display_width/2),(display_height/2))
    gamedisplayS.blit(textsurf,textrect)
    pygame.display.update()
    time.sleep(3)
    game_loop()


def crash():
    message_display("GAME OVER")


def background():
    gamedisplayS.blit(backgroundpic,(0,0))
    gamedisplayS.blit(backgroundpic,(700,0))
    gamedisplayS.blit(yellow_strip,(370,0))
    gamedisplayS.blit(yellow_strip,(370,100))
    gamedisplayS.blit(yellow_strip,(370,200))
    gamedisplayS.blit(yellow_strip,(370,300))
    gamedisplayS.blit(yellow_strip,(370,400))
    gamedisplayS.blit(yellow_strip,(370,500))
    gamedisplayS.blit(strip,(120,0))
    gamedisplayS.blit(strip,(680,0))


def car(x,y):
    gamedisplayS.blit(carimg,(x,y))

def obstacle(obs_start_x,obs_start_y,obs):
    obs_pic = pygame.image.load(f"car{obs}.jpg")
    gamedisplayS.blit(obs_pic,(obs_start_x,obs_start_y))


def score_system(passed,score):
    font = pygame.font.SysFont(None,25)
    text = font.render(f"Passed: {passed}",True,black)
    score = font.render(f"Score: {score}",True,red)
    gamedisplayS.blit(text,(0,50))
    gamedisplayS.blit(score,(0,30))

def game_loop():
    # 車子起始位置
    x = (display_width*0.4625)
    y = (display_height*0.8)
    x_change = 0
    # 障礙物
    obstacle_speed = 9
    obs = 1
    y_change = 0
    obs_start_x = random.randrange(200,(display_width-200))
    obs_start_y = -750
    obs_width = 56
    obs_height = 125
    passed = 0
    level = 0
    score = 0

    bumped = False
    while not bumped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            if event.key == pygame.K_RIGHT:
                x_change = 5
            if event.key == pygame.K_a:
                obstacle_speed += 2
            if event.key == pygame.K_b:
                obstacle_speed -= 2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
        x+=x_change

        gamedisplayS.fill(gray)
        background()
        obs_start_y -= (obstacle_speed/4)
        obstacle(obs_start_x,obs_start_y,obs)
        obs_start_y+=obstacle_speed
        car(x,y)
        score_system(passed,score)

        # if x>680-car_width or x<120:
        #     crash()

        if x>display_width-(car_width+120) or x<120:
            crash()
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


        if y<obs_start_y+obs_height:
            if x > obs_start_x and x < obs_start_x + obs_width or x+car_width > obs_start_x and x+car_width < obs_start_x+obs_width:
                crash()

        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()