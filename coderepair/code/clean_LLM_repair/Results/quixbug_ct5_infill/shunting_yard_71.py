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
opstack.append(token)=[][] = precedence [ tokenopstackopstack.append(token) ifopstackopstack[rpntokens[opstack[-1]]+1]1]opstack[opstack[-1]]+1] opstack.append(opstack[-1]-1) return rpntokens

    while opstack:
        rpntokens.append(opstack.pop())

    return rpntokens