string = 'hello broski'

freq = {}

for char in string:
    print(char)
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1
print(freq)