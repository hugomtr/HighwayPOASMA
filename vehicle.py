import numpy as np
import matplotlib.pyplot as plt
import copy

class Vehicle:
    
    def __init__(self,but,x,y,speed=1,at_intersection = False,direction = None):
        self.but = but
        self.x = x
        self.y = y
        self.speed = speed
        self.at_intersection = at_intersection
        self.direction = direction

    def vision_agent(self,x,y,direction,matrix):
        vision = []

        # adding forward cases
        for i in range(self.speed+1):
            vision.append(matrix[x+direction[0]*i,y+direction[1]*i])

        vision.append(matrix[x+direction[1]+direction[0],y+direction[0]+direction[1]]) # adding element in reverse order to
        vision.append(matrix[x-direction[1]+direction[0],y-direction[0]+direction[1]]) # obtain front left end right diagonal element
        return np.array(vision)


    def handle_obstacle(self,x,y,direction,matrix,speed):
        """
        L'agent doit normalement avancer de la vitesse self.speed
        Si il y'a self.speed cases de libres (sans usagers et feu vert ou rouge) dans la direction ou va l'agent 
        alors return True
        """
        forward_vision = self.vision_agent(x,y,direction,matrix)[:self.speed]
        count = 0
        # on récupere ce qu'il y'a directement devant nous jusqu'a la case où l'on souhaite aller
        for case in forward_vision[1:]: 
            # we meet an other vehicle = 12 or we are at an intersection 4,6
            if matrix[case[0],case[1]] in set((2,12)):
                return forward_vision[count]
            count += 1
            # à implementer ensuite tester si l'on tombe sur un feu rouge
            # ... #
        # si aucun obstacle 
        return forward_vision[-1]

    
    def move_forward(self,x,y,direction,matrix):
        new_pos = self.handle_obstacle(x,y,direction,self.speed)         
        oldx, oldy = x,y
        
        matrix[oldx,oldy] == 1
        x,y = new_pos[0],new_pos[1]

        # reste à faire ->
        # gérer le cas où les voitures quittent la matrice

    
    def allowed_direction_att_intersection(self,x,y,matrix,direction):
        allowed_case = [matrix[x+direction[0],y+direction[1]],
                        matrix[x+direction[0]*2,y+direction[1]*2],
                        matrix[x+direction[1],y+direction[0]]]
        
        allowed_index = [[x+direction[0],y+direction[1]],
                        [x+direction[0]*2,y+direction[1]*2],
                        [x+direction[1],y+direction[0]]]
        allowed_index = [np.array(u) for u in allowed_index]
        return allowed_case, allowed_index   


    def heuristique(self,x,y,but):
        # distance de manhatan
        return np.abs(but[0]-x) + np.abs(but[1]-y)
    
    
    def choose_best_direction(self,possible_case):
        frontier = [self.heuristique(case[0],case[1],self.but) for case in possible_case].sort()
        return frontier[0]


    def move_through_intersection(self,best_case,possible_move,matrix):
        distance_from_best_case = possible_move[0].index(best_case)
        index = possible_move[1][distance_from_best_case]
        if index <= self.speed:
            matrix[index[0],index[1]] = 12
            self.x,self.y = index[0],index[1]
            return False
        else:
            matrix[best_case[0],best_case[1]] = 12
            self.x,self.y = best_case[0],best_case[1]
            # on a atteint la case voulue de l'intersection on peut maintenant quitter l'intersection
            return True


    def update_direction(self,oldx,oldy,possible_move,best_case):
        distance_from_best_case = possible_move[0].index(best_case)
        # indice dans la matrice de l'element atteint
        best_case_index = possible_move[1][distance_from_best_case]
        if distance_from_best_case > 1:  # cas simple
            index_before_best_case = possible_move[1][distance_from_best_case-1]
            # update direction 
            self.direction = best_case_index - index_before_best_case 
        else:     # cas relou (l'agent tourne à droite à l'intersection)
            couple = self.direction[0],self.direction[1] # direction transformé en tuple
            dico = {(-1,0) : (0,1),(0,1) : (1,0), (1,0) : (0,-1), (0,-1) : (-1,0)} # correspondance direction nouvelle direction
            self.direction = dico[couple]


    def handle_intersection(self,x,y,road_matrix,vehicle_matrix,direction):
        x_copy, y_copy = x,y
        # possible_move[0] = value , possible_move[1] = index
        possible_move = self.allowed_direction_att_intersection(x,y,road_matrix,direction)
        best_case = self.choose_best_direction(possible_move[0])
        if self.move_through_intersection(best_case,possible_move,vehicle_matrix):
            self.update_direction(x_copy,y_copy,possible_move)
        # update direction when exiting the intersection


    def handle_configuration_encountered(self,x,y,direction,road_matrix,vehicle_matrix):
        """ 
        L'agent va rencontrer 2 config possible
        -> deplacement sur un axe:
        dans ce cas démarche classique move_forward() 
        -> sur une intersetion
        dans ce cas choix entre 3 actions possibles: choix de la meilleure (heuristique de manhatan)
            -tourner à gauche
            -aller de l'avant
            -tourner à droite
        """
        while self.x != self.but[0] and self.y != self.but[1]:
            next_position = np.array([x,y]) + direction
            next_x,next_y = next_position[0],next_position[1]
            if road_matrix[next_x,next_y] == 1: # nous n'arrivons pas sur une intersection A corriger
                self.move_forward(x,y,road_matrix,vehicle_matrix,direction)
            else:
                self.handle_intersection(x,y,road_matrix,vehicle_matrix,direction)


    def moveToGoal(self,x,y,road_matrix,vehicle_matrix):
        """ fonction qui va gérer la voiture du début à la fin """
        direction = self.find_direction()
        self.handle_configuration_encountered(x,y,direction,road_matrix,vehicle_matrix)


# North South road 
nsroad1 = np.array([5,11,18,28,37,43,49,59,76,89,95])
nsroad2 = nsroad1+1

# Est West Road
ewroad1 = np.array([7,13,22,45,67,78,90])
ewroad2 = ewroad1+1
road_mat = np.zeros((100,100)).astype('int8')

for c in nsroad1:
    road_mat[:,c] += 1
for l in ewroad1:
    road_mat[l,:] += 1

for c in nsroad2:
    road_mat[:,c] += 1
for l in ewroad2:
    road_mat[l,:] += 1

vehicle_mat = np.zeros(road_mat.shape).astype('int8')
mat = vehicle_mat + road_mat
#show the matrix -->
# plt.imshow(mat,cmap='hot')
# plt.show()


mattest = road_mat[15:40,15:40]
mattest[13,13] = 12
plt.imshow(mattest,cmap='hot')
plt.show()

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




                
    

        
        

        


            
