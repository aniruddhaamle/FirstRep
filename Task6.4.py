input_number = 1238456784
sum = 0
numTostring = str(input_number) # Convert number to string
print("Entered number is" , numTostring)

strToList = list(numTostring)  # Convert string to list
#print(strToList)
lengthOfList =  len(strToList)  #Calculate length 
#print(lengthOfList)

    # First item of list + Last item of list 
sum = int(strToList[0])+ int(strToList[lengthOfList-1])
print("Sum of first and last digit of integer is" , sum)
