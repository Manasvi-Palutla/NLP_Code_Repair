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
opstack.append(token)]: if(opstack, precedence[token] <= precedence[opstack[-1]]):
Taxonomyrpntokens.append(opstack[-1]):
Taxonomyelse:
Taxonomyopstack, precedence[token]if len(rpntokens):
Taxonomy

    while opstack:
        rpntokens.append(opstack.pop())

    return rpntokens