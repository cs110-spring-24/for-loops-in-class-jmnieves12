#Print out all the numbers between 1 and 30

Fizz = 0
Buzz = 0
FizzBuzz = 0

for count in range(1, 31):
    if count % 15 == 0: #ORDER MATTERSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
        print("FizzBuzz")
    elif count % 3 == 0:
        print("Fizz")
    elif count % 5 == 0: #writing elif means if the above if is good it'll ignore the elif
        print("Buzz")
    else:
        print(count)
#If the number is a multiple of 3, instead of printing the number, print out “Fizz”

#If the number is a multiple of 5, instead of printing the number, print out “Buzz”

#If the number is a multiple of 15, instead of printing the number, print out “FizzBuzz”