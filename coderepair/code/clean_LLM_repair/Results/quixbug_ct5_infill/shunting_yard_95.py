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
opstack.append(token)[ ] ifisinstance(token,, int):
            while] <= precedence[rpntokens[opstack[-1]]:
           if isinstance(opstack[-1], int):
           =opstack:=for[[ 0 ] ] if[[ 1 ] == 'n') : ##opstack.pop() return

    while opstack:
        rpntokens.append(opstack.pop())

    return rpntokens