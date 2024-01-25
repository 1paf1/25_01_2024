
# def factorial(number):
#     if number == 1:
#         return 1
#
#     return number * factorial(number - 1)
#
# try:
#     user_input = int(input("Enter a number: "))
#
# except ValueError:
#     print("Invalid input. Please enter int number")
#
# print(f"The factorial of {user_input} is {factorial(user_input)}")


# Завдання 1.
#
# Написати рекурсивну функцію знаходження ступеня числа.


# def get_number_pow(number, power):
#     if power == 0:
#         return 1
#
#     return number * get_number_pow(number, power - 1)
# try:
#     number = int(input("Enter a number: "))
#     power = int(input("Enter the power: "))
# except ValueError:
#     print("Invalid input")
#
# print(f"{number} in power {power} = {number ** power}")


# тестові значення number = 2, power = 3
# get_number_pow(2, 3) -> 2 * get_number_pow(2, 2) => 8
# get_number_pow(2, 2) -> 2 * get_number_pow(2, 1) => 4
# get_number_pow(2, 1) -> 2

# Завдання 2.
#
# Написати рекурсивну функцію, яка виводить N зірок у ряд, число N задає користувач.

# def print_stars(number_of_stars):
#     if number_of_stars > 0:
#         print('*', end='')
#         print_stars(number_of_stars - 1)
#
# try:
#     number_of_stars = int(input("Enter number of stars: "))
# except ValueError:
#     print("Please enter a number")
#
# print_stars(number_of_stars)


# Тестове значення number_of_stars = 5
# print_stars(5) -> '*' + print_stars(4)
# print_stars(4) -> '*' + print_stars(3)
# print_stars(3) -> '*' + print_stars(2)
# print_stars(2) -> '*' + print_stars(1)
# print_stars(1) -> '*' + print_stars(0)
# print_stars(0) -> ''


# Завдання 3.
#
# Написати рекурсивну функцію, яка обчислює суму всіх чисел у діапазоні від a до b.
#
# Користувач вводить a та b. Проілюструйте роботу функції прикладом.

# def sum_in_range_num1_to_num2(num1, num2):
#     if num1 > num2:
#         return 0
#     elif num1 == num2:
#         return num1
#     else:
#         return num1 + sum_in_range_num1_to_num2(num1 + 1, num2)
#
# try:
#     num1 = int(input("Enter a number: "))
#     num2 = int(input("Enter a second number: "))
# except ValueError:
#     print("Input is not an integer")
#
# print(f"sum in range from num1 to num2 is {sum_in_range_num1_to_num2(num1, num2)}")


# Тестове значення num1 = 2, num2 = 5
# sum_in_range_num1_to_num2(2, 5) -> 2 + sum_in_range_num1_to_num2(3, 5)
# sum_in_range_num1_to_num2(3, 5) -> 3 + sum_in_range_num1_to_num2(4, 5)
# sum_in_range_num1_to_num2(4, 5) -> 4 + sum_in_range_num1_to_num2(5, 5)
# sum_in_range_num1_to_num2(5, 5) -> 5