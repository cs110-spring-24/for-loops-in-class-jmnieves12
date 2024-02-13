import random

#Let's simulate rolling the dice 100 times and print out each dice value.
ones = 0
twos = 0
threes = 0
fours = 0
fives = 0
sixes = 0

for roll in range(100):
    roll = random.randint(1,6)
    if roll == 1:
        print("You rolled a one.")
        ones += 1
    elif roll == 2:
        print("You rolled a two.")
        twos = twos + 1
    elif roll == 3:
        print("You rolled a three.")
        threes = threes + 1
    elif roll == 4:
        print("You rolled a four.")
        fours = fours + 1
    elif roll == 5:
        print("You rolled a five.")
        fives = fives + 1
    else:
        print("You rolled a six.")
        sixes = sixes + 1

#You could just use if statements all the way down like I did when I tried writing this, but using elifs and else show your understanding better.

print(f"After 100 rolls, we got {ones} ones, {twos} twos, {threes} threes, {fours} fours, {fives} fives, and {sixes} sixes.")
#Now, let's count how many 1s, 2s, 3s, 4s, 5s, and 6s were rolled