from Node import Node
from NodeAnimals import NodeAnimals
from Fibonacci import Fibonacci
import os
import platform
from Expresion import ExpressionTree

"""
Autor@: Juan Manoel Miranda Gómez
Materia: Matematicas Discretas
Instituicion: Universidad de Caldas
Maestr@: 
"""


def clear_screen():
    """
    Codigo generado con ChatGPT
    esa funcion solo sirve para limpar la pantalla
    """
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')


clear_screen()


tree = None
menu = """1. Ingresar nuevo elemento    4. Mostrar en preOrden
2. Buscar Elmento             5. Mostrar en posOrden
3. Mostrar en inOrden         6. Salir
"""

print("Deseas crear un arbole? (Si/No)")
resp = input()
if (resp.lower() == "si"):
    print("Ingrese el valor inicial")
    val = int(input())
    tree = Node(val)
    clear_screen()
    while (resp.lower() != "6"):
        print(menu)
        resp = input()

        if (resp == "1"):
            print("Cuantos valores vas ingresar?")
            n = int(input())
            for i in range(n):
                print(f"ingrese el valor {i+1}")
                val = int(input())
                val = Node(val).val
                tree.adicionarVal(val)
            clear_screen()
            print("Valor(es) ingresado(s) con sucesso")
            print("El arbole es: ")
            print(f"In Orden: {tree.inOrden()}")
            print(f"Pre Orden: {tree.preOrden()}")
            print(f"Pos Orden: {tree.posOrden()}")

        elif (resp == "2"):
            print("Que valor estas buscando?")
            val = int(input())
            node = tree.findVal(val)
            clear_screen()
            print("valor encontrado en el arvole")
            print("caracteristicas del nodo: ")
            print(f"Valor: {node.val}")
            print("El subArbole de ese nodo es: ")
            print(f"In Orden: {node.inOrden()}")
            print(f"Pre Orden: {node.preOrden()}")
            print(f"Pos Orden: {node.posOrden()}")

        elif (resp == "3"):
            clear_screen()
            print("In Orden")
            print(tree.inOrden())

        elif (resp == "4"):
            clear_screen()
            print("Pre Orden")
            print(tree.preOrden())

        elif (resp == "5"):
            clear_screen()
            print("Pos Orden")
            print(tree.posOrden())

        elif (resp == "6"):
            clear_screen()
            print("Hasta luego")

        else:
            clear_screen()
            print("Esa opcion no existe")
else:
    print("Quieres que adivine el animal? (si/no)")
    resp = input()
    if (resp.lower() == "si"):
        animalTree = NodeAnimals(
            pergunta = "Estas pensando en un animal?", resp1= NodeAnimals(animal="pajaro"))
        while (resp != "no"):
            animalTree.preguntar()
            print("Quieres jugar de nuevo?")
            resp = input()
    else:
        print("quieres calcular el numero N de fibonacci?")
        resp = input()
        if(resp.lower() == "si"):
            print("ingrese un numero")
            n = input()
            fibo = Fibonacci(n)
            print(f"El numero {n} del fibonacci es: {fibo.calcular()}")
            input()
        else:
            print("Quieres que resulva problemas matematicos?")
            resp =input()
            if(resp.lower()=="si"):
                print("ingrese a expresion")
                exp_tree = ExpressionTree(input())
                result = exp_tree.evaluate()
                print(f"Resultado: {result}")
                input()


clear_screen()
print("Hasta luego")
