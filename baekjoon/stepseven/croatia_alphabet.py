# https://www.acmicpc.net/problem/2941

croatia_alphabet = input()

croatia_alphabet = croatia_alphabet.replace('c=', 'X')
croatia_alphabet = croatia_alphabet.replace('c-', 'X')
croatia_alphabet = croatia_alphabet.replace('dz=', 'X')
croatia_alphabet = croatia_alphabet.replace('d-', 'X')
croatia_alphabet = croatia_alphabet.replace('lj', 'X')
croatia_alphabet = croatia_alphabet.replace('nj', 'X')
croatia_alphabet = croatia_alphabet.replace('s=', 'X')
croatia_alphabet = croatia_alphabet.replace('z=', 'X')

length = len(croatia_alphabet)

print(length)