
#1. Check Prime Number
num = int(input("Enter a number: "))

if num < 2:
    print("not a prime number")
else:
    for i in range(2, num):
        if num % i == 0:
            print("not a prime number")
            break
    else:
        print("Prime number")


#2. Find the Factorial of a Number
num = int(input("enter number please:"))
fact = 1
for i in range(1, num + 1):
    fact *= i

print("Factorial =", fact)


# 3. Print the Fibonacci Sequence
n = int(input("How many terms? "))
a = 0
b = 1
for i in range(n):
    print(a, end=" ")

    next_number = a + b
    a = b
    b = next_number


#5. Generate a Random Number
import random
num = random.randint(1,100)
print("random number:",num)


# 7. Remove Punctuations From a String
import string
result = ""
text = input("enter text:")
for char in text:
    if char not in string.punctuation:
        result += char

print("string without punctuation:",result)



# 8. Sort Words in Alphabetic Order
text = input("enter text:")
words = text.split()
words.sort()
result = " ".join(words)
print("after sort:", result)


# 9. Merge Two Dictionaries
dict1 = {
    "name":"Aseel",
    "age":21
}
dict2 = {
    "city":"nablus",
    "job":"developer"
}
dict1.update(dict2)
print(dict1)

# or another way
#merged_dict = dict1 | dict2
#print(merged_dict)


# 10. Merge Two Lists and Inverse the Merged List
list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged_list = list1 + list2
merged_list.reverse()
print(merged_list)


# 11. Remove Duplicate Element From a List
nums = [1, 2, 3, 2, 4, 1, 5]
unique_numbers = list(set(nums))
print(unique_numbers)


# 13. Convert Two Lists Into a Dictionary 
keys = ["name", "age", "city"]
values = ["Aseel", 22, "Ramallah"]
result = dict(zip(keys, values))
print(result)


# 14. Delete an Element From a Dictionary if it exist
student = {
    "name": "Aseel",
    "age": 22,
    "city": "Ramallah"
}

student.pop("age", None)
print(student)


# 15. Make a Flattened List from Nested List
nested_list = [[1, 2, 3], [4, 5], [6, 7, 8]]
flattened_list = []

for sublist in nested_list:
    for item in sublist:
        flattened_list.append(item)

print(flattened_list)


# 16. Read and Write to a File
# Write to the file
with open("example.txt", "w") as file:
    file.write("Welcome!\n")
    file.write("Hello Aseeeeeeeell.")

# Read from the file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)


# 17. Append to a File
with open("example.txt", "a") as file:
    file.write("\ngood morning!")


# 19. Calculate the Difference in Memory Address in List Objects
# List
list1 = [1, 2, 3]
list2 = [4, 5, 6]

address1 = id(list1)
address2 = id(list2)

difference = abs(address1 - address2)

print("Memory address of list1:", address1)
print("Memory address of list2:", address2)
print("Difference:", difference)