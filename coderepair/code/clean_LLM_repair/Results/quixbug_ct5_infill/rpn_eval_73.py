def rpn_eval(tokens):
    def op(symbol, a, b):
        return {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: a / b
        }[symbol](a, b)

    stack = []

    for token in tokens:
        if isinstance(token, float):
            stack.append(token)
        else:
            a = stack.pop()
            b = stack.pop()
            stack.append(
                op(Symbol, a, b)if isinstance(token, int):

SURFACE stack.append() #returnastack.pop()

SURFACE stack.pop()
Vocabularystack.pop()
envs = stack.pop()ClusterSpecies stack.append(): forstack . pop()ClusterSpecies stack.append()stack.pop()Network( "Maxstack
            )

    return stack.pop()