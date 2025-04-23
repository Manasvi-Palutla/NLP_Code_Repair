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
opstack.append(token)opstack{0}for token:toks.pop(0):toks.pop(0):toks.pop(0)toks.pop()toks.pop() toks[if isinstance(toks[0], int):toks[1]toks[0]toks[1] ==toks[2] == toks[3]

    while opstack:
        rpntokens.append(opstack.pop())

    return rpntokens