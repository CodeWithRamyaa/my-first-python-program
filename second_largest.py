
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

unique_numbers = list(set(numbers))

if len(unique_numbers) < 2:
    print("Second largest number does not exist")
else:
    unique_numbers.sort()
    print("Second largest number:", unique_numbers[-2])
