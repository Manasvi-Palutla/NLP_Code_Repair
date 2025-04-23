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
opstack.append(token)opstack :) :if isinstance(opstack,opstack .) else :rpntokens . appendopstack = [ ]in()] iflen ( precedence )= precedenceif len) :
           opstack.append(opstack[-1]):
           ] <= precedence[opstack[-1]]:
           rpntokens

    while opstack:
        rpntokens.append(opstack.pop())

    return rpntokens