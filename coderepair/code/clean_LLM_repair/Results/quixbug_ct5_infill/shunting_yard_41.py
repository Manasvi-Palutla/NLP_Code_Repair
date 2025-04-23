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
opstack.append(token)## ifif isinstance(rpntokens[0]if isinstance(rpntokens[0]== len(rpntokens[0]) elserpntokens[1] == len(rpntokens[0]): #for) : returnrpntokens[1] == len(rpntokens[2]) else :rpntokens[2]"-", "-"

    while opstack:
        rpntokens.append(opstack.pop())

    return rpntokens