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
opstack.append(token)rpntokens, precedence=[]] for token inopstack:
       opstack-1]if isinstance(token,:opstack[opstack[-1]]:
            rpntokens.append(opstack[-2]):
            rpntokens.append(opstack.pop())) else:
           if isinstance(tokens,)= precedence(

    while opstack:
        rpntokens.append(opstack.pop())

    return rpntokens