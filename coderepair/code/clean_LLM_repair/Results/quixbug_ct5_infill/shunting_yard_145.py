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
opstack.append(token)=opstack.pop()
Auxiliary rpntokens.append(opstack.pop())==opstack[ - 1 ]rpntokens . pop:opstackforin precedencefor token inif isinstance ( token( token [ - 1[ - 1:if token:] if token in precedence]split (] else

    while opstack:
        rpntokens.append(opstack.pop())

    return rpntokens