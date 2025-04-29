f = open("C:\\Users\\Francisco Mambirisse\\Desktop\\prroject designer\\Book1.csv","r")
content = f.readlines()
d = {}
for l in content:
    rlno,nm,cp2,m2,p = l.split(",")
    d[rlno] = [nm,cp2,m2,p]
    print(rlno,nm,cp2,m2,p)
f.close()
print(d)
