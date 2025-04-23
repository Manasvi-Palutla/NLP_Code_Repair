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
opstack.append(token)opstack:
        rpntokens.append(opstack[-1])

   opstack.pop())

   rpntokens):
UIDS =(opstack) :] =[ 1]] else:

    while opstack:
        rpntokens.append(opstack.pop())

    return rpntokens