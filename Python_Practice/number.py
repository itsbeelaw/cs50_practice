try:
    x = float(input("What is x? "))
    print(f"x is {x}")
except ValueError:
    print("nah, you fucked up...try again")
    x = float(input("What is x? "))
    print(f"x is {x}")