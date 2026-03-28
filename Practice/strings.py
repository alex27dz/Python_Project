# String Manipulation Examples

text = "hello world"

# 1. Indexing
print("Indexing:")
print(text[0])   # h
print(text[-1])  # d
print()

# 2. Slicing
print("Slicing:")
print(text[0:5])   # hello
print(text[:5])    # hello
print(text[6:])    # world
print()

# 3. Concatenation
print("Concatenation:")
first = "Hello"
second = "Alex"
result = first + " " + second
print(result)   # Hello Alex
print()

# 4. Change Case
print("Change Case:")
print(text.upper())   # HELLO WORLD
print(text.lower())   # hello world
print(text.title())   # Hello World
print()

# 5. Replace
print("Replace:")
new_text = text.replace("world", "QA")
print(new_text)   # hello QA
print()

# 6. Check Methods
print("Check Methods:")
print("isalpha:", text.isalpha())   # False (space exists)
print("isdigit:", text.isdigit())   # False
print("islower:", text.islower())   # True
print()

# 7. Length
print("Length:")
print(len(text))   # 11
print()

# 8. Split (string → list)
print("Split:")
words = text.split(" ")
print(words)   # ['hello', 'world']
print()

# 9. Join (list → string)
print("Join:")
joined_text = " ".join(words)
print(joined_text)   # hello world
print()

string = 'alex'
print(string[::-1])

stinga = ' hello world '
print(stinga.strip())

text = "hello world"

# 1. find() → returns index or -1
print("find:")
print(text.find("world"))   # 6
print(text.find("abc"))     # -1
print()

# 2. index() → returns index or ERROR if not found
print("index:")
print(text.index("world"))  # 6
# print(text.index("abc"))  # ❌ ValueError (uncomment to see)
print()

# 3. startswith()
print("startswith:")
print(text.startswith("hello"))  # True
print(text.startswith("world"))  # False
print()

# 4. endswith()
print("endswith:")
print(text.endswith("world"))  # True
print(text.endswith("hello"))  # False
print()

email = "test@example.com"

if "@" in email and email.endswith(".com"):
    print("Valid email format")
else:
    print("Invalid email")

text = "hello world"

# replace word
new_text = text.replace("world", "Alex")
print(new_text)   # hello Alex

# replace character
text2 = "banana"
print(text2.replace("a", "o"))   # bonono

text = "hello world"

# create translation table
table = str.maketrans({
    "h": "H",
    "w": "W",
    "o": "0"
})

# apply translation
new_text = text.translate(table)
print(new_text)   # Hell0 W0rld

# 1. split() → string → list
text = "hello world python"

words = text.split(" ")
print(words)   # ['hello', 'world', 'python']
print()

# split by comma
text2 = "apple,banana,cherry"
fruits = text2.split(",")
print(fruits)   # ['apple', 'banana', 'cherry']
print()


# 2. join() → list → string
words = ["hello", "world", "python"]

result = " ".join(words)
print(result)   # hello world python
print()

# join with comma
fruits = ["apple", "banana", "cherry"]

result2 = ",".join(fruits)
print(result2)   # apple,banana,cherry
print()


# 3. Real example (cleaning input)
text = "   hello   world   "

# remove spaces + split
words = text.strip().split()
print(words)   # ['hello', 'world']

# join back clean
clean_text = " ".join(words)
print(clean_text)   # hello world

text = "alex alex alex"

print(text.count("alex"))   # 3
print(text.count("a"))      # 3
print(text.count("x"))      # 3

text = "alex"

freq = {}

for char in text:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

print(freq)
# {'a': 1, 'l': 1, 'e': 1, 'x': 1}

