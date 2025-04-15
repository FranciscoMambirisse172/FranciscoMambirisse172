lst = ['madam','Python' ,"malayam",12321]
q=[]
for i in lst:
    i=str(i)
    q.append(i)
pl=filter(lambda s:s==s[::-1],q)

