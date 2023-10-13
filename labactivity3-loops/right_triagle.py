#Assigning var
num = []
x = 0
y = 1

while x < 5:
    num.append(y) 
    for _ in num:
        print(_, end=" ") #prints value and space
    print("") #creates new line
    y += 1
    x += 1 # stops while loop