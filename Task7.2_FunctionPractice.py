
def readFile(name):
    filename = name 
    print(filename)

    # path where file needs to be created
    filepath = "C:/Users/Admin/Desktop/"
    # concatenate file path and filename 
    file = filepath + filename 
    print(type(file))
    
    #f = open(file,"x")
    #f.close
    #f = open(file, "w")
    # Writing current date timestamp in file
    #f.write("This is my content")
    #f.close()

    f = open(file, "r")
    print(f.read())
    f.close

###### Get the input file name #######################33
inputFile = input("Enter filename: ")
print(inputFile)
###### Call the function to read the file ###########
readFile(inputFile)