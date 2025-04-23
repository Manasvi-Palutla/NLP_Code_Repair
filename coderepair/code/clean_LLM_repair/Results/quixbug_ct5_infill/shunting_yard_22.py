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
if opstack:return rpntokens opstackrpntokens=rpntokens.append(opstack.pop())

   = []
ology= [ ] for= [ ]#=[]for token in tokens:if isinstance[ token ] ==[ token ] == precedence1 ] == precedenceopstack[opstack[-1]] == precedence[token]opstack[

    while opstack:
        rpntokens.append(opstack.pop())

    return rpntokens