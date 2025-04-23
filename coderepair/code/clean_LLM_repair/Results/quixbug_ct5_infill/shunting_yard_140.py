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
opstack.append(token)#isinstance(rpntokens,[ ] for token(Token, int):
MimeType rpntokens.append(token)'+'] < precedence[rpntokens[opstack[-1]]:
MimeType rpntokens.append(opstack[opstack[-1]]):[ tok] for tok inrpntokens.append(tok)rpntokens.append(tok.

    while opstack:
        rpntokens.append(opstack.pop())

    return rpntokens