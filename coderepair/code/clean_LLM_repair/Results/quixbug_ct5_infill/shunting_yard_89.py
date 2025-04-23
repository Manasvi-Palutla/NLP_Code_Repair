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
opstack.append(token)=] )else:
Electronicrpntokens.append(rpntokens[0])
AudienceToken=( 'Harmonic' , 'Rk' ,=if (, 'Harmonic' , 'Rk') else :=if precedence[token] <= precedence[opstack[-1]]:rpntokens.append(opstack

    while opstack:
        rpntokens.append(opstack.pop())

    return rpntokens