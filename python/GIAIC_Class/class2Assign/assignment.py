#1> Arithmetic opertators
# 1. Addition: a + b
a = 1
b = 2
print(a+b) 

# 2.Subtraction : c - d
c = 5
d = 3
print(c-d)

# Mutiplicaton : e * f
e = 4
f = 6
print(e*f)

# Division : g / h
g = 10
h = 2
print(g/h)

# Modulus i % j
i = 10
j = 3
print(i%j) #remainder   

# Exponentiation : k ** l
k = 2
l = 3
print(k**l)

# Floor division : m // n
m = 10
n = 3
print(m//n) #roundfigure the value and remove the decimel part

#2> Assinghment operators
# Assinghment operators are used to assign values to variables.

# 1. = (Assignment)
# Assigns the value of the right operand to the left operand.
x = 5
print(x)

# 2. += (Addition Assignment)
# Adds the value of the right operand to the left operand and assigns the result to the left operand
x = 5
x += 3
print(x) #output: 5

# 3. -= (Subtraction Assignment)
# Subtracts the value of the right operand from the left operand and assigns the result to the left operand
s = 5
s -=4
print(s) #output: 1

# 4. *= (Multiplication Assignment)
# Multiplies the value of the left operand with the value of the right operand and assigns the result
# to the left operand
t = 5
t *= 7
print(t) #output: 15

# 5. /= (Division Assignment)
# Divides the value of the left operand with the value of the right operand and assigns the result
# to the left operand
u = 10
u /= 2
print(u) #output: 5.0


# 6. %= (Modulus Assignment)
# Divides the value of the left operand with the value of the right operand and assigns the remainder
# of the division to the left operand
v = 10
v %= 3
print(v) #output: 1

# 7. **= (Exponentiation Assignment)
# Raises the value of the left operand to the power of the right operand and assigns the result to
# the left operand
w = 2
w **= 3
print(w) #output: 8

#3> Comparison operators
# Comparison operators are used to compare two values.
# They return a boolean value (True or False) depending on whether the comparison is true or fals

# 1. == (Equal to)
# Checks if the value of the left operand is equal to the value of the right operand
x = 5
y = 5
print(x == y) #output: True
print(x == 3) #output: False

# 2. != (Not Equal to)
# Checks if the value of the left operand is not equal to the value of the right operand
z = 5
print(z != 3) #output: True
print(z != 5) #output: False

# 3. > (Greater than)
# Checks if the value of the left operand is greater than the value of the right operand
a = 5
print(a > 3) #output: True
print(a > 5) #output: False

# 4. < (Less than)
# Checks if the value of the left operand is less than the value of the right operand
b = 5
print(b < 3) #output: False
print(b < 5) #output: False

# 5. >= (Greater than or Equal to)
# Checks if the value of the left operand is greater than or equal to the value of the right
# operand
c = 5
print(c >= 3) #output: True
print(c >= 5) #output: True
# 6. <= (Less than or Equal to)
# Checks if the value of the left operand is less than or equal to the value of the right
# operand
d = 5
print(d <= 3) #output: False
print(d <= 5) #output: True

# 7. ** (Exponentiation)
# Checks if the value of the left operand is equal to the value of the right operand
e = 5
print(e ** 2 == 25) #output: True

#4> Logical Operators
# Logical operators are used to combine multiple conditions in a single expression.
# They return a boolean value (True or False) depending on whether the condition is true or fals
# 1. and (And)
# Returns True if both the conditions are true
f = 5
print(f > 3 and f < 10) #output: True

# 2. or (Or)
# Returns True if either of the conditions is true
g = 5
print(g > 3 or g < 10) #output: True

# 3. not (Not)
# Returns True if the condition is false and vice versa
h = 5
print(not h > 3) #output: False

#5> Identity operators 
# These operators are used to check if both variables are the same or not.
# 1. is (Is)
# Returns True if both variables are the same and false otherwise
i = 5
print(i is 5) #output: True
# 2. is not (Is Not)
# Returns True if both variables are not the same and false otherwise
j = 5
print(j is not 5) #output: False


#6> Membership operators
# These operators are used to check if a value exists in a sequence or not.
# 1. in (In)
# Returns True if the value exists in the sequence and false otherwise
k = 5
print(k in [1, 2, 3, 4, 5]) #output

# 2. not in (Not In)
# Returns True if the value does not exist in the sequence and false otherwise
l = 5
print(l not in [1, 2, 3, 4, 5])
#output: False

#7> Bitwise operators
# These operators are used to perform operations on the binary representation of the numbers.

# 1. & (Bitwise And)
# Returns the binary AND of the two numbers
m = 5
print(m & 3) #output: 1

# 2. | (Bitwise Or)
# Returns the binary OR of the two numbers
n = 5
print(n | 3) #output: 7

# 3. ^ (Bitwise Xor)
# Returns the binary XOR of the two numbers
o = 5
print(o ^ 3) #output: 6

# 4. ~ (Bitwise Not)
# Returns the binary NOT of the number
p = 5
print(~p) #output: -6

# 5. << (Left Shift)
# Shifts the binary representation of the number to the left by the specified number of places
q = 5
print(q << 2) #output: 20

# 6. >> (Right Shift)
# Shifts the binary representation of the number to the right by the specified number of places
r = 5
print(r >> 2) #output: 1

