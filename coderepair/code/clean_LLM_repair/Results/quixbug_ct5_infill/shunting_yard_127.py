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
opstack.append(token)=- 1 ) else:
           :if isinstance(tokens[0], int):
           =if isinstance(tokens[0], int):rpntokens.append(tokens[0]))

    elif isinstance(tokens[0], int):
           else:
           rpntokens.append(tokens[0])
           [tok]'.' ) else#

    while opstack:
        rpntokens.append(opstack.pop())

    return rpntokens