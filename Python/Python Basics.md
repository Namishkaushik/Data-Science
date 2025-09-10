# 🐍 Python Introduction:

Python is a **high-level, interpreted programming language** developed by ***Guido van Rossum in 1991***. It is widely used in Data Science because of its simplicity and powerful libraries.

---
## 🤔 Why Python is Good for Data Science?

Python is extremely popular for **Data Science** because of its simplicity, versatility, and rich ecosystem of libraries.

### 1. Easy to Learn and Use
- Python has a **simple, readable syntax** — almost like English.
- Beginners can start coding quickly without worrying about complex rules.
- Ideal for experimenting with data and building models.

### 2. Extensive Libraries and Frameworks

Python has a huge ecosystem of libraries tailored for data science:

| Purpose                   | Popular Libraries                                   |
|----------------------------|---------------------------------------------------|
| Data manipulation          | `pandas`, `numpy`                                  |
| Data visualization         | `matplotlib`, `seaborn`, `plotly`                 |
| Machine learning / AI      | `scikit-learn`, `tensorflow`, `keras`, `pytorch`  |
| Statistics / Probability   | `scipy`, `statsmodels`                             |
| Big data processing        | `pyspark`, `dask`                                  |

These libraries **save time** and make data work much easier.

### 3. Versatility
- Python can handle everything from **data cleaning, visualization, and modeling** to **deploying ML models into production**.
- It works with **structured data (Excel, CSV, SQL)** and **unstructured data (text, images, videos)**.

### 4. Strong Community Support
- Python has a **massive global community**.
- Tutorials, forums, and documentation are widely available — if you face a problem, someone has likely already solved it.

### 5. Integration Capabilities
- Python integrates easily with **databases, web apps, cloud platforms**, and other programming languages.
- Useful for building end-to-end data pipelines.

### 6. Open Source and Free
- Python is **free** to use, with no licensing cost.
- You can use it for personal projects, research, and commercial applications without paying anything.

#### In Short
Python’s simplicity, rich libraries, versatility, and strong community make it the **#1 choice for Data Science**.


---
# ⚡ Starting with PYTHON...

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
Here **x, y, name, is_student** are variables. They are assigned values of different data types as mentioned in the code block.

---

## 3️⃣ Operators:
Operators are **special symbols** in Python that **perform operations** on values or variables.
They tell Python what kind of action to perform. There are various types of operators:

### ✏️ Assignment Operators:
These operators basically **assign values to the variables**.  

**For Example:**
```python
x = 10 # value '10' is assigned to variable 'x'
```
This was the basic assignment operator. It can be also be **combined with different arithmetic operators** to perform and assign values.

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

