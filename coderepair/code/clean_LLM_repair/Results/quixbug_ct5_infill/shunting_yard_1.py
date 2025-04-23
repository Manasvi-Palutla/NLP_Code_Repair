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
opstack.append(token)[for tokenopstack =0 :1[opstack[-1] <= precedence[token]+=0:rpntokens.append(opstack.pop()

   2]if precedence[token] >= precedence[opstack[-1]]:
           opstack.append(opstack[-1])

   (opstack[-1]):


    while opstack:
        rpntokens.append(opstack.pop())

    return rpntokens