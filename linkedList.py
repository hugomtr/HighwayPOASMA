class Node:

    def __init__(self, right=0, left = 0,exit=0):
        self.right = right
        self.left = left
        self.next = None
        self.exit = exit
        # 0 = pas une sortie; x > 0 = sortie numéro x
    
class CircularLinkedList:

    def __init__(self):
        self.head = None
    
    def push(self,data):
        node = Node(data)

        tmp = node
        node.next = self.head

        if self.head is not None:
            while(tmp is not None):
                tmp = tmp.next
            tmp.next = node
            node.next = None
        else:
            self.head = node

    def print():
        """
        affiche la liste circulaire
        """ 

          








    