str = input()

for char in str:
    if char.isupper():
        print(char.lower(), end='')
    else:
        print(char.upper(), end='')