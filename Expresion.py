class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class ExpressionTree:
    def __init__(self, expression):
        self.expression = expression.replace(" ", "")
        self.root = self.build_tree(self.expression)

    def build_tree(self, expr):
        if expr.isdigit():  # Si la expresión es un número, devuelva un nodo de hoja.
            return TreeNode(int(expr))
        
        # Encuentra la operación de más bajo nivel (fuera de cualquier paréntesis)
        pos, min_priority = -1, float('inf')
        stack = 0  # Para el seguimiento de paréntesis
        for i, char in enumerate(expr):
            if char == '(':
                stack += 1
            elif char == ')':
                stack -= 1
            elif stack == 0:
                priority = self.get_priority(char)
                if priority <= min_priority:
                    min_priority = priority
                    pos = i

        if pos == -1:
            return self.build_tree(expr[1:-1])  # Remover paréntesis externos

        node = TreeNode(expr[pos])
        node.left = self.build_tree(expr[:pos])
        node.right = self.build_tree(expr[pos + 1:])
        return node

    def get_priority(self, operator):
        priorities = {'+': 1, '-': 1, '*': 2, '/': 2}
        return priorities.get(operator, float('inf'))

    def evaluate(self, node=None):
        if node is None:
            node = self.root
        if isinstance(node.value, int):
            return node.value
        left_val = self.evaluate(node.left)
        right_val = self.evaluate(node.right)
        if node.value == '+':
            return left_val + right_val
        elif node.value == '-':
            return left_val - right_val
        elif node.value == '*':
            return left_val * right_val
        elif node.value == '/':
            return left_val / right_val

    def print_tree(self, node=None, level=0, prefix="Root: "):
        if node is None:
            node = self.root
        print(" " * (level * 4) + prefix + str(node.value))
        if node.left:
            self.print_tree(node.left, level + 1, "L--- ")
        if node.right:
            self.print_tree(node.right, level + 1, "R--- ")