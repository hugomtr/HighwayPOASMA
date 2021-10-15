class Vehicle:

    def __init__(self,but,y,x=0,speed=1):
        self.but = but
        self.x = x
        self.y = y

    def insert():
        """ 
        la vitesse 
        """

    def move():
        """
        """

    def speedUp():
        """ 
        modification vitesse
        """

    def slowDown():
        """
        """

    def exit():
        """ 
        """
    
    def overtake():
        """
        """


class State:

    def __init__(self,highway,exit):
        self.highway = np.zeros((2,100))
        self.exit = np.array([2,18,34,78])
    
    def update(self):
        nombre_voiture_entrantes = 2 

        voitures = []
        for i in range(nombre_voiture_entrantes):
            voitures[i] = vehicle(exit[1],)
            