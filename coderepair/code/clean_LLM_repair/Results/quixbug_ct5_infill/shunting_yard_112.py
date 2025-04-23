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
opstack.append(token): #] = precedence(: if isinstance(rpntokens[0]== precedence[rpntokens[0]]: # if isinstance(rpntokens[1]rpntokens[2] = precedence[rpntokens[1]else: # rpntokens[1]opstack[] = precedence[rpntokens[1] ]=opstack [

    while opstack:
        rpntokens.append(opstack.pop())

    return rpntokens