import numpy as np
import time

class Vehicle:
    
    def __init__(self,direction,x,y,speed=1):
        self.direction = direction
        self.x = x
        self.y = y
        self.view = []
        self.speed = speed

    def obstacle_free(self,x,y,position,speed):
        return True 

    
    def test_diretion(self,x,y,matrix):
        x = self.x
        y = self.y
        if matrix[y+1] in set(1,3) and matrix[y-1] == 0:
            return np.array([x+1,y])
        if matrix[y+1] == 0 and matrix[y-1] in set(1,3):
            return np.array([x-1,y])
        if matrix[x-1] in set(1,3) and matrix[x+1] == 0:
            return np.array([x,y+1])
        if matrix[x-1] in set(1,3) and matrix[x+1] == 0:
            return np.array([x,y-1])


    def move_forward(self,x,y,sens):
        # return couple de la position sur la matrice si on avance d'une case
        direction = self.test_direction()
        if obstacle_free(self.x,self.y,direction,self.speed):
            new_pos = (direction - np.array([self.x,self.y]))*self.speed
            self.x,self.y = self.x + new_pos[0], self.y + new_pos[1]

        # gérer le cas où les voitures quittent la matrice


    def handle_configuration_encountered(self,x,y):
        """ 
        L'agent va rencontrer 3 config possible
        -> deplacement sur un axe:
        dans ce cas démarche classique move_forward() 
        -> sur le point d'integrer une intersection
        dans ce cas 
        -> sur une intersetion
        dans ce cas choix entre 3 actions possibles: choix de la meilleure (heuristique de manhatan)
            -turn_right()
            -move_forxard_intersection()
            -turn_left()
        on va determiner la config à l'aide de la fonction find_config()
        """
        raise NotImplementedError


    def moveToGoal(self,matrix):
        """ fonction qui va gérer la voiture du début à la fin """
    
class State:
    
    def __init__(self,voitures):
        self.highway = np.zeros((2,40))
        self.voitures = voitures
    
    def update(self):
        for v in self.voitures:
            v.move(self.highway)
        return self.highway


nsroad1 = np.array([5,11,18,28,37,43,49,59,76,89,95])
nsroad2 = nsroad1+1
ewroad1 = np.array([7,13,22,45,67,78,90])
ewroad2 = ewroad1+1
mat = np.zeros((100,100)).astype('int8')

for c in nsroad1:
    mat[:,c] += 1
for l in ewroad1:
    mat[l,:] += 1

for c in nsroad2:
    mat[:,c] += 3
for l in ewroad2:
    mat[l,:] += 3
    
# plt.imshow(mat,cmap='hot')
# plt.show()

mattest = mat[5:15,5:15]


voiture1 = Vehicle(-1,1,-1)
voiture2 = Vehicle(1,0,0)
voiture3 = Vehicle(-1,1,39)
state = State([voiture1,voiture2,voiture3])
for i in range(10):
    mat = state.update()
    print(mat)
    time.sleep(1)




                
    

        
        

        


            
