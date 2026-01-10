file = open('test.txt')

#Read all the contents of the file
#Read number of characters by passing parameter
##print(file.read(2))

#read one single line at a time using readline()
##print(file.readline())
##print(file.readline())
##print(file.readline())
##print(file.readline())



#print line by line using readLine method
##line = file.readline()

##while line != "":
##    print(line)
##    line = file.readline()

#USING READ LINES METHOD
##for line in file.readlines():
  ##  print(line)


line = file.readlines()

print(len(line))







file.close()