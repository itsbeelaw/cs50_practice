def main ():
    name, house = get_student()
    print(f"{name} from {house}")

def get_student():
    name = input("What shall we call you?").strip()
    house = input("And your house? ")
    print("hmmm I see")
    return name, house

if __name__ == "__main__":
    main()