nums = [0, 1, 2, 3, 4]

squares = [x ** 2 for x in nums]
print(squares)

even_squares = [x ** 2 for x in nums if x % 2 == 0]
print(even_squares)

even_num_to_square = {x: x ** 2 for x in nums if x % 2 == 0}
print(even_num_to_square)
