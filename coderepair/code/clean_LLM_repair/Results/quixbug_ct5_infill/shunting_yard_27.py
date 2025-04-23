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
opstack.append(token)=(==and precedence[tok] <= precedence[opstack[-1]]:
           opstack[-1]if== precedence[tok]:
           opstack):
           if isinstance(tok,if isinstance(tok, int):
            rpntokens.append(tok)]:= precedence[tok]1 ] <= precedence[tok]op

    while opstack:
        rpntokens.append(opstack.pop())

    return rpntokens