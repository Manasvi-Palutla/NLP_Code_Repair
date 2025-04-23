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
opstack.append(token)== len(rpntokens) forinrpntokens :[ token ][in token ifopstackif len ( tokens ):(opstack.pop()) else:Opstack.append(opstack.pop()) ifopstack):Opstack.append(token)OpStack.append(opstack.pop()opstack.pop())opstack.

    while opstack:
        rpntokens.append(opstack.pop())

    return rpntokens