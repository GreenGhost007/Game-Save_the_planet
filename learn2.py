import pygame
import csv
screen_size=[1040,616]
screen = pygame.display.set_mode(screen_size)
backg = pygame.image.load('background.png')
planet = pygame.image.load('p_one.png')
dirt = None
P_x=450
P_y=250
move = False
keep_alive = True
clock = pygame.time.Clock()
score=0
fr_rate=200
d_lvl=20
file = open('score.txt',mode='a')
writer=csv.writer(file,delimiter=',',quotechar='"')
while keep_alive:
    screen.blit(backg,[0,0])
    screen.blit(planet,[P_x,P_y])
    pygame.event.get()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_t]:
        move=True
    elif keys[pygame.K_q]:
        print(P_x,P_y,sep=' ')
        print(score/100)
        raise SystemExit
    elif keys[pygame.K_r]:
        score=0
        P_x=450
        P_y=250
        dirt=None
    if move:
        if keys[pygame.K_t]:
            move=True
        if keys[pygame.K_w]:
            dirt = 'up'
        elif keys[pygame.K_a]:
            dirt = 'left'
        elif keys[pygame.K_s]:
            dirt = 'down'
        elif keys[pygame.K_d]:
            dirt = 'right'
        elif keys[pygame.K_UP]:
            d_lvl+=2
            #print('UP',d_lvl,sep=' ')
        elif keys[pygame.K_r]:
            score=0
            P_x=450
            P_y=250
            dirt=None
            move =False
        elif keys[pygame.K_DOWN]:
            d_lvl-=5
            if d_lvl<1:
                d_lvl=1
            #print('DOWN',d_lvl,sep=' ')
        elif keys[pygame.K_LEFT]:
            fr_rate-=50
            #print('LEFT',fr_rate,sep=' ')
            if fr_rate<2:
                fr_rate=2
        elif keys[pygame.K_RIGHT]:
            fr_rate+=50
            #print('RIGHT',fr_rate,sep=' ')
        elif keys[pygame.K_f]:
            move =False
            P_x=350
            P_y=450
            continue
        if dirt == 'up':
            P_y-=(d_lvl+10)
            score+=2+d_lvl
        if dirt == 'down':
            P_y+=(d_lvl+10)
            score+=2+d_lvl
        if dirt == 'left':
            P_x-=d_lvl
            score+=1+d_lvl
        if dirt == 'right':
            P_x+=d_lvl
            score+=1+d_lvl

        if P_x>904 or P_y>492 or P_x<=0 or P_y<=0:
            print('Game Over')
            print('Score : '+str(score/100))
            writer.writerow([score/100,d_lvl,fr_rate,P_x,P_y])
            #file.write(str([score,d_lvl,fr_rate]))
            file.flush()
            score=0
            #P_x=350
            #P_y=450
            dirt=None
            move =False
    
    pygame.display.update()
    pygame.display.flip()
    clock.tick(fr_rate)
