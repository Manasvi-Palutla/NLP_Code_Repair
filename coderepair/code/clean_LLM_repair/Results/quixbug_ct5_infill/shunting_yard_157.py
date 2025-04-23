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
opstack.append(token)for token in)opstackisinstance(token,) else:
           #if isinstance(tokens, int):if isinstance(tokens,rpntokens.append(opstack[-1]):#returnrpntokens.sort()# else:= [] for token inin tokens:"-", ] if isinstance(token, int):
           #rpnt

    while opstack:
        rpntokens.append(opstack.pop())

    return rpntokens