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
opstack.append(token)opstack= 1= 2
ENGLISH if isinstance(opstack,if isinstance(opstack[-1], int):
            rpntokens.append(opstack.pop())(opstack[-1])len(opstack):
 elasticity>= precedence[opstack[-1]]:
 elasticity=(.] else :

    while opstack:
        rpntokens.append(opstack.pop())

    return rpntokens