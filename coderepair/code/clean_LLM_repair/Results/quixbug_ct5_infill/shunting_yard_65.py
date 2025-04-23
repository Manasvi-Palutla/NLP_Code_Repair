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
opstack.append(token)= []=while precedence[token] <rpntokens.append(opstack[-1]):
            while precedence[token] <=(opstack[-1])
           rpntokens.append(opstack[-1]):
            whileand precedence[opstack[-1] <= precedence[opstack[-2]]:
           rpntokens.append(opstack.

    while opstack:
        rpntokens.append(opstack.pop())

    return rpntokens