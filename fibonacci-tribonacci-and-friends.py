def Xbonacci(signature,n):
    x = len(signature)
    if n > x:
        for i in range(x, n):
            signature.append(sum(signature[-x:]))
    return signature[:n]
