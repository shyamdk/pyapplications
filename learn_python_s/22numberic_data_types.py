#Built-in Data Types
#numeric - int, float, complex
#iterator
#sequence (also an iterator)
#mapping
#file
#class
#exception
#Operator precedence - BODMAS - Division and Multiplication have equal precedence, so are addtion and substraction
# executed Left to Right

a = 12
b = 3
print(a+b)  #15
print(a-b)  #9
print(a*b)  #36
print(a/b)  #4.0
print(a//b)  # Integer Divison
print(a%b)  #0 remainder
print()

for i in range(1, a//b):
    print(i)

print(a / (b * a) / b)