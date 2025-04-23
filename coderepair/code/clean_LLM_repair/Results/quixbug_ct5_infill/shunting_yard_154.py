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
opstack.append(token)fortoksif isinstance (toks[1]:opstack[toks[1]]tokens [ 0 ][ 1 ]token= '-''+/''-' ,'-/' :'+''/''+',1] ) ] if== '-''-','-' , ' ''+' , '-' ,

    while opstack:
        rpntokens.append(opstack.pop())

    return rpntokens