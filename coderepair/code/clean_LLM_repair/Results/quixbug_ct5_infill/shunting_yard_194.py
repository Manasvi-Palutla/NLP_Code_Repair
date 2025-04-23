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
opstack.append(token)rpntokens #rpntokensopstack =]if isinstance(rpntokens[0],isinstance(rpntokens[1], int):COKTrpntokens[1]else:COKTrpntokens.append(opstack[-1])COKTCOKTCOKTCOK TCOKTCOK TCOKTCOKTO

    while opstack:
        rpntokens.append(opstack.pop())

    return rpntokens