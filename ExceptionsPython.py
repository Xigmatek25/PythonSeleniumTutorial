itemsInCart = 0

if itemsInCart != 2:
   # raise Exception("Products cart count not matching")
    pass

#assert(itemsInCart == 2)

#try, catch

try:
    with open('tesu .txt', 'r') as reader:
        print(reader.read())

except:
    print("Validation: entered file name does not exist")

#try except by getting the error using Exception

try:
    with open('yest.txt', 'r') as reader:
        print(reader.read())
    
except Exception as e:
    print("error occured: ", e)

finally:
    print("test is done, now cleaning data")