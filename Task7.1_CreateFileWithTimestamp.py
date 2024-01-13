####### Program to create a file with name as current timestamp and add current timestamp in the file
import datetime
# Get the current date time
ct = datetime.datetime.now()
print(ct)
# Convert date time into string
strct = str(ct)
print(strct)
# Replace : with - so that we can create a folder with the name
strct = strct.replace(":", "-")
print(strct)
# path where file needs to be created
filepath = "C:/Users/Admin/Desktop/"
# concatenate file path and filename and .txt extension
filename = filepath + strct +".txt"
print(filename)
f = open(filename,"x")
f.close
f = open(filename, "w")
# Writing current date timestamp in file
f.write(strct)
f.close()
