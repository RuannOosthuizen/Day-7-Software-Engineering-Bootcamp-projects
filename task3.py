
# Here I am asking the user to input their times for each sections of the triathlon, then saving those values in variables called "swim_time", "cycle_time" and "run_time".
swim_time = int(input("Please enter the time taken in the swimming section (in minutes):\n "))
cycle_time = int(input("Please enter the time taken in the cycling section (in minutes):\n "))
run_time = int(input("Please enter the time taken in the running section (in minutes):\n "))

# Here I am simply calculating the final time of the participant using addition.
final_time = (swim_time + cycle_time + run_time)
# Here I am using the the oppropriate operators with the conditions to determin what award the participant should get depending on their total time.
if final_time <= 100:
    print(f"Congratulations! You have finished within the qualifying time with a time of {final_time} minutes.\nYour award is: (Provincial Colours)")
elif final_time > 100 and final_time <= 100 + 5:
    print(f"Congratulations! You have finished within 5 minutes of the qualifying time with a time of {final_time} minutes.\nYour award is: (Provincial Half Colours)")
elif final_time > 100 + 5 and final_time <= 100 + 10:
    print(f"Congratulations! You have finished within 10 minutes of the quelifying time with a time of {final_time} minutes.\nYour award is: (Provincial Scroll)")
else:
    print(f"Congratulations! You have finished with a qualifying time of {final_time} minutes.\nYou do not qualify for a reward.")