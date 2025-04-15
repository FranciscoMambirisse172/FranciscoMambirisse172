def count_lower_upper(str):
    alpha = {'u':0, '1':0}
    
    for x in str:
        if  x.isupper(x) == True:
            alpha['u'] +=1
            
        elif x.islower(x) == True:
            alpha ['1'] +=1
    return alpha



str= input("Enter the string:")
print(count_lower_upper(str))
