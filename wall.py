"""
@author: lucasaissaoui
"""


class wall: 

    def __init__(self, x0, y0, x1, y1, canvas):
        # Position courante de l'agent 
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.canvas = canvas

    def draw(self):
        self.canvas.create_rectangle(self.x0, self.y0,self.x1 ,self.y1, fill='black', outline='black')
        
    def free(self, x, y): 
        return  x<self.x0 or x>self.x1 or y<self.y0 or y>self.y1 
   
        
