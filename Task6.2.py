data = [10,501,22,37,100,999,87,351]
primeList =[]
countPrimeNos = 0 

for num in data:
    #if num == 1:
     #   print(num, "is not a prime number")
    #elif num > 1:
     # check for factors
     for i in range(2, num):
        if (num % i) == 0:
            flag = True 
            break
        else:
           flag = False 


     if flag == True:
        print(num, "is Not Prime")
     else:
        print(num ," is Prime")
        primeList.append(num)
        countPrimeNos = countPrimeNos +1 
print("List of Prime numbers is" ,primeList)
print("Number of Prime numbers in list is" , countPrimeNos)
   