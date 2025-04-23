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
break=. split ( '|'if isinstance(token,ifisinstance(token,[token] >= precedence[opstack[-1]]:split(token)rpntokens.append(opstack.pop()) else:split(token)for token insplit(token):split=split(token) elif(

    while opstack:
        rpntokens.append(opstack.pop())

    return rpntokens