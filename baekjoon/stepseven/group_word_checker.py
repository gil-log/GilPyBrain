# https://www.acmicpc.net/problem/1316

word_count = int(input())

count = 0
for i in range(word_count):
    word = input()
    before_letter = ' '
    dictionary = {}
    group_word_checker = 1

    for letter in word:

        if(before_letter == ' ' or before_letter == letter):
            before_letter = letter
        else:
            if(dictionary.get(before_letter) == None):

                dictionary[before_letter] = 1
            else:
                group_word_checker = 0

            before_letter = letter
    length = len(word)
    last_letter = word[length-1]
    if(dictionary.get(before_letter) != None):
        group_word_checker = 0

    if(group_word_checker == 1):
        count = count + 1

print(count)

