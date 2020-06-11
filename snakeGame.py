import pygame
import random
import os

pygame.mixer.init()
pygame.init()

white=(255,255,255)
red=(255,0,0)
black=(0,0,0)

screen_width=1000
screen_height=700

#creating window
gameWindow=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Snakes By ADITYA")
pygame.display.update()     #this function must be called everytime we change display stuff

bimg=pygame.image.load("bckgrnd.jpg")
bimg=pygame.transform.scale(bimg,(screen_width,screen_height)).convert_alpha()

font=pygame.font.SysFont(None,55)
clock = pygame.time.Clock()




#None arg refers to take default system font and 55 is font_size
def plot_snake(gameWindow,color,snk_list,snake_size):
    #print(snk_list)
    for x,y in snk_list:
        pygame.draw.rect(gameWindow,color,[x,y,snake_size,snake_size])

def text_screen(text,color,x,y):
    screen_text=font.render(text,True,color)
    #font.render(text_to_be_displayed,Antialiasing_indicator,text_color
    #Anti-aliasing --> TO show high resolution img into low resolution
    gameWindow.blit(screen_text,[x,y])

def welcome():
    exit_game=False
    while not exit_game:
        gameWindow.fill(white)
        text_screen("Welcome To SNAKES",black,300,200)
        text_screen("Press Spacebar to Start", black, 280, 300)
        text_screen("By ADITYA",red,750,600)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit_game=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    exit_game=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    pygame.mixer.music.load('astronomia.mp3')
                    pygame.mixer.music.play(-1)
                    game_loop()
        pygame.display.update()
        clock.tick(60)

#game loop
def game_loop():
    # game specific var
    snk_list = []
    snk_len = 1
    exit_game = False
    game_over = False
    snake_x = 100
    snake_y = 200
    snake_size = 30
    fps = 30
    velocity_x = 0
    velocity_y = 0
    init_velocity = 7
    food_x = random.randint(20, screen_width / 2)
    food_y = random.randint(20, screen_height / 2)
    score = 0
    if (not os.path.exists("highscore.txt")):
        with open("highscore.txt","w") as f:
            f.write("0")
    with open("highscore.txt", "r") as f:
        high_score = f.read()
        #print(high_score)
    while not exit_game:
        if game_over:
            if(score>int(high_score)):
                high_score=score    #if score is greater than high_score
            gameWindow.fill(white)
            with open("highscore.txt", "w") as f:
                f.write(str(high_score))
            text_screen("Game Over.", red, 100, 200)
            text_screen("Press Enter to Continue.", red, 100, 300)
            for event in pygame.event.get():
                if(event.type==pygame.QUIT):
                    exit_game=True
                if(event.type==pygame.KEYDOWN):
                    if(event.key==pygame.K_RETURN):
                        welcome()
        else:
            for event in pygame.event.get():
                #print(event) prints events like moving mouse ptr and pressed key events.
                if(event.type==pygame.QUIT):
                    exit_game=True
                if(event.type==pygame.KEYDOWN):
                    if(event.key==pygame.K_RIGHT):
                        velocity_x=init_velocity
                        velocity_y=0
                    if(event.key==pygame.K_LEFT):
                        velocity_x=-init_velocity
                        velocity_y=0
                    if(event.key==pygame.K_UP):
                        velocity_y=-init_velocity
                        velocity_x=0
                    if(event.key==pygame.K_DOWN):
                        velocity_y=init_velocity
                        velocity_x=0
            if(abs(snake_x-food_x)<14and abs(snake_y-food_y)<14):
                #print(snake_x," ",food_x," ",snake_y," ",food_y)
                score+=1
                snk_len+=5
                #print("Score: ",score)
                #text_screen("Score: "+str(score),red,5,5)
                food_x=random.randint(20,screen_width/2)
                food_y = random.randint(20, screen_height / 2)
            if(snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height):
                game_over=True
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play()
                #print("Game Over")
            snake_x+=velocity_x
            snake_y+=velocity_y

            gameWindow.fill(white)
            gameWindow.blit(bimg,(0,0))
            text_screen("Score: " + str(score), black, 5, 5)
            text_screen("High Score: " + str(high_score), black, 200, 5)
            pygame.draw.rect(gameWindow,red,[food_x,food_y,snake_size,snake_size])
            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)
            if(len(snk_list)>snk_len):
                del snk_list[0]
            if head in snk_list[:-1]:
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play()
                #print(head)
                #print(snk_list)
                game_over=True
            #rect(gameWindowSURFACE,ColorCo-ordinates,[x-coordinate,y-coordinate,width,height]
            plot_snake(gameWindow,black,snk_list,snake_size)
            clock.tick(fps)
        pygame.display.update()
    pygame.quit()
    quit()

welcome()