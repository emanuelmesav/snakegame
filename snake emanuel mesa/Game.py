


from cgi import test
from random import Random
from turtle import Screen, screensize, width
from food import Food
from snake import Snake
from player import player
import pygame
class Game: 
   
    def __init__(self):
        self.snake=Snake()
        self.food=Food()
        self.player=player()
        self.width=400
        self.heigth=400
        self.screen=pygame.display.set_mode(( self.width, self.heigth))
        self.clock=pygame.time.Clock()
        self.fps=60
    def checkKeys(self):
        keys=pygame.key.get_pressed() 
        if keys[pygame.K_q]: self.fps+=5
        elif keys[pygame.K_a]: self.fps-=5
        elif keys[pygame.K_UP]: self.snake.direction="UP"
        elif keys[pygame.K_DOWN]: self.snake.direction="DOWN"
        elif keys[pygame.K_RIGHT]: self.snake.direction="RIGTH"
        elif keys[pygame.K_LEFT]: self.snake.direction="LEFT"
        
    def checkEat(self):

        self.foodRect=pygame.Rect(self.food.x, self.food.y, self.food.size, self.food.size)
        self.snakeHeadRect=pygame.Rect(self.snake.body[0][0], self.snake.body[0][1], 10, 10)
        if pygame.Rect.colliderect(self.foodRect, self.snakeHeadRect):
            self.food.status = "inactive"
            self.snake.eat()
            self.player.score += 1
            print(self.player.name)
            print(self.player.score)
                     
    def run(self):
        
        pygame.init()
        
        while True:
            

            self.clock.tick(self.fps)
            #Revisar los eventos y mirar si oprimen el boton
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                 
            self.screen.fill((70,130,180))
            for celda in self.snake.body:
                   #Dibujar un rectangulo     
                 pygame.draw.rect(self.screen, self.snake.color, (celda[0], celda[1],10,10))
                  
            self.checkKeys()
            self.snake.move()
            
            if self.food.status=="inactive":
                x,y=self.food.putFood(x_max=390, y_max=390) 
                self.food.status="active"
            self.checkEat()    
                 
            pygame.draw.rect(self.screen, self.food.color, (x,y,10,10))
            
            if self.snake.body[0] in self.snake.body[1]:
                return False
                   
            if self.snake.body[0][0]>400 or self.snake.body[0][0]<0 or self.snake.body[0][1]>400 or self.snake.body[0][1]<0:
                return False    
            pygame.display.flip()
                  
            
mygame=Game()
mygame.run()
