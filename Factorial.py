'''import math
a = math.factorial(4444)
print(a)
b = str(a)
print(len(b))
my_dict = dict()
for num in b:
    if num in my_dict:
        my_dict[num] += 1
    else:
        my_dict[num] = 1
sum=0
for k in sorted(my_dict):
    print(k, ":", my_dict[k])
for num in b:
    sum += int(num)
print(sum)
'''
def split(word):
    return [char for char in word]
word = input()
word = split(word)
letter = input()
letter = split(letter)
i = int(letter[0])
word[i] = letter[2]
print("".join(word))