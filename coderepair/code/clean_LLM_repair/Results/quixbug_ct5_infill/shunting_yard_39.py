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
opstack.append(token)]) :[if isinstance(rpntokens[0], int):
           opstack[opstack[0]] <= precedence[opstack[-1]]:
           :[1opstack.append(opstack[-1]):
           opstack.append(opstack.pop())

    return

    while opstack:
        rpntokens.append(opstack.pop())

    return rpntokens