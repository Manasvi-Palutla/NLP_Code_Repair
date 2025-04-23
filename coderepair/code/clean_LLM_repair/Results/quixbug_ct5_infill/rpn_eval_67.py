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
                token+breturn op(symbol, a, b)=stack.pop()

stack.append( tokens.pop())): returnstack.pop()[:-1] #printstack.pop()stack.pop()if len(stack): #print "Stack of= stack.pop()a.pop() #print "Stack ofstack.pop()

   . pop()

            )

    return stack.pop()