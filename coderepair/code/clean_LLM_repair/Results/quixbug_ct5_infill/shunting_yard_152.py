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
opstack.append(token)('+''-'if isinstance(token, int):
           rpntokens.pop()) #return rpntokens, precedence[rpntokens[-1]]#if len(rpntokens) < (rpntokens[-1]1]rpntokens[0] opstack.pop()rpntokens.append(opstack.pop())rpntokens[1

    while opstack:
        rpntokens.append(opstack.pop())

    return rpntokens