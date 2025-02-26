# Day 38
# Custom errors
# Sometimes we raise errors so that something major should not happen
# A good programmer delivers the code with proper custom error raise and exception handling so that the user gets a seamless experience
# We can raise the error by the keyword "raise".

# Example-:
try:
    a = int(input("Enter the value between 1 to 10: "))
    if a < 1 or a > 10:
        raise ValueError("Matlab batane ke baad bhi yahi harkat karni hai na.")
    else:
        if a == 1:
            print(f"Pakad liya saale!! , {a}")
        elif a == 2:
            print(f"Chalo chalo!! , {a}")
        elif a == 3:
            print(f"abe kuch dhang ka soch le")
        elif a >= 4:
            print("Har ek number ke liye guess nahi karne vala")
            print("Baki ka code baad me likhunga!!", f"ha vaise tere a ki value hai {a}")

except ValueError as v:
    print("Abe hushari number ka matlab samjh nahi aata kya udhar naam likhne bola tha kya tereko.", f"{v}")
finally:
    print("Abhi chod jo hua vo hua vapas karte hai.")


# # QUICK QUIZ
# if someone write's "quit" the program should not raise an error.
try:
    b = int(input("Enter the number : "))
    if b=="quit":
        print("Abhi chalna bandh hua hai")
    else:
        raise ValueError("not possibe")
except:
    print("Chlo next karte hai!")
finally:
    for i in range(1,11):
        print(12, f"x {i} = ",12 * (i))