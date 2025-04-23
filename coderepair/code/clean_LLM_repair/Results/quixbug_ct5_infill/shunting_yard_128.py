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
opstack.append(token)=if isinstance(rpntokens[0], int):
           isinstance(rpntokens[1]] <= precedence[rpntokens[2]]:
           1]#2]if isinstance(rpntokens[0]= precedence[rpntokens[1]]-precedence[opstack[1]]:opstack=[opstack] # return

    while opstack:
        rpntokens.append(opstack.pop())

    return rpntokens