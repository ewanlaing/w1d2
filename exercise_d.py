import pdb
# For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:
even = []
for number in numbers:
    if number % 2 == 0:
        even.append(number)
print(even)

# 2. Print the difference between the largest and smallest value:
l = max(numbers)
s = min(numbers)
x = l - s
print(x)


# 3. Print True if the list contains a 2 next to a 2 somewhere.
num = len(numbers)
for x in range(num):
    if numbers[x] == 2 and numbers[x-1] == 2:
        print(True)
    

# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
#    So [11, 6, 4, 99, 7, 11] would have sum of 22

    


# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5. 

sum = 0
for number in numbers:
    if number == 13:
        continue
    elif number == numbers[numbers.index(13) + 1]:
        continue
    else:
        sum += number
print(sum)
