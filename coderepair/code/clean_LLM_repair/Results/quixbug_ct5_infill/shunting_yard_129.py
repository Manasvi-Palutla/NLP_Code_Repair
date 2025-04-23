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
opstack.append(token), precedence =in precedence:( precedence [ tokenopstack andprecedence[opstack[-1]]) if isinstanceif isinstance(token, int):
           [token][token]== precedence[token] else:
           rpntokens.append(token)
Auxiliaryrpntokens.append(opstack[-1]

    while opstack:
        rpntokens.append(opstack.pop())

    return rpntokens