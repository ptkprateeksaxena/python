# how to read a file in python

file = open("prateek.txt")  #open is used to open a file
print(file.read()) #read is used to read the file
file.close()  #close is used to close the open file

#add a content in file

# file2 = open("prateek.txt","a")  # a is used when we have to append in the file
# file2.write(" Saxena")
# file2.close()

file2 = open("prateek1.txt","w")  # w is used when we have to write in the file and if file is not exit then it will create it
file2.write(" Saxena")
file2.close()

file2 = open("prateek1.txt")
print(file2.read())
file2.close()

#reading the file from different location

file3 = open('../21oct/sample_file.txt')
print(file3.read())
file3.close()