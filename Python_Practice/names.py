name = input("What's Your name? ")

file = open("names.txt", "w")
file.write(f"{name}\n")
file.close()

with open("names.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print("hello,", line)