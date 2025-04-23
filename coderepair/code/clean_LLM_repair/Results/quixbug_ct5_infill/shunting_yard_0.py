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
opstack.append(token)= [)==opstack:opstack.append(opstack.pop())if isinstance(opstack, int):
            rpntokens.append(opstack[-1]]else:
           +] + precedence [opstack:
            rpntokens.append(opstack[-1])if isinstance(opstack[0], int):
            rpntokens

    while opstack:
        rpntokens.append(opstack.pop())

    return rpntokens