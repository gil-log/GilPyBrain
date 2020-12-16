# https://www.acmicpc.net/problem/2908

first_number, second_number = map(int, input().split())

first_units = first_number % 10
first_tens = int(int(first_number / 10) - (int(first_number / 100) * 10))
first_hundreds = int(first_number / 100)

second_units = second_number % 10
second_tens = int(int(second_number / 10) - (int(second_number / 100) * 10))
second_hundreds = int(second_number / 100)

first_reverse_number = first_units * 100 + first_tens * 10 + first_hundreds
second_reverse_number = second_units * 100 + second_tens * 10 + second_hundreds

max_number = max(first_reverse_number, second_reverse_number)

print(max_number)