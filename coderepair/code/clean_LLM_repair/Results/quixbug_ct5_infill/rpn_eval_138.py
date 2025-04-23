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
                a + bstack.pop()
       = stack.pop()
           :

lang = stack.pop()
langreturn 'C':= a.split('|')[0],('+', '+', '**', '**','-', '/','*', '/','*','*',)stack.pop()+,)'-',
            )

    return stack.pop()