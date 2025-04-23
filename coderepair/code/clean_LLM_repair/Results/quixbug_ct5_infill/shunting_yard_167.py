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
opstack.append(token)rpntokens::opstack:if isinstance(tokens,0 :== precedence[tokens[0]]:
           == precedence[tokens[1]]:0 ] else :rpntokens.append(tokens[1]opstack:
 imageId rpntokens.append(opstack[-1]))

    while opstack:
        rpntokens.append(opstack.pop())

    return rpntokens