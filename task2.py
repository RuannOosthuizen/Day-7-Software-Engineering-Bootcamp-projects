# Here I am asking the user to input data of the shape of building they are working with (square, rectangular or round), then saving that data in a variable called shape.
answer = input("Please enter the shape of building you are working with? if it's square, rectangular or round.\n : ")
shape = answer.lower()

# Step 1: I use the  if statements to prompt for the appropreiate dimensions depending on what the user inputted.
# Step 2: I then calculate the area of the appropriate shape using the formulas for that perticular shape.
# Step 3: I then print out the final calculated area of the users foundational shape.
if shape == "squere":
    square = float(input("Please enter the lenght of the square:\n ")) 
    area_square = square**2
    print(f"The area of your squere foundation is:\n {area_square}")
elif shape == "rectangular":
    length = float(input("Please enter the length:\n "))
    width = float(input("Please enter the width:\n "))
    area_rectangle =  length * width
    print(f"The area of your rectangle foundation is:\n {area_rectangle}")
elif shape == "round":
    radius = float(input("Please enter the radius:\n "))
    area_round = 3.14 * radius ** 2
    print(f"The area of your round foundation is:\n {area_round}")