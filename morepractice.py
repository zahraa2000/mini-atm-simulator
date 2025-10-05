# Practice with Python Operators

# 1. Arithmetic Operators
a = 15
b = 4
print("Arithmetic Operators")
print("a + b =", a + b)   # Addition
print("a - b =", a - b)   # Subtraction
print("a * b =", a * b)   # Multiplication
print("a / b =", a / b)   # Division
print("a % b =", a % b)   # Modulus (remainder)
print("a ** b =", a ** b) # Exponentiation
print("a // b =", a // b) # Floor division
print("-" * 30)

# 2. Comparison Operators
print("Comparison Operators")
print("a == b:", a == b)  # Equal
print("a != b:", a != b)  # Not equal
print("a > b:", a > b)    # Greater than
print("a < b:", a < b)    # Less than
print("a >= b:", a >= b)  # Greater or equal
print("a <= b:", a <= b)  # Less or equal
print("-" * 30)

# 3. Logical Operators
x = True
y = False
print("Logical Operators")
print("x and y:", x and y)
print("x or y:", x or y)
print("not x:", not x)
print("-" * 30)

# 4. Bitwise Operators
m = 6   # binary: 110
n = 3   # binary: 011
print("Bitwise Operators")
print("m & n =", m & n)   # AND
print("m | n =", m | n)   # OR
print("m ^ n =", m ^ n)   # XOR
print("~m =", ~m)         # NOT
print("m << 1 =", m << 1) # Left shift
print("m >> 1 =", m >> 1) # Right shift
print("-" * 30)


# String Operators in Python

# 1. Concatenation (+)
str1 = "Hello"
str2 = "World"
print("Concatenation:", str1 + " " + str2)  # Hello World

# 2. Repetition (*)
print("Repetition:", str1 * 3)  # HelloHelloHello

# 3. Membership (in / not in)
print("'H' in str1:", 'H' in str1)       # True
print("'z' not in str1:", 'z' not in str1)  # True

# 4. Comparison (==, !=, >, <, >=, <=)
a = "apple"
b = "banana"
print("a == b:", a == b)  # False
print("a != b:", a != b)  # True
print("a < b:", a < b)    # True (compares alphabetically)
print("a > b:", a > b)    # False

# 5. Indexing and Slicing (using [])
word = "Python"
print("First char:", word[0])     # P
print("Last char:", word[-1])     # n
print("Slice [0:3]:", word[0:3])  # Pyt
print("Reversed:", word[::-1])    # nohtyP

# -----------------------------------------
# Practice Code: Conditions + Conditional Operators
# -----------------------------------------

# 1. Even or Odd
num = int(input("Enter a number: "))
print("Result:", "Even" if num % 2 == 0 else "Odd")

print("-" * 40)

# 2. Positive, Zero, or Negative
num2 = int(input("Enter another number: "))
check = "Positive" if num2 > 0 else "Zero" if num2 == 0 else "Negative"
print(f"{num2} is {check}")

print("-" * 40)

# 3. Voting eligibility
age = int(input("Enter your age: "))
print("Voting Eligibility:", "Eligible to Vote" if age >= 18 else "Not Eligible")

print("-" * 40)

# 4. Presidency eligibility (nested condition)
age2 = int(input("Enter age for presidency check: "))
eligibility = "Eligible for Presidency" if age2 >= 40 else "Eligible to Vote" if age2 >= 18 else "Not Eligible"
print(f"At age {age2} → {eligibility}")

print("-" * 40)

# 5. Compare two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
comparison = "a > b" if a > b else "a < b" if a < b else "a == b"
print(f"Comparison → {comparison}")

print("-" * 40)

# 6. Compare two strings
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
result = "Same" if s1 == s2 else "Not Same"
print(f"Comparison of '{s1}' and '{s2}' → {result}")

print("-" * 40)

# 7. Check if string is empty
text = input("Enter any string (or leave empty): ")
status = "Empty" if text == "" else "Not Empty"
print(f"The string is → {status}")

print("-" * 40)

# 8. Grading system
score = int(input("Enter your score (0-100): "))
grade = "A" if score >= 90 else "B" if score >= 75 else "C" if score >= 50 else "F"
print(f"Score: {score} → Grade: {grade}")

print("-" * 40)

# 9. Character check in word
word = input("Enter a word: ")
ch = input("Enter a character to search: ")
exists = f"'{ch}' found in {word}" if ch in word else f"'{ch}' not found in {word}"
print("Check:", exists)

print("-" * 40)

# 10. Palindrome check
pal = input("Enter a word to check palindrome: ")
print("Palindrome:", "Yes" if pal == pal[::-1] else "No")

print("-" * 40)

