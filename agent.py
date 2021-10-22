"""
@author: lucasaissaoui
"""

import numpy as np


class Agent: 
    
    def __init__(self, x, y, xGoal, yGoal, canvas):
        # Position courante de l'agent 
        self.x = x
        self.y = y
        
        # Posoition but de l'agent 
        self.xGoal = xGoal
        self.yGoal = yGoal
        
        # Constante d'affichage
        self.aRadius = 5
        self.sRadius = 8
        
        self.canvas = canvas
        self.goalDraw =  self.canvas.create_oval(self.xGoal - self.sRadius, self.yGoal - self.sRadius , self.xGoal + self.sRadius, self.yGoal + self.sRadius, outline='green')
        self.agentDraw = self.canvas.create_oval(self.x - self.aRadius, self.y - self.aRadius , self.x + self.aRadius, self.y + self.aRadius, fill='blue', outline='blue')
        
        
    def up(self):
        self.eraseAgent()
        self.y = self.y - 10
        self.drawAgent()
        
    def down(self): 
        self.eraseAgent()
        self.y = self.y + 10
        self.drawAgent()
        
    def left(self): 
        self.eraseAgent()
        self.x = self.x - 10
        self.drawAgent()
        
    def right(self): 
        self.eraseAgent()
        self.x = self.x + 10
        self.drawAgent()
        
    def moveToGoal(self):
        
        if self.x == self.xGoal and self.y == self.yGoal:
            print("Goal")
        else:
            dirs = np.zeros(4)
            
            dirs[0] = np.sqrt((self.xGoal - self.x)**2 + (self.yGoal - self.y - 10)**2)
            dirs[1] = np.sqrt((self.xGoal - self.x + 10)**2 + (self.yGoal - self.y)**2)
            dirs[2] = np.sqrt((self.xGoal - self.x)**2 + (self.yGoal - self.y + 10)**2)
            dirs[3] = np.sqrt((self.xGoal - self.x - 10)**2 + (self.yGoal - self.y)**2)

            dirToGo = np.argmax(dirs)
            
            print("Dirs : ", dirs)
            #print("Dir : ", dirToGo)
            
            if dirToGo == 0:
                self.up()
            elif dirToGo == 1:
                self.right()
            elif dirToGo == 2: 
                self.down()
            elif dirToGo == 3: 
                self.left()
            
        
    def drawAgent(self):
        self.agentDraw = self.canvas.create_oval(self.x - self.aRadius, self.y - self.aRadius , self.x + self.aRadius, self.y + self.aRadius, fill='blue', outline='blue' )
        
    def eraseAgent(self): 
        self.canvas.delete(self.agentDraw)