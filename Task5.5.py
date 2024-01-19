#input_string  = "MADAM"
input_string  = "ABCD"
reverse_string =""

for j in (input_string):
    #print(j)
    reverse_string =j +  reverse_string

print(reverse_string)


if input_string==reverse_string:
    print("Palindrome")
    
else:
    print("Not Paindrome")



