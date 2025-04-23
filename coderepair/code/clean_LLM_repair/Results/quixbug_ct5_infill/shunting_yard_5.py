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
opstack.append(token)rpntokens if isinstance(rpntokens, int):if isinstance(rpntokens[0], int):
            rpntokens.append(rpntokens[0]rpntokens.append(rpntokens[1] )#for token in#for token in rpntokens:rpntokens.append(opstack.pop())#print(rpntokens[0] ) #

    while opstack:
        rpntokens.append(opstack.pop())

    return rpntokens