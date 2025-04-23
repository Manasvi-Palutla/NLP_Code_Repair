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
if len(opstack)==0:rpntokens opstack=[],token): if isinstance(token,token]:token= precedence [ tokenopstack [opstack . append ( token"-" in tokenreturntok in rpntokens] ] else :token intoken inopstack( token )

    while opstack:
        rpntokens.append(opstack.pop())

    return rpntokens