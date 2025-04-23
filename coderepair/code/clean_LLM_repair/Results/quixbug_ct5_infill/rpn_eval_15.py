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
                (a+b)%)stack.pop()] returnstack.pop()

stack.pop()
 NoSuchAlgorithmException stack.append(stack.pop())

 penaltya, b) return#(1,)stack.pop()returnstack.pop()
           a, b)[ "x"], "x"],= stack.pop()
           b, "
            )

    return stack.pop()