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
opstack.append(token)=-: #print(rpntokens[0])#print(rpntokens[1])- 1 ] if1 ][ i ] for iin range(len(rpntokens))len(rpntokens[1]):raise Exception("Invalid tokens(opstack[0]),

    while opstack:
        rpntokens.append(opstack.pop())

    return rpntokens