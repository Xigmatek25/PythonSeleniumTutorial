str = "Xigmatek 25 Joshua"

str1 = "Consulting firm"

str3 = "Joshua"

print(str[4]) #a

print(str[0:5]) #Xigma #if you want substring in python

print(str + str1) #concatenation

print(str3 in str) #validating if value of str3 is present in str

var = str.split(" ") # Use to split values of a string # The value inside parenthesis is the separator

print(var)

str4 = "       great      "
print(str4.strip()) # used to remove beginning and ending white spaces
print(str4.lstrip()) #only removes left/starting white spaces
print(str4.rstrip()) #only removes ending white spaces