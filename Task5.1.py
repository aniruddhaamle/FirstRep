# Input sting is initialised 
input_String = "Guvi Geeks Network Private Limited"
# Initialized the counter to count the vowels to 0
count = 0
# Creating list of vowels 
Vowels_list = ["a" , "e" , "i" , "o" , "u"]
# Comparing the each charactor in input string with charactors in vowel list and if match is found then count is increased 
for i in input_String:
    if i in Vowels_list:
        count = count + 1
#Printing the count of vowels         
print (f"Total number of vowels in the input string is {count}")


# Initialized the counters to count the individual vowels to 0
counta = counte = counti =counto = countu = 0
# Comparing every charactor in input string one by one with each vowel and if match is found then count is increased 
for j in input_String:
    if j == "a":
        counta = counta + 1
    if j == "e":
        counte = counte + 1
    if j == "i":
        counti = counti + 1
    if j == "o":
        counto = counto + 1
    if j == "u":
        countu = countu + 1
#Printing the count of individual vowels     
print(f"Total number of a in the input string is {counta}")
print(f"Total number of e in the input string is {counte}")
print(f"Total number of i in the input string is {counti}")
print(f"Total number of o in the input string is {counto}")
print(f"Total number of u in the input string is {countu}")
    

