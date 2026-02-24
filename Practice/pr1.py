string = "say hello broski"
substring = "hello"

start = string.find(substring)
end = start + len(substring)

newstring = string[start:end]
print(newstring)