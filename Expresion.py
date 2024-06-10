import sympy as sp

class ExpressionTree:
    def __init__(self, expression):
        self.expression = expression

    def calcular(self):
        return self._evaluate(self.expression)

    def _evaluate(self, expr):
        expr = expr.replace(' ', '')
        if '(' in expr:
            # Encontrar subexpressão mais interna
            start = expr.rfind('(')
            end = expr.find(')', start)
            inner_expr = expr[start+1:end]
            # Resolver subexpressão
            inner_result = str(self._evaluate(inner_expr))
            # Reemplazar subexpressão con su resultado
            expr = expr[:start] + inner_result + expr[end+1:]
            return self._evaluate(expr)
        else:
            return sp.sympify(expr)





