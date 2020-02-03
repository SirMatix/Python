import pygame as pg
import time
import random

pg.init()

crash_sound = pg.mixer.Sound("crash.wav")
pg.mixer.music.load("Canal_3.wav")



display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)


red = (200,0,0)
light_red = (255,0,0)
light_green = (0,255,0)
green = (0,200,0)


block_color = (23,255,55)

car_width = 77

gameDisplay = pg.display.set_mode((display_width,display_height))
pg.display.set_caption('a bit Racey')
clock = pg.time.Clock()

carImg = pg.image.load('racecar.png') # car image
carIcon = pg.image.load("racecar_icon.png") # program icon 32x32
pg.display.set_icon(carIcon) # setting the program icon

pause = False


def things_dodged(count):
    font = pg.font.SysFont(None, 25)
    text = font.render("Dodged: " + str(count), True, black)
    gameDisplay.blit(text,(0,0))

def things(thingx,thingy, thingw, thingh, color):
    pg.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])
    

def car(x,y):
    gameDisplay.blit(carImg,(x,y))

def text_objects(text,font):
    textSurface = font.render(text,True,black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pg.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)    
    pg.display.update()
    time.sleep(2)

    game_loop()

def quitgame():
    pg.quit()
    quit()

def crash():
    
    pg.mixer.music.stop()
    pg.mixer.Sound.play(crash_sound)
    
    #gameDisplay.fill(white)    # new screen like paused
    largeText = pg.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects("You Crashed", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()



        button("Play Again!",150,450,100,50,light_green,green,game_loop)
        button("Quit",550,450,100,50,light_red,red,quitgame)

        pg.display.update()
        clock.tick(15)
    



    

def button(msg,x,y,width,height,actCol,inaCol,action=None):
    mouse = pg.mouse.get_pos()
    click = pg.mouse.get_pressed()   

    if x+width > mouse[0] > x and y+height > mouse[1] > y:
        pg.draw.rect(gameDisplay, actCol, (x,y,width,height))
        
        if click[0] == 1 and action !=None:
            action()
##            if action == "play":
##                game_loop()
##            elif action == "quit":
##                pg.quit()
##                quit()
    else:
        pg.draw.rect(gameDisplay, inaCol, (x,y,width,height))

    smallText = pg.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(width/2)),(y+(height/2)) )
    gameDisplay.blit(textSurf, textRect)
        
def unpause():
    global pause
    pg.mixer.music.unpause()
    pause = False

def paused():
    pg.mixer.music.pause()
    
    #gameDisplay.fill(white)    # new screen like paused
    largeText = pg.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    while pause:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()



        button("Continue!",150,450,100,50,light_green,green,unpause)
        button("Quit",550,450,100,50,light_red,red,quitgame)

        pg.display.update()
        clock.tick(15)

def game_intro():
    intro = True
    while intro:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
        gameDisplay.fill(white)
        largeText = pg.font.Font('freesansbold.ttf',115)
        TextSurf, TextRect = text_objects("A bit Racey", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("GO!",150,450,100,50,light_green,green,game_loop)
        button("Quit",550,450,100,50,light_red,red,quitgame)

        pg.display.update()
        clock.tick(15)
    


def game_loop():
    global pause
    pg.mixer.music.play(-1)
    x = (display_width * 0.45)
    y = (display_height * 0.7)


    x_change = 0

    thing_startx = random.randrange(0,display_width)
    thing_starty = -600
    thing_speed = 4
    thing_width = 100
    thing_height = 100
     
    dodged = 0

    gameExit = False

    while not gameExit:

        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    x_change = -10
                if event.key == pg.K_RIGHT:
                    x_change = 10
                if event.key == pg.K_p:
                    pause = True
                    paused()

        

            if event.type == pg.KEYUP:
                if event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
                    x_change = 0

        x += x_change
        
        gameDisplay.fill(white)
    
        #things(thingx, thingy, thingw, thingh, color)
        things(thing_startx, thing_starty, thing_width, thing_height, block_color)
        thing_starty += thing_speed
        car(x,y)
        things_dodged(dodged)

        

        if x > display_width-car_width or x < 0:
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,display_width)
            dodged += 1
            thing_speed += 0.5
            thing_width += (dodged * 1.2)

        if y < thing_starty+thing_height:
            if x > thing_startx and x < thing_startx+ thing_width or x+car_width > thing_startx and x+car_width < thing_startx+thing_width:
                crash()
                
        pg.display.update()
        clock.tick(60) # in FPS


game_intro()
game_loop()
pg.quit()
quit()
    
 
