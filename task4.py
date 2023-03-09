# Here I am asking the user to input a integer and saving it in a variable called user_num
user_num = int(input("Please enter any whole number\n : "))

# Here I am using the "%" module operator with the "==" equel operator to determin if the number that the user inputted is divisible by 2 and 5, 2 or 5 or neither of them.
if user_num % 2 == 0 and user_num % 5 == 0:
    print("Your number is divisible by 2 and 5.")
elif user_num % 2 == 0:
    print("Your number is divisible by 2.")
elif user_num % 5 == 0:
    print("Your number is divisible by 5.")
else:
    print("Your number is not divisible by 2 or 5.")