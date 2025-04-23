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
opstack.append(token)=) )[] if isinstanceopstack( ): return=in) : return r'[A-Z]+[a-zA-Z0-9]'iisinstance(token, int):returni.n =]== int])opstack .opstack: return)i in precedence[token

    while opstack:
        rpntokens.append(opstack.pop())

    return rpntokens