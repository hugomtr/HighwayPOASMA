import numpy as np

class Vehicle:

    def __init__(self,but,y,x=0,speed=1):
        self.but = but
        self.x = x
        self.y = y
        self.speed = speed

    def move(self,highway):
        if (self.y == self.but and self.x == 0):
            return -1

        for i in range(self.speed):
            if highway[self.x][self.y+i] == 1:
                self.slow_down(self.speed - i)
                self.y += self.speed
                return self.x,self.y - self.speed
                
        self.y += self.speed
        return self.x,self.y - self.speed
        
    def speed_up(self,valeur):
        self.speed += valeur

    def slow_down(self,valeur):
        self.speed -= valeur

    # def exit():

    
    # def overtake():
    #     """
    #     """


class State:

    def __init__(self):
        self.highway = np.zeros((2,40))
        self.sortie = np.array([2,18,34])
        self.voitures = []
    
    def update(self):
        nombre_voiture_entrantes = 1 

        for _ in range(nombre_voiture_entrantes):
            self.voitures.append(Vehicle(self.sortie[1],self.sortie[0]))

        for i in range(len(self.voitures)):
            move = self.voitures[i].move(self.highway)
            if move == -1:
                self.highway[self.voitures[i].x,self.voitures[i].y] = 0
                self.voitures.pop(i)
            else:
                self.highway[move[0],move[1]] = 0 # ancienne position mise à 0
                print(self.voitures[i].x,self.voitures[i].y)
                self.highway[self.voitures[i].x,self.voitures[i].y] = 1 # nouvelle mise à 0

state = State()
state.update()
state.update()




                
    

        
        

        


            
