n = int(input())

for i in range(1, n + 1):
    digits_sum = 0
    for digits in str(i):
        digits_sum += int(digits)
    is_special = digits_sum in [5, 7, 11]
    print(f"{i} -> {is_special}")
