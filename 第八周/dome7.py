def equality(num1,num2):
    if len(num1)>len(num2):
        if num1[:len(num2)]==num2:
            return equality(num1[len(num2):],num2)
        else:
            if num1[0]>num2[0]:
                return True
            elif num1[0]<num2[0]:
                return False
            else:
                return equality(num1[1:],num2[1:])
    elif num1==num2:
        return True   
    else:
        if num2[:len(num1)]==num1:
            return  equality(num1,num2[len(num1):])
        else:
            if num1[0]>num2[0]:
                return True
            elif num1[0]<num2[0]:
                return False
            else:
                return equality(num1[1:],num2[1:])
def max_value(ls):
    max_val=''
    while len(ls):
        better_val=ls[0]
        for i in range(1,len(ls)):
            if ls[i][0]>better_val[0]:
                better_val=ls[i]
            elif ls[i][0]<better_val[0]:
                continue
            else:
                if equality(ls[i][1:],better_val[1:]):
                    better_val=ls[i]
        ls.remove(better_val)
        max_val+=better_val
    return max_val
ls=['112','113']
print(max_value(ls))

        
                    
                
    
