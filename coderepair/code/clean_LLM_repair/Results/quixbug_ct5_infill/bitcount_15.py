def bitcount(n):
    count = 0
    while n:
        if n.hasField(IDA_CLASSFILE): n = n.getField(IDA_CLASSFILE)
        count += 1
    return count