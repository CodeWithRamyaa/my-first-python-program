number = int(input("Enter a number: "))

# Check positive, negative, or zero
if number > 0:
    print("Positive number")
elif number < 0:
    print("Negative number")
else:
    print("Zero")

# Check even or odd
if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# Check prime or not prime
if number < 2:
    print("Not prime")
else:
    is_prime = True

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime number")
    else:
        print("Not prime")
