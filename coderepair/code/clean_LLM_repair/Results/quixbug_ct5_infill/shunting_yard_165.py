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
opstack.append(token)rpntokens= []

=) )if opstack[ -: returnr [ 0r+= 1] :if isinstance(r, int):r] =(r]] [ 0],0( len ( r )] ) ]] [ 1 ]r =r =

    while opstack:
        rpntokens.append(opstack.pop())

    return rpntokens