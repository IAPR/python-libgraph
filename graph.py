from node import Node

class Graph:
    """
    This class contains a graph and all the functions it uses.
    """

    def __init__(self):
        self.NodeList = []
        
    def __repr__(self):
        returnStr = ""
        for node in self.NodeList:
            returnStr = returnStr + str(node) + "\n"
        return returnStr

    def __str__(self):
        return self.__repr__()
        
    

    def BFS(self, origin, dest_id):
        #
        # create empty queue Q   
        # 
        # root.distance = 0
        # Q.enqueue(root)
        opened = [ (origin, 0, None) ]  # (node, distance, parent)
        closed = []
        parent_list = []
        dest = None
        
        def SearchParent(node):
            for c in closed:
                n = c[0]
                if(node.id == n.id):
                    return c[2]
            return None
        
        def Search():
            nonlocal opened
            nonlocal closed
            while( len(closed) < len(self.NodeList) ):
                new_opened = []
                   
                # while Q is not empty:
                while( len(opened) > 0 ):
                    #     current = Q.dequeue()
                    cur_opened = opened.pop()
                    node = cur_opened[0]
                    
                    if(node.id == dest_id):
                        return cur_opened[2]
                    
                #     for each node n that is adjacent to current:
                    for inner_node, size in node.adyacentList:
                #         if n.distance == INFINITY:
                #             n.distance = current.distance + 1
                #             n.parent = current
                #    Si el nodo ya esta cerrado, pasar al siguiente
                        if( inner_node in closed or inner_node in opened ):
                            continue
                        newly_opened = ( inner_node, size, node )
                #             Q.enqueue(n)
                        new_opened.append(newly_opened)
                #   closenode()
                    closed.append(cur_opened)
                # update opened list
                opened += new_opened
            
        # Search By BFS
        dest = Search()
        # Get route
        c = dest
        while(c != None):
            parent_list.append(c)
            c = SearchParent(c)
        parent_list.reverse()
        
        return parent_list

    def DFS(self, origin, dest_id):
        visited = []
        route_list = []
        
        def Search(node, depth = 0):
            #
            # Marcar al nodo como visitado, para pasar por el
            # de nuevo
            #
            if(node not in visited):
                visited.append(node)
                
            ## DEBUG
            # for v in visited:
            #     print("V:", v.id)

            # Buscar dentro de los nodos internos
            for innerNode,size in node.adyacentList:
                if(innerNode in route_list):
                    continue
                    
                ## DEBUG
                # print(innerNode, dest_id)
                # input()
                
                # Anadir a la ruta
                route_list.append(node)
                
                # Si la ruta es el destino, dejar de buscar
                if(innerNode.id == dest_id):
                    return True
                # Seguir buscando si no es
                else: 
                    res = Search(innerNode, depth + 1)
                    
                    if( res is False):
                        route_list.pop()
                    else:
                        return res         
            return False
            
        result = Search(origin)
        if(result is True):
            return route_list
        else:
            return None
