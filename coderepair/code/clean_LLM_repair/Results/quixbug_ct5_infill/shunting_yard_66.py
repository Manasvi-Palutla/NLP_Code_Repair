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
opstack.append(token)rpntokens=] if isinstance(rpntokens[0],) if isinstance(rpntokens[1], int):rpntokens[1] if isinstance(rpntokens[2]rpntokens[0] ==return rpntokens[1] if isinstance(rpntokens[1]if isinstance(rpntokens[1]10] elserp

    while opstack:
        rpntokens.append(opstack.pop())

    return rpntokens