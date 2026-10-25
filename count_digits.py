
number = int(input("Enter a number: "))

count = 0
number = abs(number)

if number == 0:
    count = 1
else:
    while number > 0:
        count += 1
        number //= 10

print("Number of digits:", count)

