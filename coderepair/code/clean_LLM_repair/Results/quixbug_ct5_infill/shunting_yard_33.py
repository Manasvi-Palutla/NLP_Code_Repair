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
opstack.append(token)rpntokens1: return rpntokens if1 ]1 ]opstack [ - 1ifopstack>= precedence[token] <=rpntokens.pop())

    if opstack:1 ]opstack.pop()

    else:
Opened rpntokens.append(opstack.pop())opstack.pop()
Opened rpntokens

    while opstack:
        rpntokens.append(opstack.pop())

    return rpntokens