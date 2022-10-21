
class Snake:
    
    def __init__(self):
        self.color=(124,252,0)
        self.direction="RIGTH"
        
        self.body=[(19,0),(18,0),(17,0),(16,0),(15,0),(14,0),(13,0),(12,0),(11,0),(10,0),(9,0),(8,0),(7,0),(6,0),(5,0),(4,0),(3,0),(2,0),(1,0),(0,0)]
        
    def updateCoordiantes(self, x, y):
        if self.direction=="UP":
            y-=1
        elif self.direction=="DOWN":
            y+=1   
        elif self.direction=="LEFT":
            x-=1
        elif self.direction=="RIGTH":
            x+=1
        
        return (x,y)
         
    def eat(self):
        
        for i in range(10):
            
            (x,y)=self.body[0]
            
            x,y=self.updateCoordiantes(x,y)
            
            
            self.body.insert(0, (x,y))
        
    def move(self):
        #Vamos a colocarle la cabeza a la serpiente
        (x,y)=self.body[0]
        x,y=self.updateCoordiantes(x,y)
        self.body.insert(0, (x,y))
        
        #Remove the tail
        self.body.pop()

  
        
        