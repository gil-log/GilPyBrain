
# import math
#
# M, N = map(int, input().split())
#
# # prime_number_boolean_list = [False for i in range(M, N+1)]
#
# # prime_number_list = list()
#
# for number in range(M, N+1):
#     is_prime_number = True
#     sqrt_number = int(math.sqrt(number)) + 1
#
#     for i in range(2, sqrt_number):
#         if(number % i == 0):
#             is_prime_number = False
#             break
#
#     if(is_prime_number == False): continue
#
#     # for prime_number_in_list in prime_number_list:
#     #     if(number % prime_number_in_list == 0):
#     #         is_prime_number = False
#     #
#     # if(is_prime_number == False): continue
#     #
#     # prime_number_list.append(number)
#     print(number)

def isSoSu(v):
    for i in range(2, int(v ** 0.5) + 1):
        if v % i == 0: return 0
    return 1 * (v != 1)


a, b = map(int, input().split())

for i in range(int(a), int(b) + 1):
    if isSoSu(i) == 1:
        print(i)
