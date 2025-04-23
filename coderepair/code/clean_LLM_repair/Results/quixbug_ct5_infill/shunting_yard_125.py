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
opstack.append(token)rpntokens= [for token inopstack:
IOData if isinstance(token, int):
           if isinstance(tokens,=>= precedence[token] <=opstack.pop())/2+1+1opstack.pop()/2+1+111]=2+1+1*2+1-2*2 else:
           

    while opstack:
        rpntokens.append(opstack.pop())

    return rpntokens