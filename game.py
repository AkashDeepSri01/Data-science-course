import pgzrun
from random import randint

HEIGHT=700
WIDTH=1200
w,h=WIDTH,HEIGHT

music.play('remix')

p=Actor('ironman',(600,350))
e=Actor('alien',(w//2,200))
c=Actor('coin',(w//2,h-100))
score=0 # (global variable)
game_state=0
def draw():
  if game_state==0:
    screen.fill('white')
    p.draw()
    e.draw()
    c.draw()
    screen.draw.text(f'score:{score}',(10,10),color='black')
  elif game_state==1:
      screen.draw.text(f'Game Over',(w//2,h//2)color='red')

  elif game_state==2:
      screen.draw.text(f'You Win',(w//2,h//2),color='green')    
def player_update():
    if keyboard.left:
        p.x-=5
    elif keyboard.right:
        p.x += 5
    elif keyboard.up:
        p.y -= 5
    elif keyboard.down:
        p.y += 5


def enemy_update():
    
    if c.x > e.x:
        e.x += 3
    if c.x < e.x:
        e.x -= 3   
    if c.y > e.x:
        e.y += 3
    if c.y < e.x:
        e.y -= 3        

def score_update():
    global score
    if p.colliderect(c):
        score+=10
        c.x=randint(0,w)
        c.y=randint(0,h)      
        sounds.action.play()  
    if e.colliderect(c):
        score-=10
        c.x=randint(0,w)
        c.y=randint(0,h)      
        sounds.action.play()  

def update():
    enemy_update()    
    player_update()
    score_update()


pgzrun.go()