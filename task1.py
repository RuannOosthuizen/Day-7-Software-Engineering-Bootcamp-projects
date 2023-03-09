# Here I am simply declare three variables called num1, num2 and num3 and assigning each variable a number value.
num1 = 5
num2 = 10
num3 = 20

# Here I am using the arithmetic operators "<" and ">" in a if statement to determine which variable is larger.
if num1 > num2:
    print(f"num1 is larger then num2, it having the value of: {num1}.")
else:
    print(f"num2 is larger then num1, it having the value of: {num2}.")

# Here I am using the arithmetic operator "%" in an if statement to determing if the number is odd or even.
if (num1 % 2) == 0:
    print("num1 is an even number.")
else:
    print("num1 is an odd number.")

# Here I am using the "<" and ">" operators in an if statement, to determin which variable is larger then the others to print out the values from largest to smallest order.
if num1 > num2:
    num1,num2 = num2,num1
if num1 > num3:
    num1,num3 = num3,num1
if num2 > num3:
    num2,num3 = num3,num2
print(num3, ">", num2, ">", num1)