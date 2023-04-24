import pygame as pg 
import random as rr 
from sys import exit
from time import sleep

#varijable i ostale bitne stvari
screen = pg.display.set_mode((1200,600))
clock = pg.time.Clock()
bird_pos = (80,300)
game_state = False
gravity = 0
balloon_speed = 2



#inicijacija i loadanje asserta
pg.init()
pg.display.set_caption("Flappy Birb")
#pozadina             
sky = pg.image.load(r"C:\Users\Korisnik\Desktop\RealStart\Programiranje\Python programi\FlappyBirb\sky.png")
sky = pg.transform.scale(sky,(1200,600))
sky_box= sky.get_rect(topleft= (0,0))
#pticica 
birb = pg.image.load(r"C:\Users\Korisnik\Desktop\RealStart\Programiranje\Python programi\FlappyBirb\bird.png")
birb = pg.transform.scale(birb,(50,50))
birb_box= birb.get_rect(center= (100,300))
#prepreke
balloon1 = pg.image.load(r"C:\Users\Korisnik\Desktop\RealStart\Programiranje\Python programi\FlappyBirb\Balloon.jfif")
balloon1 = pg.transform.scale(balloon1,(70,70))
balloon_box1 = balloon1.get_rect(center= (800,100))

balloon2 = pg.image.load(r"C:\Users\Korisnik\Desktop\RealStart\Programiranje\Python programi\FlappyBirb\Balloon.jfif")
balloon2 = pg.transform.scale(balloon2,(70,70))
balloon_box2 = balloon2.get_rect(center= (550,200))

balloon3 = pg.image.load(r"C:\Users\Korisnik\Desktop\RealStart\Programiranje\Python programi\FlappyBirb\Balloon.jfif")
balloon3 = pg.transform.scale(balloon3,(70,70))
balloon_box3 = balloon3.get_rect(center= (100,300))

balloon4 = pg.image.load(r"C:\Users\Korisnik\Desktop\RealStart\Programiranje\Python programi\FlappyBirb\Balloon.jfif")
balloon4 = pg.transform.scale(balloon4,(70,70))
balloon_box4 = balloon4.get_rect(center= (700,500))
#play
play = pg.image.load(r"C:\Users\Korisnik\Desktop\RealStart\Programiranje\Python programi\FlappyBirb\play.png")
play  = pg.transform.scale(play,(200,100))
play_box = play.get_rect(center= (600,340))
#text
text = pg.font.Font(None,70)
shade = pg.font.Font(None,70)
text = text.render("Flappybirb",False,(200,100,100))
shade = shade.render("Flappybirb",False,(50,50,50))
#tutorial 
tutor = pg.font.Font(None,30)
tutor = tutor.render("Press spacebar to play!", False, (50,150,50))
#score 
score = pg.font.Font(None,30)
score = score.render("Your score: ", False, (50,150,50))
#num = pg.font.Font(None,30)
#num = num.render(str(balloon_speed-3), False, (50,150,50))
#gameover
#over =pg.font.Font(None,50)
#over = over.render("Game Over!", False, (250,50,50))



#game loop
while True: 
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit

    #pakiranje i crtanje stvari
    
    screen.blit(sky,sky_box)


    if game_state: 
        screen.blit(birb,birb_box)
        screen.blit(balloon1,balloon_box1)
        screen.blit(balloon2,balloon_box2)
        screen.blit(balloon3,balloon_box3)
        screen.blit(balloon4,balloon_box4)

        if balloon_box1.right >= 0:
            balloon_box1.left -= balloon_speed
        else: 
            balloon_box1.left = 1200
            
            balloon_box1.top =rr.randint(50,500)

        if balloon_box2.right >= 0:
            balloon_box2.left -= balloon_speed
        else: 
            balloon_box2.left = 1200
            balloon_speed +=1 
            balloon_box2.top =rr.randint(50,500)

        if balloon_box3.right >= 0:
            balloon_box3.left -= balloon_speed
        else: 
            balloon_box3.left = 1200

            balloon_box3.top =rr.randint(50,500)

        if balloon_box4.right >= 0:
            balloon_box4.left -= balloon_speed
        else: 
            balloon_box4.left = 1200
            balloon_speed +=1 
            balloon_box4.top =rr.randint(50,500)

        keys = pg.key.get_pressed()
        if keys[pg.K_SPACE]:
            gravity = -10
            birb_box.bottom += gravity
        else:
            gravity +=1 
            birb_box.bottom += gravity

        if birb_box.bottom <= 0:
            game_state = False
            over =pg.font.Font(None,50)
            over = over.render("Game Over!", False, (250,50,50))
            screen.blit(over,(500,200))
            sleep(1)
        
        elif birb_box.top >= 600:
            game_state = False
            over =pg.font.Font(None,50)
            over = over.render("Game Over!", False, (250,50,50))
            screen.blit(over,(500,200))
            sleep(1)

        elif birb_box.colliderect(balloon_box1):
            game_state = False
            over =pg.font.Font(None,50)
            over = over.render("Game Over!", False, (250,50,50))
            screen.blit(over,(500,200))
            sleep(1)

        elif birb_box.colliderect(balloon_box2):
            game_state = False
            over =pg.font.Font(None,50)
            over = over.render("Game Over!", False, (250,50,50))
            screen.blit(over,(500,200))
            sleep(1)

        elif birb_box.colliderect(balloon_box3):
            game_state = False
            over =pg.font.Font(None,50)
            over = over.render("Game Over!", False, (250,50,50))
            screen.blit(over,(500,200))
            sleep(1)
        
        elif birb_box.colliderect(balloon_box4):
            game_state = False
            over =pg.font.Font(None,50)
            over = over.render("Game Over!", False, (250,50,50))
            screen.blit(over,(500,200))
            sleep(1)
    else:
         
        screen.blit(play, play_box)
        screen.blit(shade,(472,202))
        screen.blit(text,(470,200))
        screen.blit(tutor,(485,255))
        screen.blit(score,(20,20))
        num = pg.font.Font(None,30)
        num = num.render(str(balloon_speed-2), False, (50,150,50))
        screen.blit(num,(140,20))
        
    
        
        keys = pg.key.get_pressed()
        if keys[pg.K_SPACE]:
                game_state = True 
                birb_box.center = (100,300)
                balloon_box1.center = (200,100)
                balloon_box2.center = (500,200)
                balloon_box3.center = (700,400)
                balloon_box4.center = (1100,300)
                balloon_speed = 6
                



    pg.display.update()


    clock.tick(60)