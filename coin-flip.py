import random

# Let's simulate flipping 100 coins and ouput the results.
heads = 0
tails = 0
for flip in range(100): # range(0, 100, 1) # range(0, 100) if you don't specify it will start at 0 then go to 100. could then be (50, 100) and it'll start at 50 and go to 100.
    coin = random.randint(1, 2)
    if (coin ==1):
        print("heads")
        heads += 1 #heads = heads + 1 #rees like the shorter way of writing it.
    else:
        print("tails")
        tails += 1

print(f"After 100 flips, we got {heads} heads and {tails} tails")

# Now, let's keep count of how many heads and tails we flipped.