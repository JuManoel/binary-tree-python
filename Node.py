class Node():
    def __init__(self, val=0,nodeD=None,nodeE=None) -> None:
        """
        __init__(int, Node, Node)
        definir inicialmente el nodo Derecho y Esquiero y su valor
        valores por defecto: 0, None, None
        """
        self.val = val
        self.nodeD = nodeD
        self.nodeE = nodeE

    def findVal(val):
        if(self.val == val):
            return self
        if(val>self.val):
            if(self.nodeD != None):
                return self.nodeD.findVal(val)
            return 
        if(val<self.val and self.nodeE != None):
            return self.nodeE.findVal(val)
    