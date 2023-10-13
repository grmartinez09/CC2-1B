# Assigning variables
input_num = int(input("Input: "))
sum = 0
formula_list = []

# Formula
while len(formula_list) < input_num:
    for i in range(1, input_num+1):
        formula_list.append(i) 
print("Formula:", "+".join(map(str, formula_list))) #nesting of formula and formula list to print summation solution/expression

# Summation
for i in range(1, input_num+1):
    sum += i #adding values for each number up to input number
print("Summation:", sum) #printing sum of all numbers up to input