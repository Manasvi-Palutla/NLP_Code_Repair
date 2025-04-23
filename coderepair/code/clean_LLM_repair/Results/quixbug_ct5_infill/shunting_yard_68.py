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
if opstack:return"a" else : #a""b""a" else] = 2"c"] =) )"d"= ( "b" ,([] = (]] = ("c" ,[, "c" , "c" )"c" ]]

    while opstack:
        rpntokens.append(opstack.pop())

    return rpntokens