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
opstack.append(token)rpntokens_to_kd=None==,[, 1 ) for] =) )=rpntokens_to_kd.keys(): # if!=rpntokens_to_kd=[] #isinstance(tokens, int):=() ifisinstance(tok, int):if( tok

    while opstack:
        rpntokens.append(opstack.pop())

    return rpntokens