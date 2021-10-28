import numpy as np
import matplotlib.pyplot as plt
import time

class Vehicle:
    
    def __init__(self,but,x,y,sens,speed=1):
        self.but = but
        self.x = x
        self.y = y
        self.speed = speed
        self.sens = sens


    def find_diretion(self,x,y,matrix):
        # the agent needs to go down
        if matrix[y+1] in set(1,3) and matrix[y-1] == 0:
            return np.array([1,0])
        # the agent needs to go up
        if matrix[y+1] == 0 and matrix[y-1] in set(1,3):
            return np.array([-1,0])
        # the agent needs to go right
        if matrix[x-1] in set(1,3) and matrix[x+1] == 0:
            return np.array([0,1])
        # the agent needs to go left
        if matrix[x-1] in set(1,3) and matrix[x+1] == 0:
            return np.array([0,-1])


    def vision_agent(self,x,y,direction,matrix):
        vision = []
        # adding forward cases
        for i in range(self.speed):
            vision.append(matrix[x+direction[0]*i,y+direction[1]*i])
        
        # adding surrounding cases
        rv_direction = direction[::-1]  # reverse order
        vision.append(matrix[x+rv_direction[0],y+rv_direction[1]])
        vision.append(matrix[x-rv_direction[0],y-rv_direction[1]])
        return np.array(vision)


    def handle_obstacle(self,x,y,direction,matrix,speed):
        """
        L'agent doit normalement avancer de la vitesse self.speed
        Si il y'a self.speed cases de libres (sans usagers et feu vert ou rouge) dans la direction ou va l'agent 
        alors return True
        """
        # on récupere ce qu'il y'a directement devant nous jusqu'a la case où l'on souhaite aller
        forward_vision = self.vision_agent(x,y,direction,matrix)[:self.speed]
        count = 0
        for case in forward_vision[1:]:
            if matrix[case[0],case[1]] == 12:
                return forward_vision[count]
            count += 1
            # à implementer ensuite tester si l'on tombe sur un feu rouge
            # ... #
        # si aucun obstacle on retourne 
        return forward_vision[-1]


    def move_forward(self,x,y):
        direction = self.find_direction(x,y)
        new_pos = self.handle_obstacle(x,y,direction,self.speed)         
        x,y = new_pos[0],new_pos[1]
        # reste à faire ->
        # gérer le cas où les voitures quittent la matrice

    
    def heuristique(self,x,y,but):
        return np.abs(but[0]-x) + np.abs(but[1]-y)
    
    
    def choose_best_direction(self,x,y):
        raise NotImplementedError


    def handle_configuration_encountered(self,x,y,matrix):
        """ 
        L'agent va rencontrer 3 config possible
        -> deplacement sur un axe:
        dans ce cas démarche classique move_forward() 
        -> sur le point d'integrer une intersection
        dans ce cas 
        -> sur une intersetion
        dans ce cas choix entre 3 actions possibles: choix de la meilleure (heuristique de manhatan)
            -turn_right()
            -move_forward_intersection()
            -turn_left()
        on va determiner la config à l'aide de la fonction find_config()
        """
        direction = self.find_direction()
        next_position = np.array([x,y]) + direction
        next_x,next_y = next_position[0],next_position[1]
        if matrix[next_x,next_y] == 6 and self.sens == 1:
            # checker les feux rouges
            self.choose_best_direction(x,y)
            

    def moveToGoal(self,x,y,matrix):
        """ fonction qui va gérer la voiture du début à la fin """
        raise NotImplementedError

# North South road 
nsroad1 = np.array([5,11,18,28,37,43,49,59,76,89,95])
nsroad2 = nsroad1+1

# Est West Road
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
    
# show the matrix -->
plt.imshow(mat,cmap='hot')
plt.show()

mattest = mat[5:15,5:15]


class State:
    
    def __init__(self,voitures):
        self.environnement = mattest
        self.voitures = voitures
    
    def update(self):
        for v in self.voitures:
            v.move(self.highway)
        return self.highway


# **********  TEST A VENIR **************
 
# voiture1 = Vehicle(-1,1,-1)
# voiture2 = Vehicle(1,0,0)
# voiture3 = Vehicle(-1,1,39)
# state = State([voiture1,voiture2,voiture3])
# for i in range(10):
#     mat = state.update()
#     print(mat)
#     time.sleep(1)




                
    

        
        

        


            
