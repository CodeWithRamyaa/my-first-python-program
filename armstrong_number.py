
number = int(input("Enter a number: "))

if number < 0:
    print("Not an Armstrong number")
else:
    digits = str(number)
    power = len(digits)

    total = sum(int(digit) ** power for digit in digits)

    if total == number:
        print("Armstrong number")
    else:
        print("Not an Armstrong number")

