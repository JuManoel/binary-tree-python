class NodeAnimals():
    def __init__(self, pergunta="", animal="", resp1=None, resp2=None, respA="") -> None:
        self.__validarNode__(resp1)
        self.__validarNode__(resp2)
        self.pergunta = pergunta
        self.animal = animal
        self.resp1 = resp1
        self.resp2 = resp2
        self.respA = respA

    def adicionar(self):
        print("Que tipo de animal es?")
        animal = input()
        print(f"Qué pregunta distinguiría a un {self.animal} en {animal}?")
        pregunta = input()
        print(f"Si el animal fuera un {animal}, cuál sería la respuesta?")
        resp = input()
        node = NodeAnimals(pergunta=pregunta, animal=animal, respA=resp)
        self.__validarNode__(node)
        if (resp.lower() == "si"):
            self.resp1 = node
            self.resp2 = NodeAnimals(animal=self.animal,respA="no")
        elif (resp.lower() == "no"):
            self.resp2 = node
            self.resp1 = NodeAnimals(animal=self.animal,respA="si")
        else:
            print("Esa respuesta es invalida")

    def preguntar(self):
        print(self.pergunta)
        resp = input()
        if (resp.lower() == self.respA):
            if (resp.lower() == "si"):
                if (self.resp1 is not None):
                    self.resp1.preguntar()
                    return
            elif (resp.lower() == "no"):
                if (self.resp2 is not None):
                    self.resp2.preguntar()
                    return
            print(f"Es un: {self.animal}?")
            resp = input()
            if (resp.lower() == "no"):
                if (self.resp2 is not None):
                    self.resp2.preguntar()
                    return
                self.adicionar()
                return
            print("Voy un genio, no?")
            return
        if (resp.lower() == "si"):
            if (self.resp1 is not None):
                self.resp1.preguntar()
                return
            self.adicionar()
        elif (resp.lower() == "no"):
            if (self.resp2 is not None):
                self.resp2.preguntar()
                return
            self.adicionar
        return

    def __validarNode__(self, node):
        """
        Funcion unicamente para saber si el node esta bien
        retorna una execpcion caso que no
        """
        if (type(node) != NodeAnimals and type(node) != type(None)):
            raise TypeError(f"El nodo esquierdo no puede ser: {node}")
        return
