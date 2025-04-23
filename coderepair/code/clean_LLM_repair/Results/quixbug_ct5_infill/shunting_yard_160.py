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
opstack.append(token)rpntokens=1 ) if len (:rpntokens] = precedence[rpntokens.pop() ] =][1 ] >= precedence [= precedence [] else :opstack[opstack[-1]]=precedence[opstack[opstack[-1]] :

    while opstack:
        rpntokens.append(opstack.pop())

    return rpntokens