class Node:
    """
    This class is used as a base for nodes for the graph.
    """

    #
    # Adyacencia
    #   (Nodo, Magnitud)
    #

    def __init__(self, _id):
        self.id = _id
        self.adyacentList = []

    def __repr__(self):
        return self.id
        
    def __str__(self):
        return self.__repr__()
        
    def Print(self):
        print("ID:", self.id)
        for node,size in self.adyacentList:
            print("N:", node.id, "S:", size)
        print("\n")