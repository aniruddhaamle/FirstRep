data = [10,501,22,37,100,999,87,351]
evenList =[]
oddList =[]

############## Approach 1 ###############
isEven = lambda a: a%2 ==0
evenList = list(filter(isEven, data))
print(evenList)

isOdd = lambda a: a%2 !=0
oddList = list(filter(isOdd, data))
print(oddList)


################## Approach 2 ##############
for i in data:
    if i % 2 ==0:
        evenList.append(i)
    else:
        oddList.append(i)

print(evenList)
print(oddList)