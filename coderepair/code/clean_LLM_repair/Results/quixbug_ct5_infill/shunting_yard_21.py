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
opstack.append(token)opstack:)

for token in)in precedence:
IFF neat =if noun <=== 0:rpntokens.append(opstack[-1]= precedence[token][noun]rpntokens.extend(rpntokens[-1]):returnopstack.append(noun)= precedence[token]

    while opstack:
        rpntokens.append(opstack.pop())

    return rpntokens