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

 taxonomy = op(op,a,b) (((Op(Op(Op(Op(Op(Op(Op(Op(Op(Op(Op(Op(Op(Op))))))))),((Op(Op(Op(Op(Op(Op(Op(Op(Op(Op(Op(Op(Op)))))))))))))))))))))))))))))= stack.pop()

            )

    return stack.pop()