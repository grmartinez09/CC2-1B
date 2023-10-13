#Assigning var
num = [1, 2, 3, 4, 5]
x = 0
y = 4
 
while x < 5:
    for _ in num:
        print(_, end=" ")#prints value and space
    print("")#creates new line
    del num[y] # removes value from list
    y -= 1
    x += 1 # stops loop