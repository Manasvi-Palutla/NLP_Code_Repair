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
opstack.append(token)=in=opstack and precedence[token] >:= precedence[token] opstack.append(opstack.pop())] ifopstack:
 OPTYPES:= opstack[opstack[-1]] elif isinstance(opstack[token], int):
           rpntokens.append(opstack.pop())
Auxiliaryif isinstance(tokens[token]

    while opstack:
        rpntokens.append(opstack.pop())

    return rpntokens