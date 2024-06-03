import numpy as np


class Node():
    def __init__(self, val=0, nodeD=None, nodeE=None) -> None:
        """
        __init__(self,numero, Node, Node)
        definir inicialmente el nodo Derecho y Esquiero y su valor
        valores por defecto: 0, None, None
        """
        # Validar si los datos son los buenos
        self.__validarNode__(nodeD)
        self.__validarNode__(nodeE)
        self.__validarValor__(val)

        # converter para el tipo de dato ideal
        # como no sabemos el tamaño del arbole, la memora será un recurso esencial para nosotros
        val = self.__conveterVal__(val)
        # apos validar los tipos de datos y garantir que todo esta ok, asigno los valores
        self.val = val
        self.nodeD = nodeD
        self.nodeE = nodeE

    def findVal(self, val):
        """
        findVal(self, numero)
        funcion que retorna el nodo en que esta el valor que buscas
        caso el valor que buscas no esta en el arbole, retorna que el valor esta malo
        """
        self.__validarValor__(val)
        val = self.__conveterVal__(val)
        if (self.val == val):
            return self
        if (val > self.val):
            if (self.nodeD is not None):
                return self.nodeD.findVal(val)
            raise ValueError(f"{val} no existe en el Arbole")
        if (val < self.val):
            if (self.nodeE is not None):
                return self.nodeE.findVal(val)
            raise ValueError(f"{val} no existe en el Arbole")

    def inOrden(self):
        """
        Percorre el arbole en inOrden utilizando funciones recursivas
        """
        if (self.nodeE is not None and self.nodeD is not None):
            return f"{self.nodeE.inOrden()} {self.val} {self.nodeD.inOrden()} "
        if (self.nodeE is None and self.nodeD is not None):
            return f"{self.val} {self.nodeD.inOrden()} "
        if (self.nodeE is not None and self.nodeD is None):
            return f"{self.nodeE.inOrden()} {self.val} "
        return f" {self.val} "

    def preOrden(self):
        """
        Percorre el arbole en preOrden, utilizando recursion
        """
        if (self.nodeE is not None and self.nodeD is not None):
            return f"{self.val} {self.nodeE.preOrden()} {self.nodeD.preOrden()} "
        if (self.nodeE is None and self.nodeD is not None):
            return f"{self.val} {self.nodeD.preOrden()} "
        if (self.nodeE is not None and self.nodeD is None):
            return f"{self.val} {self.nodeE.preOrden()} "
        return f" {self.val} "

    def posOrden(self):
        """
        Percorre el arbole en posOrden, utilizando recursion
        """
        if (self.nodeE is not None and self.nodeD is not None):
            return f"{self.nodeE.posOrden()} {self.nodeD.posOrden()} {self.val}"
        if (self.nodeE is None and self.nodeD is not None):
            return f"{self.nodeD.posOrden()} {self.val}"
        if (self.nodeE is not None and self.nodeD is None):
            return f"{self.nodeE.posOrden()} {self.val}"
        return f"{self.val}"

    def adicionarVal(self, val):
        """
        adicionarVal(self, numero)
        Intenta adicionar un nuevo valor en el arbole
        Utilizando recursion, me permite buscar el local ideal para el nuevo valor
        """
        self.__validarValor__(val)
        val = self.__conveterVal__(val)
        if (self.val == val):
            raise ValueError(f"El valor {val} ya existe en el arbole")
        if (val > self.val):
            if (self.nodeD is None):
                self.nodeD = Node(val)
                return
            self.nodeD.adicionarVal(val)
        elif (val < self.val):
            if (self.nodeE is None):
                self.nodeE = Node(val)
                return
            self.nodeE.adicionarVal(val)

    def __validarValor__(self, val):
        """
        funcion unicamente para saber si el valor es de tipo valido
        retorna una exepcion caso que no
        """
        if not isinstance(val, (int, float)):
            raise TypeError(
                f"El valor del nodo tiene que ser numerico, no puede ser {val}")

    def __validarNode__(self, node):
        """
        Funcion unicamente para saber si el node esta bien
        retorna una execpcion caso que no
        """
        if not isinstance(node, (Node, type(None))):
            raise TypeError(f"El nodo no puede ser: {node}")

    def __conveterVal__(self, val):
        """
        funcion que retorna el valor convertido para el tipo de dato ideal
        la memoria es un recurso esencial en los arboles, entonces, converter para el tipo de dato
        ideal, es una prioridad
        """
        if isinstance(val, int):
            if np.iinfo(np.int8).min <= val <= np.iinfo(np.int8).max:
                return np.int8(val)
            elif np.iinfo(np.int16).min <= val <= np.iinfo(np.int16).max:
                return np.int16(val)
            elif np.iinfo(np.int32).min <= val <= np.iinfo(np.int32).max:
                return np.int32(val)
            else:
                return np.int64(val)
        elif isinstance(val, float):
            if np.finfo(np.float32).min <= val <= np.finfo(np.float32).max:
                return np.float32(val)
            else:
                return np.float64(val)
