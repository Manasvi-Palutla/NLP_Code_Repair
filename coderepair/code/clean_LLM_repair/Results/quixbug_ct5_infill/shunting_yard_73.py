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
opstack.append(token)(]= precedence[rpntokens.pop()]:
            if len(rpntokens)>if= precedence[rpntokens.pop()],= precedence[rpntokens.pop()]rpntokens.pop()if"-"] >= precedence[rpntokens.pop()]else:
           opstack[-1] >= precedence[opstack[-

    while opstack:
        rpntokens.append(opstack.pop())

    return rpntokens