def even_squares(numbers):
    result = {}
    for n in numbers:
        if n % 2 == 0:
            result[n] = n * n
    return result

print(even_squares([1, 2, 3, 4, 5, 6]))