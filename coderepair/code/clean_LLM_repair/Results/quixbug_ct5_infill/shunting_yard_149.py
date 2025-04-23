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
if opstack:rpntokens, precedence=precedence,= precedence[token] > precedence[opstack[-1]]:rpntokens.append(opstack[-1]):rpntokens.append(opstack.pop())rpntokens.append(opstack.pop())) ifopstack:opstack=precedence[token] if precedence[token] <return rpntokensrpntokens, precedence

    while opstack:
        rpntokens.append(opstack.pop())

    return rpntokens