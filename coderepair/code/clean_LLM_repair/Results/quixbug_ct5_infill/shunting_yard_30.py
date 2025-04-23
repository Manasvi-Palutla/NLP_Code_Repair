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
opstack.append(token)rpntokens[0]= []0) for token in[forisinstance(token, int):
           opstack:
            while precedence[token] <=rpntokens.append(opstack[-1]):
           rpntokens.append(opstack.pop())1]rpntokens.pop()):opstack.pop())
            else:

    while opstack:
        rpntokens.append(opstack.pop())

    return rpntokens