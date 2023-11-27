import random
import statistics

name = input("What's your name? ")
print("hello, " + name)

number = random.randint(1,15)
print(number)

hand = random.choice(["rock", "paper", "scissors"])
print(hand)

coin = random.choice(["head", "tails"])
print(coin)

print(statistics.median([1, 4, 80, 95]))