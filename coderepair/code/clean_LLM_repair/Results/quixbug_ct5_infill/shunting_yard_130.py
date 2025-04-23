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
opstack.append(token)= [ ]opstack ) :rpntokens.extend(opstack):opstack:
        if isinstance(token,opstack.pop()

   if isinstance(token,rpntokens.append(opstack.pop()):rpntokens.append(opstack.pop())
IODomsgreturnrpntokens.extend(opstack): return rpntokens

    while opstack:
        rpntokens.append(opstack.pop())

    return rpntokens