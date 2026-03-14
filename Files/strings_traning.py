'''
----------------------------------------
c = message.find('broski')
k = c + len('broski')
print(message[c:k])
----------------------------------------
abc = 'abcdefghijklmnopqrstuvwxyz'
helper = {}
for i in abc:
    helper[i] = message.count(i)

print(helper)
----------------------------------------
for i in message:
    counter = 0
    for k in message:
        if i == k:
            counter +=1
    dict[i] = counter
print(dict)
----------------------------------------
dict = {}
message = "hello broski"

char_count = {}
for i in message:
    if i in char_count:
        char_count[i] += 1
    else:
        char_count[i] = 1

print(char_count)
----------------------------------------
message = "hello broski"

#newmessage = message[::-1]
#print(newmessage)
----------------------------------------
message = "hello broski"
newmessage = ""

for i in range(len(message) -1, -1, -1):  # start, stop, step
    newmessage += message[i]

print(newmessage)
----------------------------------------
from sys import flags

str1 = "listen"
str2 = "silent"
flagis = 0
flagisfalse = 0

for i in str1:
    if i in str2 and str1.count(i) == str2.count(i):
        flagis += 1
    else:
        flagisfalse += 1

if len(str1) != len(str2):
    print("Not Anagram")

if flagisfalse > 0:
    print('Not Anagram')
else:
    print('Anagram')

----------------------------------------
list1 = [1, 2, 5, 9, 7, 8, 6]

helperlist = []
for k in range(len(list1)):
    maxnum = list1[0]
    for i in list1:
        if i > maxnum:
            maxnum = i
    helperlist.append(maxnum)
    list1.remove(maxnum)

print(helperlist)
----------------------------------------
dict1 = {
    "Alex": {"age": 30, "city": "New York"},
    "Jamoy": {"age": 29, "city": "Los Angeles"}
}

dict2 = {
    "Alex": {"age": 35, "profession": "Engineer"},
    "Oleg": {"age": 40, "city": "Chicago"}
}



for key in dict1:
    print(key)
    print(dict1[key])
    print(type(dict1[key]))
    if type(dict1[key]) == dict:
        print('dictionary is in value')

        if key not in dict2:
            dict2[key] = {}

        for value in dict1[key]:
            dict2[key][value] = dict1[key][value]
    else:
        print('regular value')
        dict2[key] = dict1[key]

print("✅ Merged Result:")
print(dict2)
----------------------------------------

'''















