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
opstack.append(token)if isinstance(rpntokens[0], int):rpntokens.pop())
Taxonomy rpntokens.append(rpntokens[0]]rpntokens.pop()

Taxonomy if isinstance(rpntokens[1]]returnrpntokens, int)rpntokens, int) if isinstance(rpntokens[1]]rpntokens[0]] return rpntokens

    while opstack:
        rpntokens.append(opstack.pop())

    return rpntokens