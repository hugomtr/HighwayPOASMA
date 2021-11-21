import numpy as np
import matplotlib.pyplot as plt
import copy

class Vehicle:
    
    def __init__(self,but,x,y,direction,speed=1):
        self.but = but
        self.x = x
        self.y = y
        self.speed = speed
        self.direction = direction
        self.intersection_count = 0
        self.leaving_intersection = False
        self.possible_move = []
        self.best_case = []

    def vision_agent(self):
        vision = []

        # adding forward cases
        for i in range(self.speed+1):
            vision.append([self.x+self.direction[0]*i,self.y+self.direction[1]*i])

        vision.append([self.x+self.direction[1]+self.direction[0],self.y+self.direction[0]+self.direction[1]]) # adding element in reverse order to
        vision.append([self.x-self.direction[1]+self.direction[0],self.y-self.direction[0]+self.direction[1]]) # obtain front left end right diagonal element

        return np.array(vision)


    def handle_obstacle(self,matrix):
        """
        L'agent doit normalement avancer de la vitesse self.speed
        Si il y'a self.speed cases de libres (sans usagers et feu vert ou rouge) dans la direction ou va l'agent 
        alors return True
        """
        forward_vision = self.vision_agent()[:self.speed+1]
        count = 0
        # on récupere ce qu'il y'a directement devant nous jusqu'a la case où l'on souhaite aller
        for case in forward_vision[1:]: 
            # we meet an other vehicle = 12 or we are at an intersection 2
            if matrix[case[0],case[1]] in set((2,8)):
                return forward_vision[count]
            count += 1
            # à implementer ensuite tester si l'on tombe sur un feu rouge
            # ... #
        # si aucun obstacle 
        return forward_vision[-1]

    
    def move_forward(self,matrix):
        print("***")
        new_pos = self.handle_obstacle(matrix).astype(int) 
        print("pos",new_pos)      
        oldx, oldy = self.x,self.y
        
        # la voiture s'est deplacé ancienne position libre
        matrix[oldx,oldy] = 1
        self.x,self.y = new_pos[0],new_pos[1]

        # la voiture s'est deplacé nouvelle position
        matrix[new_pos[0],new_pos[1]] = 8
        print(matrix)
        print("***")
        # reste à faire ->
        # gérer le cas où les voitures quittent la matrice

    
    def allowed_direction_att_intersection(self):
        # cas ou on tourne à gauche
        left_direction = {(-1,0):(0,-1), (0,1):(-1,0), (1,0):(0,1), (0,-1):(1,0)} 
        # allowed_case = [matrix[self.x+self.direction[0],self.y+self.direction[1]],
        #                 matrix[self.x+self.direction[0]*2,self.y+self.direction[1]*2],
        #                 matrix[self.x+self.direction[0]*2 + left_direction[self.direction][0],
        #                 self.y+self.direction[1]*2 + left_direction[self.direction][1]]]
        
        allowed_index = [(self.x+self.direction[0],self.y+self.direction[1]),
                        (self.x+self.direction[0]*2,self.y+self.direction[1]*2),
                        (self.x+self.direction[0]*2 + left_direction[self.direction][0],
                        self.y+self.direction[1]*2 + left_direction[self.direction][1])]
        return allowed_index   


    def heuristique(self,x,y,but):
        # distance de manhatan
        return np.abs(but[0]-x) + np.abs(but[1]-y)
    
    
    def choose_best_direction(self):
        print(self.possible_move)
        frontier = np.array([self.heuristique(case[0],case[1],self.but) for case in self.possible_move])
        indice_min = np.argmin(frontier)
        print("frontier",frontier)
        print("indice_min",indice_min)
        print(self.possible_move[indice_min])
        self.in_intersection = True
        return self.possible_move[indice_min]


    def move_through_intersection(self,vehicle_matrix):
        distance_from_best_case = self.possible_move.index(self.best_case)+1

        new_pos = self.possible_move[self.speed*self.intersection_count - 1]
        print("new_pos",new_pos)
        print("count",self.intersection_count)
        # on met a jour l'ancienne position comme libre
        vehicle_matrix[self.x,self.y] = 1 

        if distance_from_best_case > self.speed*self.intersection_count:
            vehicle_matrix[new_pos[0],new_pos[1]] = 8
            self.x,self.y = new_pos[0],new_pos[1]
            print("pas encore à la best_case")
            #print(vehicle_matrix)
            return False
        else:
            print("a la best_case")
            vehicle_matrix[self.best_case[0],self.best_case[1]] = 8
            self.x,self.y = self.best_case[0],self.best_case[1]
            #print(vehicle_matrix)
            return True


    def update_direction(self):
        distance_from_best_case = self.possible_move.index(self.best_case)+1
        # indice dans la matrice de l'element atteint
        direction = {"left" : {(-1,0):(0,-1), (0,1):(-1,0), (1,0):(0,1), (0,-1):(1,0)}, 
                    "right" : {(-1,0):(0,1), (0,1):(1,0), (1,0):(0,-1), (0,-1):(-1,0)}}
        
        print("ancienne direction", self.direction)

        if distance_from_best_case == 1:  # on tourne à droite
            self.direction = direction["right"][self.direction]
        elif distance_from_best_case == 3:  # on tourne à gauche
            self.direction = direction["left"][self.direction]
        
        print("nouvelle direction", self.direction)



    def handle_intersection(self,vehicle_matrix):
        """
        gère l'intersection de A à Z
        """
        self.intersection_count += 1
        if self.intersection_count == 1:
            print("modif apporté")
            self.possible_move = self.allowed_direction_att_intersection()
            self.best_case = self.choose_best_direction()

        if self.leaving_intersection:
            self.move_forward(vehicle_matrix)
            print("leaving intersection")
            self.intersection_count = 0
            self.leaving_intersection = False
            return

        # test si l'on a atteint la fin de l'intersection
        if self.move_through_intersection(vehicle_matrix):
            print(self.intersection_count,"at the best case")
            self.update_direction()
            self.leaving_intersection = True



    def handle_configuration_encountered(self,road_matrix,vehicle_matrix):
        """ gère les configurations trouvés et appelle les fonctions correspondantes """
       
        if self.x == self.but[0] and self.y == self.but[1]:  # test si on est au but
            print("Nous sommes au but")
            return 

        next_position = np.array([self.x,self.y]) + self.direction
        next_x,next_y = next_position[0],next_position[1]
        
        if road_matrix[next_x,next_y] == 1 and self.intersection_count == 0: # nous n'arrivons pas sur une intersection à corriger
            print("sur une route")
            self.move_forward(vehicle_matrix)
        else:
            print("sur une intersection")
            self.handle_intersection(vehicle_matrix)


    def moveToGoal(self,road_matrix,vehicle_matrix):
        """ fonction qui va gérer la voiture du début à la fin """
        self.handle_configuration_encountered(road_matrix,vehicle_matrix)


