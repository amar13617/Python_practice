#Write a program to get the maximum number from a list.
num = [23,55,7,8,9]
max1 = num[0]
for index in num:
    if index > max1:
        max1 = index
#print(max1)
#Write a program to get the second maximum number from a list.
num = [23,55,7,8,9]
Largest_num = num[0]
Second_num = num[0]
for index in num:
    if index > Largest_num:
        Largest_num = index
        for index in num:
            if index > Second_num and index != Largest_num:
                Second_num  = index
#print(Second_num)

#Write a program in Python to remove duplicate items from a list.
num = [2,3,4,5,2,6,3,2]
list1 = []
for i in num:
    if i not in list1:
        list1.append(i)

#print(list1)

#Write a program to check whether a given key exists in a dictionary or not.
dict = {'0':1, '1':2, '2':3, '4':5}
def check_key(dict1):
    for i in dict1:
        if i in dict:
            return True
        else:
            return False
#print(check_key('7'))

#Python program to remove a set of keys.
num = {0:"Value 1", 1:"Value 2", 2:"Value 3"}
keys = [0,1]
for k in keys:
    num.pop(k)
#print(num)

#Write a program to sum all the values of a dictionary.
dict1 = {'key 1': 200, 'key 2': 300}
sm = 0
for i in dict1:
    sm = sm + dict1[i]
#print(sm)

#Write a program to get the maximum and minimum value of dictionary.
dict1 = {'key 1': 200, 'key 2': 300}
max = 0
for i in dict1.values():
    if i > max:
        max = i
#print(max)

