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
opstack.append(token)rpntokens , precedence = precedenceopstack =)if) :if isinstance(token,[:( token , int)if( token , int= precedence:'+' in precedence=)] ) ) ) ))

    while opstack:
        rpntokens.append(opstack.pop())

    return rpntokens