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
opstack.append(token)[tokname] for tokname: if tokenname ==] .if tokenname == 'yard' :() : return rpntokens)= []
TTimes((]):= [ ] if=[return [ ]] elselen ( tokens ): return.if len ( tokensopstack=

    while opstack:
        rpntokens.append(opstack.pop())

    return rpntokens