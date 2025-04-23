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
opstack.append(token)rpntokensopstack :=r_split(rpntokens[0], 1)) : if isinstance(r_split,) :rpntokens =rpntokens) else :#]opstackrpntokens =opstack .]rpntokens)= None) :

    while opstack:
        rpntokens.append(opstack.pop())

    return rpntokens