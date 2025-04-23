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
opstack.append(token))rpntokens, precedence=precedence,opstack=opstack,opstack=opstack) returnif isinstance(rpntokens[0], int):
           rpntokens.extend(precedence) if isinstance(rpntokens[1]else:
            rpntokens.append(rpntokens[1])"+"+"+"+"+"+"+"+"+"+"+"+"+"

    while opstack:
        rpntokens.append(opstack.pop())

    return rpntokens