#Define a function in python that accepts 3 values and returns the maximum of three numbers.
def maximum(a,b,c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c
#print(maximum(4,2,6))

#Define a function which counts vowels and consonant in a word.
def count(word):
    const = 0
    vowel = 0
    for i in range(len(word)):
        if word[i] in ["a", "e", "i","o","u"]:
            vowel = vowel + 1
        else:
            const = const + 1
#print(count("google"))

#Define a function that returns Factorial of a number.
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
#print(factorial(5))

#Define a function that accepts lowercase words and returns uppercase words.
def response(text):
    z = text.upper()
    return z
#print(response("Amar"))

#Write a program to reverse a string in python.
str = "amit"
str_reverse = []
for i in reversed(str):
    str_reverse.append(i)
text = "".join(str_reverse)
#print(text)

#Write a program to remove duplicates in a string.
str = "pythonlobby"
str_remove = []
for i in str:
    if i in str_remove:
        continue
    else:
        str_remove.append(i)

#print("".join(str_remove))

#Python program to count the occurrence of each character in a word.
word ="google"
dict = {}
for i in word:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1

#print(dict)

a = [1,2,3,4,5,6,7,8]
print(a[2::2])

#Reversing string
str = 'My Name is Jessa'
str1 = []
for ele in reversed(str):
    str1.append(ele)
#print("".join(str1))

#Remove items from a list while iterating
number_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
list1 = []
for ele in number_list:
    if ele <= 50:
        list1.append(ele)
#print(list1)

#Display all duplicate items from a list
sample_list = [10, 20, 60, 30, 20, 40, 30, 60, 70, 80]
unique = []
duplicate = []
for ele in sample_list:
    if ele not in unique:
        unique.append(ele)
    else:
        duplicate.append(ele)
#print(duplicate)

#Filter dictionary to contain keys present in the given list

# Calculate the multiplication and sum of two numbers.
def calculation(a,b):
    if a * b >= 1000:
        return a+b
    else:
        return a*b
#print(calculation(2,8))

name = 'natalie'
name1 = name[::-1]
#print(name1)

name2 = []
for i in reversed(name):
    name2.append(i)
#print("".join(name2))

message = 'Hola Amigos'
message1 = 'J' + message[1:]
#print(message1)

string = "Python is fun"
#print(string.partition('fun'))

string = "Python is fun, isn't it"
print(string.partition('is'))

sentences = 'Time to master data science', 'amar', 'at'
for i in sentences:
    print(i)

#print('a' > 'b')
#print('a' < 'b')
#print('abc'> 'b')
#print('abd'>'abc')

a = 7/2
#print(a)
b = 7%2
#print(b)
c = 7//2
#print(c)

#Write a program to check whether a given key exists in a dictionary or not.
dict = {'0':1, '1':2, '2':3}
def check(x):
    if x in dict:
        return "yes"
    else:
        return "No"
#print(check('7'))

#Write a program to iterate over dictionary items using for loop.

#Python program to remove a set of keys.
dict1 = {0:"Value 1", 1:"Value 2", 2:"Value 3"}

keys = [0,1]
for k in keys:
    dict1.pop(k)
#print(dict1)

#Python program to sort dictionary by values (Ascending/ Descending).
dict = {'c': 2, 'd':4 , 'a' : 3, 'b' : 1}
list1  = list(dict.items())
list1.sort(reverse= True)
#print(list1)

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
dict1 = {}
for i in range(0, len(keys)):
    dict1.update({keys[i] : values[i]})
#print(dict1)

#Merge two Python dictionaries into one
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict1.update(dict2)
#print(dict1)

sampleDict = { 
  "name": "Kelly",
  "age":25, 
  "salary": 8000, 
  "city": "New york" }

keys = ["name", "salary"]
n = {k: sampleDict[k] for k in keys}
#print(n)

#Write a program to rename a key city to a location in the following dictionary.
sampleDict = { 
  "name": "Kelly",
  "age":25, 
  "salary": 8000, 
  "city": "New york" }
sampleDict["Location"] = sampleDict.pop("city")
#print(sampleDict)

def check(mydict):

    sm = 0
    for i in mydict:
        sm =sm + mydict[i]
    return sm
dict1 = {'key 1': 200, 'key 2': 300}
#print(check(dict1))

#dict1 = {'key 1': 'Apple','key 2':'Mango','key 3':'Papaya'}

#for i in sorted(dict1.values()):

#Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x)
dict1 = {}
for i in range(1,11):
    dict1[i] = i*i
#print(dict1)

strn = 'pytHOnloBBy'
lower = []
upper = []
for i in range(len(strn)):
    if strn[i].islower():
        lower.append(strn[i])
    else:
        upper.append(strn[i])
#print(" ".join(lower+upper))

#count special character in string:
n = '@pyThOnlobb!Y34'
lower = 0
upper = 0
special = 0
numeric = 0
for i in range(len(n)):
    if n[i].islower():
        lower = lower + 1
    elif n[i].isupper():
        upper = upper + 1
    elif n[i].isnumeric():
        numeric = numeric + 1
    else:
        special = special + 1
#print(special)
#print(upper)

n = ["name","age","","hello"]
#n1 = []
#for i in range(len(n)):
#    if n[i] != "":
#        n1.append(n[i])
#print(n1)

str1 = "geekforgeek"
n = 4
str2 = ''
for char in range(len(str1)):
    if char != n:
        str2 = str2 + str1[char]
#print(str2)



    
name = "Amar"
like = "Biryaani"
a = 'my {0} and i eat {1}'.format(name, like)
#print(a)

print('One'.isalpha())
print('One1'.isalpha())

#Reverse the tuple in python
tuple1 = (10, 20, 30, 40, 50)
tuple2 = list(tuple1)
tuple_list = []
for i in reversed(tuple2):
    tuple_list.append(i)
#print(tuple(tuple_list))

tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
#print(tuple1[1][1])

#Swaping
tuple1 = (11, 22)
tuple2 = (99, 88)
tuple1 , tuple2 = tuple2, tuple1
#print(tuple1)
#print(tuple2)

#Modify tuple
tuple1 = (11, [22, 33], 44, 55)
tuple1[1][0] = 222
#print(tuple1)

#Counts the number of occurrences of item 50 from a tuple.
tuple1 = (50, 10, 60, 70, 50)
tuple2 = list(tuple1)
x = []
x1 = 50
for i in tuple2:
    if i == x1:
        x.append(i)
#print(x.count(50))

t1 = (1,2,3,4,5,6,7,8)
#print(t1[-5:-2])

#(a,b,c,d) = (1,2,3)
#ValueError

a = (2,1,3,5,6,77,4)
b = list(a)
max = 0
for i in b:
    if i > max:
        max = i
#print(max)


tuple1 = (1,2)
dict = {1 : 'python', 2: 'c'}
tuple2 = list(tuple1)
tuple2.append(dict)
#print(tuple(tuple2))



