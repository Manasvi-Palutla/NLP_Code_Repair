def shunting_yard(tokens):
    precedence = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2
    }

    rpntokens = []
    opstack = []
    for token in tokens:
        if isinstance(token, int):
            rpntokens.append(token)
        else:
            while opstack and precedence[token] <= precedence[opstack[-1]]:
                rpntokens.append(opstack.pop())
opstack.append(token)'/'] = precedence[rpntokens.pop()='/'=='/'):
            rpntokens.append(opstack[-1]).append(opstack[-2]).append(opstack[-1])else:'/'= precedence[rpntokens.pop()] + precedence[rpntokens.pop()]rpntokens

    while opstack:
        rpntokens.append(opstack.pop())

    return rpntokens