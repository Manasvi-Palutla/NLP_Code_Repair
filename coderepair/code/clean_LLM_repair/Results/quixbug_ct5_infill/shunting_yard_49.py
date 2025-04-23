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
opstack.append(token)rpntokens.join(rpntokens))  defreturntoken= [for tokentoken in rpntokens: if isinstance(token,if isinstance(token, int):iftoken] <= precedence[token]opstack[token]= precedence[token]opstack[-1]]'/' :]

    while opstack:
        rpntokens.append(opstack.pop())

    return rpntokens