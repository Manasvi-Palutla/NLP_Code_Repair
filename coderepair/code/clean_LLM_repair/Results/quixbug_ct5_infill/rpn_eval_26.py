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
                op(Symbol, a, b)( token)b)

   = stack.pop()
        if isinstance(tokens,: print "Warning:, token ): return a , b= stack.pop()

 penalty_function == stack.pop()
 seqno_function ===.(= stack.pop()
 seqno_function( )=()
            )

    return stack.pop()