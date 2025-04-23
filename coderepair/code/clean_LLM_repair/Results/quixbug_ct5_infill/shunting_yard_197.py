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
opstack.append(token)rpntokens =rpntokensrpntokens:return'+' if isinstance(token, int):

if isinstance(token, int):
           rpntokens.append(token)
Ambientrpntokens.append(token)
Ambient rpntokens.append(opstack[-1]]=opstack[-2]rpntokens.pop()
Ambient if len

    while opstack:
        rpntokens.append(opstack.pop())

    return rpntokens