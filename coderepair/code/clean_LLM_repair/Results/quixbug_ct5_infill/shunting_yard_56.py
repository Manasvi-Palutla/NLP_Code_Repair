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
else:
           rpntokensisinstance(rpntokens[0], int):rpntokens[1]rpntokens[2] -rpntokens[3] -rpntokens[0]] -rpntokens[2] - rpntokens[3] return

    while opstack:
        rpntokens.append(opstack.pop())

    return rpntokens