def initialize():
    # North South road 
    nsroad1 = np.array([5,11,18,28,37,43,49,59,76,89,95])
    nsroad2 = nsroad1+1

    # Est West Road
    ewroad1 = np.array([7,13,22,45,67,78,90])
    ewroad2 = ewroad1+1
    road_mat = np.zeros((100,100)).astype('int8')
    vehicle_mat = np.zeros((100,100)).astype('int8')

    for c in nsroad1:
        road_mat[:,c] += 1
    for l in ewroad1:
        road_mat[l,:] += 1

    for c in nsroad2:
        road_mat[:,c] += 1
    for l in ewroad2:
        road_mat[l,:] += 1

    for c in nsroad1:
        vehicle_mat[:,c] = 1
    for l in ewroad1:
        vehicle_mat[l,:] = 1

    for c in nsroad2:
        vehicle_mat[:,c] = 1
    for l in ewroad2:
        vehicle_mat[l,:] = 1
        
    mattest_road = road_mat[15:40,15:40]
    mattest_vehicle = vehicle_mat[15:40,15:40]

    return mattest_vehicle,mattest_road


def affichage(vehicle_mat,road_mat):
    plt.matshow(vehicle_mat + road_mat)
    plt.show()

# class Environnment:
    
#     def __init__(self,voitures):
#         self.mat_voiture = initialize()[0]
#         self.mat_road = initialize()[1]        
#         self.voitures = voitures
    
#     def update(self):
#         for v in self.voitures:
#             v.moveToGoal(v.x,v.y,v.direction,self.mat_road,self.mat_voiture)
#         return self.highway


# **********  TEST A VENIR **************
 
# voiture1 = Vehicle(-1,1,-1)
# voiture2 = Vehicle(1,0,0)
# voiture3 = Vehicle(-1,1,39)
# state = State([voiture1,voiture2,voiture3])
# for i in range(10):
#     mat = state.update()
#     print(mat)
#     time.sleep(1)

if __name__ == '__main__':
    mattest_vehicle = initialize()[0]
    mattest_road = initialize()[1]

    but = [[7,7],[8,24],[7,2]]

    mattest_vehicle[7,7] = 5
    mattest_vehicle[8,24] = 5
    mattest_vehicle[7,2] = 5

    vleft = Vehicle([7,7],22,14,(-1,0))
    vstraight = Vehicle([8,24],8,11,(0,1))
    vright = Vehicle([7,2],1,13,(1,0))

    mattest_vehicle[vleft.x,vleft.y] = 8
    mattest_vehicle[vstraight.x,vstraight.y] = 8
    mattest_vehicle[vright.x,vright.y] = 8

    print(mattest_vehicle)

    for i in range(20):
        vleft.moveToGoal(mattest_road,mattest_vehicle)
        vstraight.moveToGoal(mattest_road,mattest_vehicle)
        vright.moveToGoal(mattest_road,mattest_vehicle)
        print(mattest_vehicle)
                

    

        
        

        


            
