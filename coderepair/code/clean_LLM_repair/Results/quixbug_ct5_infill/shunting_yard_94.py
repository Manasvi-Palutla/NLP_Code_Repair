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
opstack.append(token)[if isinstance(rpntokens[0], int):
           rpntokens[0].split( '/'))[0] else:
rpntokens== [ ]

    while opstack:
        rpntokens.append(opstack.pop())

    return rpntokens