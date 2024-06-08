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
        node1 = NodeAnimals(animal=self.animal)
        node2 = NodeAnimals(animal=animal)
        self.animal = ""
        self.pergunta = pregunta
        self.respA = ""
        self.__validarNode__(node1)
        self.__validarNode__(node2)
        if(resp.lower() == "si"):
            self.resp1 = node2
            self.resp2 = node1
        elif (resp.lower() == "no"):
            self.resp2 = node2
            self.resp1 = node1
        else:
            print("Esa respuesta es invalida")

    def preguntar(self):
        if (self.pergunta != ""):
            print(self.pergunta)
            resp = input()
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
        else:
            print(f"Es un: {self.animal}?")
            resp = input()
            if (resp.lower() == "no"):
                if (self.resp2 is not None):
                    self.preguntar()
                    return
                self.adicionar()
                return
            print("Voy un genio, no?")

    def __validarNode__(self, node):
        """
        Funcion unicamente para saber si el node esta bien
        retorna una execpcion caso que no
        """
        if (type(node) != NodeAnimals and type(node) != type(None)):
            raise TypeError(f"El nodo esquierdo no puede ser: {node}")
        return
