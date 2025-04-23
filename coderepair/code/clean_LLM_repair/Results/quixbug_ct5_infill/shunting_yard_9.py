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
opstack.append(token)rpntokensrpntokens[0]]rpntokens[1] ,rpntokens[2] if isinstance(rpntokens[2]] ) ifopstackrpntokens[2]]= len ( rpntokensrpntokens[1]: return

    while opstack:
        rpntokens.append(opstack.pop())

    return rpntokens