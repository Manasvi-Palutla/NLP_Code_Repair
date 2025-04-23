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
opstack.append(token)[ ] if==ifopstack:
            rpntokens.append(opstack[-1]))rpntokens.append(opstack[-1])rpntokens.append(opstack.pop()) else:cacertrpntokens.append(opstack[-1]))cacert if> precedence[opstack[-1]]:cacert.append(opstack[-

    while opstack:
        rpntokens.append(opstack.pop())

    return rpntokens