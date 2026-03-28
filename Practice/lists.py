list = [1,2,3,4,5]
print(list[0:5])
print(len(list))

# starting list
numbers = [1, 2, 3]

# 1. append() → add ONE item to the end
numbers.append(4)
print("append:", numbers)   # [1, 2, 3, 4]

# 2. extend() → add MULTIPLE items
numbers.extend([5, 6])
print("extend:", numbers)   # [1, 2, 3, 4, 5, 6]

# 3. insert() → add at specific index
numbers.insert(0, 0)
print("insert:", numbers)   # [0, 1, 2, 3, 4, 5, 6]

# 4. remove() → remove by VALUE (first match)
numbers.remove(3)
print("remove:", numbers)   # [0, 1, 2, 4, 5, 6]

# 5. pop() → remove by INDEX and return value
last_item = numbers.pop()
print("pop:", numbers)      # [0, 1, 2, 4, 5]
print("popped value:", last_item)  # 6



numbers = [3, 1, 4, 2]
sorted_list = []

# we loop fixed number of times
for _ in range(len(numbers)):
    max_val = numbers[0]

    # find max
    for num in numbers:
        if num > max_val:
            max_val = num

    # move max to new list
    sorted_list.append(max_val)
    numbers.remove(max_val)

print(sorted_list)   # [4, 3, 2, 1]