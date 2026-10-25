
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

target = int(input("Enter the number to search: "))

found = False

for i in range(len(numbers)):
    if numbers[i] == target:
        print("Number found at index:", i)
        found = True
        break

if not found:
    print("Number not found")

