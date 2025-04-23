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
                token)
        = op(op, a,b)}[] return=,:= { }. append)() ) [stack.pop() ) ,stack.pop() ,=b] = stack.pop()return. pop( )stack.pop() , a, bb]) ifbstack.pop()], b)
            )

    return stack.pop()