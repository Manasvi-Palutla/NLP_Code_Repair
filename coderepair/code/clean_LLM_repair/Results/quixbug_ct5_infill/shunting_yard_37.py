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
opstack.append(token)return rpntokens=== [ ] #=if len(rpntokens):r =[] r_all_tokens ={ } for token inr_all_tokens) if isinstance ( token. appendreturnr_all_tokens :

    while opstack:
        rpntokens.append(opstack.pop())

    return rpntokens