def fun(a):
    list=[]
    for x in range (a,0,-1):
        list.append(x)
    return list
print(fun(10))

def print_and_return(list):
   print(list[0])  
   return list[1]

print(print_and_return([1,2]))

def first_plus_length(list):
    
    return(list[0]+len(list))
print(first_plus_length([1,2,3,4,5]))

def values_greater_than_second(list):
    newlist=[]
    if len(list)<2:
        return False
    else :
        for x in range(0,len(list),1):
            if list[x]>2:
                newlist.append(list[x])
    return newlist
print(values_greater_than_second([5,2,3,2,1,4]))

def length_and_value(x,y):
    list=[]
    for i in range(x):
        list.append(y)
    return list
print(length_and_value(5,7))

