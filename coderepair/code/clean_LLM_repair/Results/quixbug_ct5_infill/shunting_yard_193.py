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
opstack.append(token)=,=,'-'if isinstance(tokens[0], int):
            rpntokens.append(tokens[0]rpntokens.append(token):(tokens[0]):
           rpntokens.append(tokens[1])
IUMrpntokens.append(tokens[1] - 1)
           (tokens[0],opstack

    while opstack:
        rpntokens.append(opstack.pop())

    return rpntokens