---

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
      # Output - 13
    ```

- #### Subtraction (-):
    It subtracts 'b' from 'a'.
    ```python
    print(a - b)
    ```
    Now, it will assign the values of 'a' and 'b'.
    ```python
    print(10 - 3)
      # Output - 7
    ```

- #### Multiplication (*):
    It multiplies 'a' and 'b'.
    ```python
    print(a * b)
    # Output : 30
    ```
    

- #### Division (/):
    It divides 'a' by 'b'.
    ```python
    print(a / b)
    # Output : 3.3333333333333335
    ```
    

- #### Floor Division (//):
    It divides 'a' by 'b' and rounds the answer (towards negative infinity) to the nearest whole number.
    ```python
    print(a // b)
    # Output : 3
    ```
    

- #### Modulus (%):
    It returns the remainder after dividing 'a' by 'b'.
    ```python
    print(a % b)
    # Output : 1
    ```
    

- #### Exponential (**):
    It means 'raise to the power of', i.e., 'a' raised to the power 'b'.
    ```python
    print(a ** b)
    # Output : 1000
    ```
    
---
  
### ⚖️ Comparison Operators:
Comparison operators (also called **relational operators**) are used to **compare two values**.
They return either `True` or `False` (Boolean result).


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

---

### 🔗 Logical Operators:
Logical operators are used to **combine conditional statements**. They return either `True` or `False` (Boolean result).


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
print(not(x > 2))        # False (because x > 2 is True, because 'not' inverts the result)
```

---

### ⚙️ Bitwise Operators:
Bitwise operators work on **binary (bit-level) representations** of numbers.


***Types of Bitwise Operators:***
| Operator | Name        | Description                              | Example | Result |
|----------|-------------|------------------------------------------|---------|--------|
| `&`      | AND         | Sets each bit to 1 if both bits are 1    | `5 & 3` | `1` |
| `\|`      | OR          | Sets each bit to 1 if one of the bits is 1 | `5 \| 3` | `7` |
| `^`      | XOR         | Sets each bit to 1 if only one bit is 1  | `5 ^ 3` | `6` |
| `~`      | NOT         | Inverts all the bits  | `~5` | `-6` |
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

---

### 🆔 Identity Operator:
Identity operators check whether **two objects are the same in memory**, not just equal in value.


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

---

### 🧩 Membership Operator:
Membership operators test whether a **value exists in a sequence** (string, list, tuple, etc.).


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

---

## 4️⃣ Control Flow in Python:
Control flow decides the order in which code executes.

### ✅ If-Else Statements:
In Python, `if-else` statements are **used for decision making**.
They allow your program to **execute certain code only if a condition is true**, and optionally execute another block if the condition is false.

***Syntax:***
```python
if condition:
    # code to run if condition is True
else:
    # code to run if condition is False
```

***Example:***
```python
age = 18

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# Output - "You are an adult."
```

***🌲 If-Elif-Else Chain:***

When you have multiple conditions, you can use **`elif`** (short for *else if*).

```python
marks = 75

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Grade: F")

# Output - "Grade: B"
```

---

### 🔁 Loops:
In Python, `loops` are used to **repeat a block of code multiple times** until a condition is met.
They help you avoid writing the same code again and again.

***🔄 for loop*** 

A for loop is used to **iterate over a sequence** (like a list, tuple, string, dictionary, or range) and execute a block of code for each element in that sequence.

It’s mainly used when you know **how many times you want to repeat something.**

***Syntax:***
```python
for i in sequence:
    # code block
```
 - Here, **i** is a **variable** that takes the value of each element in the sequence (one at a time).
 - And, **sequence** → the collection (list, string, range, etc.) you want to loop through.

***Example:***
```python
for i in range(5):
    print(i)

# Output:
0
1
2
3
4
```

***🔂 while loop***

A while loop in Python is used to **repeat a block of code as long as a condition is `True`**.
 - The condition is checked before each iteration.
 - If the condition becomes False, the loop stops.

***Syntax***
```python
while condition:
    # code block
```
**condition** → an expression that returns `True` or `False`.
 - If it’s True, the loop runs.
 - If it’s False, the loop ends.

***Example:***
```python
count = 0

while count < 5:
    print(count)
    count += 1

# Output:
0
1
2
3
4
```

***->Infinite Loop***

If the condition is **always True**, the loop will **never stop** unless a `break` is used.

```python
while True:
    print("This runs forever!")
    break
```

***🌀 Loop Control Statements:***

- **break** → Exits the loop immediately.  
- **continue** → Skips the current iteration and moves to the next one.  
- **pass** → Does nothing (used as a placeholder).  

***Example:***
```python
for i in range(5):
    if i == 2:
        continue  # skip 2
    if i == 4:
        break     # stop loop at 4
    print(i)

# Output:
0
1
3

```

***👉 Key Points***
- Use **for loop** when you know how many times to repeat.  
- Use **while loop** when you don’t know in advance and depend on a condition.  
- Loops make code **shorter, cleaner, and reusable**

---

## 🛠️ Python Functions:
Functions are **blocks of reusable code** that perform a specific task. They help in making programs **modular, maintainable, and readable**.

### 🤨 Why use functions?
- Avoids code repetition
- Makes code modular
- Increases readability
- Easy to debug and test
- Supports reusability

### ✍️ Defining a Function:
In Python, a function is defined using the `def` keyword.

Syntax:

```python
def function_name(parameters):
    """docstring (optional)"""
    # code block
    return value
```
