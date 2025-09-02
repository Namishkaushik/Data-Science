# 🐍 Python Introduction:

Python is a **high-level, interpreted programming language** developed by ***Guido van Rossum in 1991***. It is widely used in Data Science because of its simplicity and powerful libraries.

---

## 1️⃣ Python Setup:
- Install **Python** from [python.org](https://www.python.org/) or use **Anaconda** for data science.  
- Use **Jupyter Notebook** or **Google Colab** for interactive coding.

---

## 2️⃣ Python Syntax:

### 🖨 Print & Comments:
`print()` is a **built-in function** in Python that **outputs text, numbers, variables, or any other data** to the standard output device (usually your monitor). <br>
While, a `comment` is a line in the code that Python **ignores** while running the program.
```python
# This is a comment
print("Hello, Data Science!")  # Prints text
```
### 📝 Variables & Data Types:
Variable is like a **container** that is used to store data in your program.
  - It doesn’t need explicit declaration of type (Python figures it out automatically).
  - The value stored in a variable **can change while the program runs** — that’s why it’s called a *variable*.
```python
x = 10          # integer
y = 3.14        # float
name = "Namish" # string
is_student = True # boolean
```
Here **x, y, name, is_student** are variables. They are assigned values of different data types as mentioned in the code bloc.
## 3️⃣ Operators:
Operators are **special symbols** in Python that **perform operations** on values or variables.
They tell Python what kind of action to perform. There are various types of operators:

### ✏️ Assignment Operators:
These operators basdically **assign values to the variables**.  <br>
**For Example:**
```python
x = 10 # value '10' is assigned to variable 'x'
```
This was the basic assignment operator. It can be also be **combined with differnt arithmetic operators** to perform and assign values. <br>
**For Example:**
```python
x+=1 # This basically means x = x+1
```
**Common Assignment Operators:**

| Operator | Example   | Equivalent To     |
|----------|-----------|-------------------|
| `=`      | `x = 5`   | `Assigns 5 to x`   |
| `+=`     | `x += 3`  | `x = x + 3`       |
| `-=`     | `x -= 2`  | `x = x - 2`       |
| `*=`     | `x *= 4`  | `x = x * 4`       |
| `/=`     | `x /= 2`  | `x = x / 2`       |
| `%=`     | `x %= 3`  | `x = x % 3`       |
| `**=`    | `x **= 2` | `x = x ** 2`      |
| `//=`    | `x //= 2` | `x = x // 2`      |


### 🔢 Arithmetic Operator:
Arithmetic operators in Python are the symbols we use to perform mathematical operations on numbers.
We have many kinds of Arithmetic Operators:
```python
a = 10
b = 3
```
- #### Addition (+):
    It adds 'a' and 'b'
    ```python
    print(a + b) 
    ```
    👆 It basically means:
    ```python
    print(10 + 3) # Assigned the values of 'a' and 'b'.
      # Answer - 13
    ```

- #### Subtraction (-):
    It subtracts 'b' from 'a'.
    ```python
    print(a - b)
    ```
    Now, it will assign the values of 'a' and 'b'.
    ```python
    print(10 - 3)
      # Answer - 7
    ```

- #### Multiplication (*):
    It multilies 'a' and 'b'.
    ```python
    print(a * b)
    ```
    Output : 30

- #### Division (/):
    It divides 'a' from 'b'.
    ```python
    print(a / b)
    ```
    Output : 3.3333333333333335

- #### Floor Division (//):
    It divides 'a' from 'b' and rounds the answer (towards negative infinity) to the nearest whole number.
    ```python
    print(a // b) 
    ```
    Output : 3

- #### Modulus (%):
    It returns the remainder after dividing 'a' by 'b'.
    ```python
    print(a % b)
    ```
    Output : 1

- #### Exponential (**):
    It means 'raise to the power of', it multiplies 'a' by itself ,'b' number of times
    ```python
    print(a ** b)
    ```
    Output : 1000

  
### ⚖️ Comparison Operators:
Comparison operators (also called **relational operators**) are used to **compare two values**.
They return either `True` or `False` (Boolean result).<br><br>
***List of Comparison Operators:***

| Operator | Meaning                  | Example   | Result   |
|----------|--------------------------|-----------|----------|
| `==`     | Equal to                 | `5 == 5`  | `True`   |
| `!=`     | Not equal to             | `5 != 3`  | `True`   |
| `>`      | Greater than             | `5 > 3`   | `True`   |
| `<`      | Less than                | `5 < 3`   | `False`  |
| `>=`     | Greater than or equal to | `5 >= 5`  | `True`   |
| `<=`     | Less than or equal to    | `3 <= 5`  | `True`   |

***Example in python:***
```python
x = 10
y = 20

# Statement     # Output

print(x == y)   # False
print(x != y)   # True
print(x > y)    # False
print(x < y)    # True
print(x >= 10)  # True
print(y <= 15)  # False
```
They are mostly used when you want to check conditions, often inside `if` and `while loops`.


### 🔗 Logical Operators:
Logical operators are used to **combine conditional statements**. They return either `True` or `False` (Boolean result).
<br><br>
***Types of Logical Operators:***

| Operator | Meaning                                              | Example                  | Result |
|----------|------------------------------------------------------|--------------------------|--------|
| `and`    | Returns `True` if **both** conditions are true       | `(5 > 2 and 10 > 3)`     | `True` |
| `or`     | Returns `True` if **at least one** condition is true | `(5 > 2 or 10 < 3)`      | `True` |
| `not`    | Reverses the result (True → False, False → True)     | `not(5 > 2)`             | `False` |

***For Example:***
```python
x = 5
y = 10

# Statement              # Output

print(x > 2 and y > 5)   # True  (both conditions are True)
print(x > 2 or y < 5)    # True  (one condition is True)
print(not(x > 2))        # False (because x > 2 is True, but not makes it False)
```

### ⚙️ Bitwise Operators:
Bitwise operators work on **binary (bit-level) representations** of numbers.
<br><br>
***Types of Bitwise Operators:***
| Operator | Name        | Description                              | Example | Result |
|----------|-------------|------------------------------------------|---------|--------|
| `&`      | AND         | Sets each bit to 1 if both bits are 1    | `5 & 3` | `1` |
| `\|`      | OR          | Sets each bit to 1 if one of the bits is 1 | `5 \| 3` | `7` |
| `^`      | XOR         | Sets each bit to 1 if only one bit is 1  | `5 ^ 3` | `6` |
| `~`      | NOT         | Inverts all the bits (2’s complement form) | `~5` | `-6` |
| `<<`     | Left Shift  | Shifts bits left (adds zeros on right)   | `5 << 1` | `10` |
| `>>`     | Right Shift | Shifts bits right (drops bits on right)  | `5 >> 1` | `2` |

***Example:***
```python
a = 5    # 0101 in binary
b = 3    # 0011 in binary

# Statement    # Output

print(a & b)   # 1  (0001)
print(a | b)   # 7  (0111)
print(a ^ b)   # 6  (0110)
print(~a)      # -6 (inverts bits of 5)
print(a << 1)  # 10 (1010)
print(a >> 1)  # 2  (0010)
```

### 🆔 Identity Operator:
Identity operators check whether **two objects are the same in memory**, not just equal in value.
<br><br>
***Types of Identity Operators:***
| Operator | Description | Example | Result |
|----------|-------------|---------|--------|
| `is`     | Returns True if both variables point to the same object | `x is y` | `True` / `False` |
| `is not` | Returns True if they do **not** point to the same object | `x is not y` | `True` / `False` |

***Example:***
```python
x = [1, 2, 3]
y = [1, 2, 3]
z = x

# Statement        # Output

print(x is y)      # False (different objects in memory)
print(x is z)      # True  (same memory reference)
print(x is not y)  # True
```


### 🧩 Membership Operator:
Membership operators test whether a **value exists in a sequence** (string, list, tuple, etc.).
<br> <br>
***Types of Membership Operator:***
| Operator | Description | Example | Result |
|----------|-------------|---------|--------|
| `in`     | Returns True if value is found in sequence | `"a" in "apple"` | `True` |
| `not in` | Returns True if value is NOT found in sequence | `5 not in [1, 2, 3]` | `True` |

***Example:***
```python
fruits = ["apple", "banana", "cherry"]

# Statement                   # Output
print("apple" in fruits)      # True
print("grape" not in fruits)  # True
print("z" in "pizza")         # True (string membership check)
```
