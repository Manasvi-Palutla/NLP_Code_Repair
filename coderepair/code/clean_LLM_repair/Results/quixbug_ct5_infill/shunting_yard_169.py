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
if opstack:opstack.append(token)opstack )] = precedence [ token] =[ 0 ]] = precedence [ toktok:[ tok ]toktoks_to_use [ toktoks_to_use [tok ] [tok ]tok ]toklen is not Noneif toklentoklen is not None]==opstack

    while opstack:
        rpntokens.append(opstack.pop())

    return rpntokens