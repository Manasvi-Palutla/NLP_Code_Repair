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
opstack.append(token)# print(rpntokens)rpntokens=[ ]== '-':
           if isinstance(opstack,returnrpntokens[0] != '-')rpntokens.append(opstack[-1] == '-':#if isinstance(rpntokens[0]:returnrpntokens[1]rpntokens[0]!=='-':return'/'

    while opstack:
        rpntokens.append(opstack.pop())

    return rpntokens