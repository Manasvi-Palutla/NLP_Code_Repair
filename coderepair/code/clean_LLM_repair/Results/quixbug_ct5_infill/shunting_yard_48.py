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
opstack.append(token): return rpntokensif isinstance(rpntokens, list): return=opstack :) : return=(opstack[0])

.) if isinstance) :if isinstance(rpntokens[0] ==(rpntokens[1] ==11 ] = precedence [[) else :==[ ]op

    while opstack:
        rpntokens.append(opstack.pop())

    return rpntokens