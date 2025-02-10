# Day 15
# import modules(built-in)
import time

timestamp = time.strftime('%H:%M:%S')
print(timestamp)

# logic
if timestamp > "12:00:00":
    print("Good Afternoon!")
    print("Have a nice afternoon")
elif timestamp > "16:00:00":
    print("Good Evening!")
    print("Exercise time!!")
elif timestamp > "20:00:00":
    print("Good Night!")
    print("Its a rest time")
elif timestamp > "5:00:00":
    print("Good Morning sir!!")
    print("May you enjoy your day")
else:
    print("WELL TIME ERROR IS A COMIC THING!")

# checking everything is good!
print("meeting is scheduled after 1 hr after current time",timestamp,"don't be late")