def ispangram(str):
    alphaset = 'abcdefghijklmnopqrstuvwxyz'
    str = str.lower()
    a = set-(alphaset)
    s = set(str)
    return a <= s

print(ispangram("The quick brown fox jumps over the lazy dog"))
print(ispangram("Crazy Frederick bought many very exquisite opa"))
print(ispangram("Manan"*7))
    
