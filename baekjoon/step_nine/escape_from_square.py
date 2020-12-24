# https://www.acmicpc.net/problem/1085

x, y, w ,h = map(int, input().split())

length_list = []

top_length = h - y
bottom_length = y
left_length = x
right_length = w - x

length_list.append(top_length)
length_list.append(bottom_length)
length_list.append(left_length)
length_list.append(right_length)

print(min(length_list))