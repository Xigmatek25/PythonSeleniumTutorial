# for loops

obj = [2, 3, 5, 7, 9]

for i in obj:
    if i <=6:
        print(i)
    else:
        print("larger than 6")
        break


summation = 0
for j in range(1, 6):
    summation = summation + j
print(summation)

print("----------------------------------------")
#(1, 10 ,3) -> (1, 10) = will print 1 to 9; (, 3) -> will add 3 from previous iterations and print only those in range
for k in range(1, 10, 3):
    print(k) #1 4 7
