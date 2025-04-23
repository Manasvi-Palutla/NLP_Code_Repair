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
                op(symbol, a, b)=a/b)],)) :stack.pop()]= stack.pop()
ENG returnreturn None== 'N' else. pop() :'+'):. append (if len (]= 'N' else :if len ( stack= 'N'[ 'F' ] ) ['-''
            )

    return stack.pop()