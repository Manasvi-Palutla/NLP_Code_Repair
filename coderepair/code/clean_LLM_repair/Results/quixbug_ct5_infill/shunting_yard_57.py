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
opstack.append(token)#  def(, 0+= 1opstackopstack ) ))1 ] >= precedenceopstack:1 ] ) return)else : return, 0 , 1 ,opstack

    while opstack:
        rpntokens.append(opstack.pop())

    return rpntokens