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
opstack.append(token),= [ ]=+ 1+ 1 ) #==for token in rpntokens) if isinstanceopstack[token] < precedence[token]. append () else :=) if isinstance (= ( 'p' , 'p')"p" ][ token ].] =:'*''

    while opstack:
        rpntokens.append(opstack.pop())

    return rpntokens