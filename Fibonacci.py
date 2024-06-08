class Fibonacci():
    def __init__(self,n) -> None:
        self.n = int(n)

    def calcular(self):
        if(self.n == 1 or self.n == 0):
            return self.n
        elif(self.n>1):
            node1 = Fibonacci(self.n-1)
            node2 = Fibonacci(self.n-2)
            return (node1.calcular() + node2.calcular())
        raise ValueError("Valor de n no es valido")
