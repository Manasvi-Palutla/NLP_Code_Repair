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
                token)op(op, a, b)op(op, a, b)op(op,return'/'):astack.append( a)stack.append(stack.pop())return 0.0stack.pop()KNP=stack.pop()KNPelse:knp_rpn_eval(stack):KNP_RPN_EVAL(stack):KNP_RPN_E
            )

    return stack.pop()