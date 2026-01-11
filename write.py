#read the file and store all the lines in list
#reverse the list
#write the list back to the file

with open('test.txt', 'r') as reader:

    lines = reader.readlines()
    #lines.reverse()
    with open('test.txt', 'w') as writer:
        for line in reversed(lines):
            writer.write(line)




