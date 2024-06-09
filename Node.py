import numpy as np
"""
Para los que no son de python:
Python no tiene "private", pero si queremos hacer algo parecido
nos toca utilizar el las "__" antes y despues del nombre del metodo o atributo
Si queremos llamar algo que pertenece al objeto, en java utilizamos el this.algo
aca en python utilizamos el self.algo
Python no es un lenguaje tipado (o sea no hay int, float, double) como java
entonces para "convertelo" en tipado, utilizamos la libreria  numpy (NUMeros con PYthon)
que nos regala un "control" de la memoria muy bueno
El throw que tenemos en java, aca en python es raise Execption
"""


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
            return f"{self.nodeE.inOrden()}, {self.val}, {self.nodeD.inOrden()}"
        if (self.nodeE is None and self.nodeD is not None):
            return f"{self.val}, {self.nodeD.inOrden()}"
        if (self.nodeE is not None and self.nodeD is None):
            return f"{self.nodeE.inOrden()}, {self.val}"
        return f"{self.val}"

    def preOrden(self):
        """
        Percorre el arbole en preOrden, utilizando recursion
        """
        if (self.nodeE is not None and self.nodeD is not None):
            return f"{self.val}, {self.nodeE.preOrden()}, {self.nodeD.preOrden()}"
        if (self.nodeE is None and self.nodeD is not None):
            return f"{self.val}, {self.nodeD.preOrden()}"
        if (self.nodeE is not None and self.nodeD is None):
            return f"{self.val}, {self.nodeE.preOrden()}"
        return f"{self.val}"

    def posOrden(self):
        """
        Percorre el arbole en posOrden, utilizando recursion
        """
        if (self.nodeE is not None and self.nodeD is not None):
            return f"{self.nodeE.posOrden()}, {self.nodeD.posOrden()}, {self.val}"
        if (self.nodeE is None and self.nodeD is not None):
            return f"{self.nodeD.posOrden()}, {self.val}"
        if (self.nodeE is not None and self.nodeD is None):
            return f"{self.nodeE.posOrden()}, {self.val}"
        return f"{self.val}"

    def adicionarVal(self, val):
        """
        adicionarVal(self, numero)
        Intenta adicionar un nuevo valor en el arbole
        Utilizando recursion, me permite buscar el local ideal para el nuevo valor
        """
        self.__validarValor__(val)
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
    
    def max(self):
        if(self.nodeD is None):
            return self.val
        return self.nodeD.max()
    
    def min(self):
        if(self.nodeE is None):
            return self.val
        return self.nodeE.min()

    def __validarValor__(self, val):
        """
        funcion unicamente para saber si el valor es de tipo valido
        retorna una exepcion caso que no
        """
        # aca valido el tipo de dato "primitivo"
        if (type(val) != type(0) and type(val) != type(0.0)):
            # creo unas listas de los tipos de datos de numpy
            tipos_enteros = (np.int8, np.int16, np.int32,
                             np.int64, np.intc, np.int_)
            tipos_flotantes = (np.float16, np.float32, np.float64, np.float_)
            # valido si es hijo de eses tipos
            if (isinstance(val, tipos_enteros) and isinstance(val, tipos_flotantes)):
                raise TypeError(
                    f"El valor del nodo tiene q ser numerico, no puede ser {val}")
        return

    def __validarNode__(self, node):
        """
        Funcion unicamente para saber si el node esta bien
        retorna una execpcion caso que no
        """
        if (type(node) != type(Node) and type(node) != type(None)):
            raise TypeError(f"El nodo esquierdo no puede ser: {node}")
        return

    def __conveterVal__(self, val):
        """
        funcion que retorna el valor convertido para el tipo de dato ideal
        la memoria es un recurso esencial en los arboles, entonces, converter para el tipo de dato
        ideal, es una prioridad
        """
        self.__validarValor__(val)
        if (type(val) == type(0)):
            if val < np.iinfo(np.int8).max and val > np.iinfo(np.int8).min:
                return np.int8(val)
            elif val < np.iinfo(np.int16).max and val > np.iinfo(np.int16).min:
                return np.int16(val)
            elif val < np.iinfo(np.int32).max and val > np.iinfo(np.int32).min:
                return np.int32(val)
            else:
                return np.int64(val)
        elif (type(val) == type(0.0)):
            if val < np.finfo(np.float32).max and val > np.finfo(np.float32).min:
                return np.float32(val)
            else:
                return np.float64(val)
        else:
            return val
