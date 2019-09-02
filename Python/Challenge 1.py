# Challenge 1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

# Create result variable
res = 0

# For Loop 
for i in range(1000):
    #check div by 3 or 5
    if i % 3 == 0 or i % 5 == 0:
        
        #add to result
        res += i

        #print
        print(res)

# Answer is 233,168
