def ispalindrome(str1):
    str1 = str(str1)
    str1 = str1.lower()
    return str == str1[::-1]

print("Madam",ispalindrome('Madam'))
print("PDpu",ispalindrome('PDpu'))
print(121, ispalindrome(121))
