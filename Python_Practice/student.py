def main():

    name = get_name()
    house = get_house()
    birthday = get_birthday()
    print(f"{name} was born on {birthday} from the wonder house of {house}")

def get_name():
    name = input("Welcome...what should we call you? : ")
    print(f"Hello, {name}")
    return name

def get_house():
    house = input("If you know it, state your House: ")
    print(f"Glorious, you just saved us some time")
    return house

def get_birthday():
    birthday = input("Excellent...What is your birthday?: ")
    print(f"Oh cool, so is mine!")
    return birthday

if __name__ == "__main__":
    main()