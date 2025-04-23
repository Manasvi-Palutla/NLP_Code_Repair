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
opstack.append(token)= [ ]return rpntokens=in precedence:opstack [opstack[opstack[-1]] >= precedence[token]opstack.append(token)

XSD ifopstack:
Taxonomy rpntokens.append(opstack[-1]]rpntokens.append(opstack.pop())
Terminology return rpntokens

    while opstack:
        rpntokens.append(opstack.pop())

    return rpntokens