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
opstack.append(token)=returnrpntokens =opstack =opstack.append(rpntokens) if isinstance(opstack,if isinstance(opstack, int):ClusterTaxonomyrpntokens.append(opstack.pop()):ClusterTaxonomyrpntokens.append(opstack.pop()):ClusterTaxonomy rpntokens.append(opstack.pop())ClusterTaxonomy if isinstance(opstack,

    while opstack:
        rpntokens.append(opstack.pop())

    return rpntokens