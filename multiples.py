# Print out the multiples of 3 up to 100.
for count in range(1, 100):
    if count % 3 == 0:
        print(count)
    elif count % 5 == 0:
        print(count)
        #has to be an elif. if it was an if you'd get repeats of multiples of 15.
#doing this will still make the first number 3 bc 1 and 2 are not divisible by 3.
        
    #if count % 3 == 0 or count % 5 == 0:

# Now using the same loop, let’s see if we can print out the multiples of 5 too