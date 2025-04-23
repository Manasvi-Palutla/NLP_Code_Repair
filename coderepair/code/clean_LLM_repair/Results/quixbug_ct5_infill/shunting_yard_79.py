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
if notopstack:]forfor= 1= 1]opstack . appendwhile[)while precedence[token] <= precedence[opstack[-1]]:opstack . poprpntokens.append(opstack.pop()) if isinstance(opstack[0], int):
           rpntokens.append(opstack.pop()) if isinstance(opstack[1]] <= precedence

    while opstack:
        rpntokens.append(opstack.pop())

    return rpntokens