input_string  = "Guvi Geeks Network Private Limited"
Vowels_list = ["a" , "e" , "i" , "o" , "u"]
for i in input_string:
    if i in Vowels_list:
        input_string = input_string.replace(i, "")
print(input_string)