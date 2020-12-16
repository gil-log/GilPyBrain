# https://www.acmicpc.net/problem/1152

word = input()

count = 0

letter_flag = 0
for letter in word:

    if(letter_flag == 1 and letter == " "):
        count = count + 1
        letter_flag = 0

    if(letter != " "):
        letter_flag = 1

length = len(word)
last_letter = word[length - 1]
if(last_letter != " "): count = count + 1
print(count)