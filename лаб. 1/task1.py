numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
b = numbers[0:4]
с = numbers[5:-1]
numbers[4] = 0
g = sum(numbers)
h = len(numbers)
a = g / h
numbers[4] = a
print("Измененный список:", numbers)
