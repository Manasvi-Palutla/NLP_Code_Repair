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
opstack.append(token)rpntokensif isinstance(rpntokens, list):if isinstance(rpntokens[0],else:
           rpntokens[1]]=rpntokens[2]]=rpntokens[3]=rpntokens[4] returnopstack:
OpenedSession rpntokens.append(opstack.pop())

    while opstack:
        rpntokens.append(opstack.pop())

    return rpntokens