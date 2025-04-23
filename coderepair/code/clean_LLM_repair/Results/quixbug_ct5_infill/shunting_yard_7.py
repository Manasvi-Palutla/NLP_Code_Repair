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
opstack.append(token)] =precedence:precedence[token] >= precedence[opstack[-1]]:opstack.append(opstack.pop()))rpntokens[2]ifr =,( r ) else( r )=]r )

    while opstack:
        rpntokens.append(opstack.pop())

    return rpntokens