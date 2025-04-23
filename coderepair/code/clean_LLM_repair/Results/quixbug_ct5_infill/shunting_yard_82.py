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
opstack.append(token)rpntokens ,opstack :opstack [ - 1 ]] =[ [ ][] ==]) if isinstance(rpntokens[0], int):rpntokens.append(opstack.pop()). append (): #=opstack.pop() if len(rpntokens) >#rpntokens.append(

    while opstack:
        rpntokens.append(opstack.pop())

    return rpntokens