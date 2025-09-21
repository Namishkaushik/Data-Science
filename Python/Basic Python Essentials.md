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

### 🖨 print() & Comments:
`print()` is a **built-in function** in Python that **outputs text, numbers, variables, or any other data** to the standard output device (usually your monitor). <br>
While, a `comment` is a line in the code that Python **ignores** while running the program.
```python
# This is a comment
print("Hello, Data Science!")  # Prints text
```

### 📥 input() function:
`input()` is a **built-in function** that:
- Displays a prompt message (optional).
- Waits for the user to type something.
- Returns the input as a string.

**Example:**
```python
name = input("Enter your name: ")
print("Hello,", name)
```
If user types **Namish**, the output will be:

```python
Enter your name: Namish
Hello, Namish
```

You can also add data types in front of input, to restrict the entry of the data to a particular data type.

**For Example:**
```python
age = int(input("Enter the age: "))
print("The age is:", age)
```
This will now take the input only in integer form.

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

### 🔹 f-string:
An **f-string** lets you embed variables and expressions inside a string using `{ }`.

```python
name = "Namish"
age = 19
print(f"My name is {name} and I am {age} years old.")


# Output : My name is Namish and I am 19 years old.
```
You can also evaluate expressions,
```python
a = 5
b = 3
print(f"{a} + {b} = {a+b}")



# Output : 5 + 3 = 8

```

### Q. What is string?
A **string** is just a sequence of characters.

Characters can be:
- Letters → `"a"`, `"hello"`
- Numbers (as text) → `"123"`
- Symbols → `"@#$"`
- Even spaces → `" "`

### Slicing:
Slicing in Python is a **way to extract a portion (substring, sublist, or subsequence) from a sequence** like a string, list, or tuple.

The syntax is:
```python
sequence[start:end:step]
```
- **start** → Index to start from (inclusive).
- **end** → Index to stop at (exclusive).
- **step** → How many steps to move after each element. Can be negative.

**For Example:**
```python
s = "Python"

print(s[0:4])    # 'Pyth'  → from index 0 to 3
print(s[2:])     # 'thon'  → from index 2 to end
print(s[:4])     # 'Pyth'  → from start to index 3
print(s[::2])    # 'Pto'   → every 2nd character
print(s[::-1])   # 'nohtyP' → reversed string
```
You can do the same with List and Tuple.

So, **slicing is just a way to pick parts of a sequence** using indices, and with the step parameter you can even reverse it!


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

## 4️⃣ Data Structures in Python:
Data Structures are **ways to organize and store data** so that they can be used efficiently.  
Python provides several built-in data structures, and you can also create custom ones.

### 🔹 Types of Data Structures

1. **Primitive Data Structures**  
   - Integers (`int`)  
   - Floats (`float`)  
   - Strings (`str`)  
   - Booleans (`bool`)  

2. **Non-Primitive (or Abstract) Data Structures**  
   - Built-in: **List, Tuple, Set, Dictionary**  
   - User-defined: **Stack, Queue, Linked List, Tree, Graph, Hash Table**

### 🟦 Lists

- A **list** in Python is an **ordered, mutable (changeable), and iterable collection** that can hold items of different data types (integers, strings, floats, objects, even other lists). Lists are one of Python’s most commonly used data structures.  

- It is defined with `[]`.

- Use when you need ordered collection with flexibility.

Some common operations:-
```python
fruits = ["apple", "banana", "cherry"]  # Defining a list.
# ['apple', 'banana', 'cherry']

# --- Adding ---
fruits.append("mango")   # It adds "mango" at the last.
# ['apple', 'banana', 'cherry', 'mango']

fruits.insert(1, "orange")   # It inserts "orange" at index '1'.
# ['apple', 'orange', 'banana', 'cherry', 'mango']

# --- Removing ---
fruits.remove("banana")   # removes by value
# ['apple', 'orange', 'cherry', 'mango']

popped = fruits.pop()     # removes last element ("mango")
# ['apple', 'orange', 'cherry']

del fruits[0]             # deletes element at index 0 ("apple")
# ['orange', 'cherry']

# --- Updating ---
fruits[1] = "grapes"      # modifies element at index 1
# ['orange', 'grapes']

# --- Checking ---
print("apple" in fruits)  
# False  (since "apple" was deleted earlier)
```
---
---
> ***Q. What is list comprehension?***
>> **List comprehension** is a concise way to create lists in Python using a **single line of code**.
>>
>>Instead of writing a loop + append, you can generate lists directly inside square brackets.
>>
>> **Syntax:**
>>```python
>>[expression for item in iterable if condition]
>>```
>> - **expression** → What to store in the list
>> - **item** → Variable that takes values from the iterable.
>> - **iterable** → A sequence (list, string, range, etc.)
>> - **condition** (optional) → Filters which items to include.
>> 
>> **Examples:**
>> 1. Squares of numbers(1-5): 
>>```python
>>squares = [x**2 for x in range(1, 6)]
>>print(squares)   # [1, 4, 9, 16, 25]
>>```
>> 
>> 2. Even numbers from 1 - 10:
>>```python
>>evens = [x for x in range(1, 11) if x % 2 == 0]
>>print(evens)   # [2, 4, 6, 8, 10]
>>```
>> 3. First letters of words:
>>```python
>>words = ["apple", "banana", "cherry"]
>>first_letters = [w[0] for w in words]
>>print(first_letters)   # ['a', 'b', 'c']
>>```
>>
>> 4. Flatten a nested list:
>>```python
>>matrix = [[1,2],[3,4],[5,6]]
>>flat = [num for row in matrix for num in row]
>>print(flat)   # [1, 2, 3, 4, 5, 6]
>>```

---
---

### 🟨 Tuples
- A **tuple** is a built-in Python data structure that is very *similar to a list*, but with one key difference: **tuples are immutable** (the values cannot be changed).
- They are **faster then list** as they are immutable.
- It is defined with `()`.
- Use when data should not change (like constants, coordinates).

Some common operations:
```python
# Defining a tuple
fruits = ("apple", "banana", "cherry", "apple")

# --- Accessing ---
print(fruits[0])       # apple  (first element)
print(fruits[-1])      # cherry (last element)
print(fruits[1:3])     # ('banana', 'cherry') (slicing)

# --- Checking ---
print("apple" in fruits)   # True
print("mango" in fruits)   # False

# --- Counting & Index ---
print(fruits.count("apple"))   # 2 (number of times "apple" appears)
print(fruits.index("banana"))  # 1 (first index of "banana")

# --- Length ---
print(len(fruits))   # 4

# --- Concatenation ---
t1 = (1, 2, 3)
t2 = (4, 5)
print(t1 + t2)       # (1, 2, 3, 4, 5)

# --- Repetition ---
print(t1 * 2)        # (1, 2, 3, 1, 2, 3)

# --- Nesting ---
nested = (t1, t2)
print(nested)        # ((1, 2, 3), (4, 5))

# --- Converting to List (to modify) ---
temp = list(fruits)
temp[1] = "grapes"
fruits = tuple(temp)
print(fruits)        # ('apple', 'grapes', 'cherry', 'apple')
```

### 🟩 Sets
- A **set** is a built-in **unordered collection of unique elements**.
- It is **mutable** and **hetrogeneous**.
- Use when you need unique elements or set operations (union, intersection).
- Defined with `{}`

Creating a list:
```python
# Using curly braces
my_set = {1, 2, 3, 4}

# Using set() function
another_set = set([1, 2, 2, 3, 4])  
print(another_set)  # {1, 2, 3, 4}
```
Some common operations:
```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Add element
A.add(10)

# Remove element
A.remove(2)   # Throws error if element not found
A.discard(100)  # Safe remove, no error if not found

# Union (combine elements)
print(A | B)  # {1, 3, 4, 5, 6, 10}

# Intersection (common elements)
print(A & B)  # {3, 4}

# Difference (elements in A but not in B)
print(A - B)  # {1, 10}

# Symmetric Difference (elements in A or B but not both)
print(A ^ B)  # {1, 5, 6, 10}

# Membership
print(3 in A)     # True
print(7 not in A) # True
```

### 🟥 Dictionaries
A **dictionary** is a built-in Python data structure that **stores data as key–value pairs**. It is:
- **Unordered* (Python 3.6+ maintains insertion order, but logically dicts are unordered)
- **Mutable** (can add, remove, or update items)
- **Indexed by keys** (not positions like lists/tuples)
- **Unique keys** (each key must be unique, but values can repeat)
- **Use when you need mapping** (like ID → Data, word → meaning)
- Defined by `{}`



Some common functions:
```python
# Defining a dictionary
student = {"name": "Namish", "age": 20, "course": "Python"}

# --- Accessing ---
print(student["name"])         # Namish
print(student.get("age"))      # 20
print(student.get("grade", "N/A"))  # N/A (default if key not found)

# --- Adding / Updating ---
student["age"] = 21            # Update value
student["city"] = "Delhi"      # Add new key-value pair
# {'name': 'Namish', 'age': 21, 'course': 'Python', 'city': 'Delhi'}

# --- Removing ---
student.pop("course")          # Removes 'course'
del student["city"]            # Removes 'city'
removed = student.popitem()    # Removes last inserted pair (tuple)
student.clear()                # Empties dictionary

# --- Checking ---
print("name" in student)       # True (checks key)
print("Namish" in student.values())  # True (checks value)

# --- Looping ---
student = {"name": "Namish", "age": 20, "course": "Python"}
for key in student:
    print(key, student[key])   # Access by key

for key, value in student.items():
    print(f"{key}: {value}")

# --- Useful Functions ---
print(student.keys())     # dict_keys(['name', 'age', 'course'])
print(student.values())   # dict_values(['Namish', 20, 'Python'])
print(student.items())    # dict_items([('name', 'Namish'), ('age', 20), ('course', 'Python')])

print(len(student))       # 3
```

### 🟪 Stack
A **stack** is a **linear data structure** that follows the principle:

👉 **LIFO (Last In, First Out)**
- The last element added (pushed) is the first one removed (popped).
- Imagine a stack of plates: you put one on top, and the last plate placed is the first one you take off.

✅ **Stack Operations:**
- Push → Add an element to the top
- Pop → Remove the top element
- Peek / Top → View the top element without removing it
- isEmpty → Check if the stack is empty

📌 **Implementation using List:**
```python
stack = []  # empty stack

# Push
stack.append(10)
stack.append(20)
stack.append(30)
print("Stack after pushes:", stack)  
# [10, 20, 30]

# Pop
print("Popped:", stack.pop())  # 30
print("Stack now:", stack)     # [10, 20]

# Peek (last element)
print("Top element:", stack[-1])  # 20

# Check if empty
print("Is stack empty?", len(stack) == 0)  # False
```
📌 **Implementation using collections.deque**
```python
from collections import deque

stack = deque()

# Push
stack.append(1)
stack.append(2)
stack.append(3)
print("Stack after pushes:", stack)  
# deque([1, 2, 3])

# Pop
print("Popped:", stack.pop())  # 3
print("Stack now:", stack)     # deque([1, 2])
```

---
>**🌀 collections.deque in Python**
>>A deque (pronounced "deck") stands for Double-Ended Queue.
>>>It’s a generalized queue from Python’s collections module that allows fast appends and pops from both ends. 
---

### 🟧 Queue 
A **queue** is a linear data structure that follows the **FIFO (First In, First Out)** principle, i.e, The **first element added** is the **first one removed**.

**Characteristics of a Queue:**
- **Insertion (enqueue)** happens at the **rear (end)**.
- **Deletion (dequeue)** happens at the **front (start)**.
- Useful in scheduling, order processing, BFS (breadth-first search), etc.
- Use for task scheduling, printers, order processing.

**1. Implementing a Queue in Python**
```python
queue = []

# Enqueue (add at rear)
queue.append("A")
queue.append("B")
queue.append("C")
print(queue)  # ['A', 'B', 'C']

# Dequeue (remove from front)
print(queue.pop(0))  # A
print(queue)         # ['B', 'C']

```

**2. Using collections.deque (Recommended ✅)**
```python
from collections import deque

queue = deque()

# Enqueue
queue.append("A")
queue.append("B")
queue.append("C")
print(queue)  # deque(['A', 'B', 'C'])

# Dequeue
print(queue.popleft())  # A
print(queue)            # deque(['B', 'C'])
```
- `deque` is faster then `list` for queues.

**3. Using queue.Queue (for multi-threading)**
```python
from queue import Queue

q = Queue()

# Enqueue
q.put("A")
q.put("B")
q.put("C")

# Dequeue
print(q.get())  # A
print(q.get())  # B
```


## 5️⃣ Control Flow in Python:
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

##  6️⃣ Python Functions:
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
### 📞 Calling a Function:
```python
def greet():
    print("Hello, Python!")

greet()  # Function call
```
Here, we defined a function called **greet()** in the first line. So, when we called it in the last line, it will go back to the funtion and print whatever was defined in it. 

Like in this example, when we call the greet() function, it will print - ```Hello, Python!``` - as it was defined in the function.

### 📦 Functions with Parameters:
In Python finctions, **Parameters** are the <u>variables</u> that are defined in a function to **accept input values** when the function is called. They act as placeholders for the data you want the function to work with.


While **Argument** is the actual value passed when calling a function.

```python
def greet(name): # name - parameter
    print(f"Hello, {name}!")

greet("Namish") # Namish - argument

# Output:
Hello, Namish!
```
Here, we defined a parameter called "name". And then we passed the argument "Namish" while calling the function.

### ⚡ Function with return value:
```python
def add(a, b):
    return a + b # return statement used

result = add(5, 10)
print("Sum:", result)

# Output:
Sum: 15
```
###  📝 Types of Function Argumens:
There are several types of Arguments :-
1. ***Positional Arguments:***
    - The values a passed in order, matching the function's parameters.
    - **Order matters**
    ```python
    def divide(a, b):
        return a / b

    print(divide(10, 2))  

    # Output:
    5.0
    ```
2. ***Keyword Arguments:***
    - Values are passed using *Parameter values*
    - **Order doesn't matter**
    ```python
    def student(name, age):
        print(f"Name: {name}, Age: {age}")

    student(age=20, name="Namish")

    # Output:
    # Name: Namish, Age: 20
    ```
3. ***Default Arguments:***
    - Parameters can have **default values**
    - If no argument is passed, then the default value is used.
    ```python
    def power(base, exp=2):
    return base ** exp

    print(power(5))    
    print(power(5, 3)) 

    # Output:
    25
    125
    ```
4. ***Variable - Length Arguments:***
    - They are used when you **don't know** in advanced, that **how many arguments will be passed**.
    - ```*args``` (arguments) is used in function definitions to allow the function to **accept any number of positional arguments** and **pack them in a tuple** called ```args```.<br>
    - ```**kwargs```(keyword arguments) is used in function defination to allow the function to **accept any number of named arguments** and **packs them in a dictionary** called ```kwargs```.
    
    <u>**Example-1:  (*args)**</u>
    ```python
    def sum_all(*args):
    return sum(args)

    print(sum_all(1, 2, 3, 4, 5)) 

    # Output:
    15
    ```
    <u>**Example-2: (*args)**</u>
    ```python
    def greet_all(*names):
    for name in names:
        print(f"Hello, {name}!")

    greet_all("Namish", "Karan", "Lucky")

    # Output:

    # Hello, Namish!
    # Hello, Karan!
    # Hello, Lucky!
    ```
    <u>**Example-3 (\**kwargs)**</u>
    ```python
    def student_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

    student_info(name="Namish", age=20, course="Python")

    # Output:
    # name: Namish
    # age: 20
    # course: Python

    ```

### 🎭 Anonymous Function(Lambda):
An **anonymous function** in Python, also called a **lambda** function, is a *small, unnamed function* defined using the ```lambda``` keyword. Unlike regular functions defined with def, a **lambda function can have any number of arguments** but **only a single expression**, whose result is automatically returned. Lambda functions are typically used for short, throwaway operations, often as arguments to higher-order functions like map(), filter(), and reduce().

**Syntax:**
```python
lambda arguments: expression
```
**Example:**
```python
square = lambda x: x ** 2
print(square(5))  

# Output: 25
```

### 🎯 Nested Functions:
A **nested function** is a function **defined inside another function.**

The outer function can call the inner one, and the inner function can access variables from the outer function (thanks to enclosing scope).
```python
def outer():
    message = "Hello from outer!"

    def inner():
        print(message)  # inner() can access outer()'s variable

    inner()  # Call inner function

outer()


# Output: Hello from outer!
```

### 🏛️ Scope of Variables:
The **scope of a variable** refers to the region of the program where that variable is **accessible and can be used**.

Python follows the LEGB rule to decide the scope:
- **L - Local Variable** - Variables defined inside a function, accessible only within that function.
    ```python
    def func():
        x = 10  # Local variable
        print(x)

    func()
    print(x)  # ❌ Error: x not accessible outside
    ```
- **E - Enclosing Scope** - Variables in the outer (enclosing) function for nested functions.
    ```python
    def outer():
        y = 20
        def inner():
            print(y)  # Access enclosing variable
        inner()

    outer()  # Output: 20
    ```
- **G - Global Variable** - Variables defined at the top level of a script or module, accessible anywhere inside functions (if not shadowed).
    ```python
    z = 30  # Global variable

    def show():
        print(z)

    show()  # Output: 30
    print(z) # Output: 30 (As it is accesible outside)
    ```
- **B - Built-in Scope** - Names pre-defined by Python (like len, print, range).
    ```python
    print(len([1, 2, 3]))  # len is from built-in scope
    ```

### 🌍 global and nonlocal Keywords:
1. **global keyword** 
- The ```global``` keyword is used to **access and modify a variable that is defined in the global scope** (outside all functions).
- <u>Without ```global```</u>, assigning to a variable inside a function will create a <u>local variable</u> instead of changing the global one.
    ```python
    x = 10  # Global variable

    def modify():
        global x
        x = 20  # Modifies the global variable

    modify()
    print(x)  # Output: 20
    ```
2. **nonlocal keyword** 
- The ```nonlocal``` keyword is used inside nested functions to **modify a variable from the enclosing (outer) function scope**, not the global scope.
    ```python
    def outer():
        y = 5
        def inner():
            nonlocal y
            y = 10  # Modifies the variable from outer function
        inner()
        print(y)

    outer()  # Output: 10
    ```

### 🌀 Recursion:
It is basically a function calling itself.
```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # 120
```

### Built-in functions:
- **len()** → Length of object
- **max(), min()** → Largest and smallest
- **sum()** → Sum of iterable
- **sorted()** → Sorts a sequence
- **map(), filter(), reduce()** → Functional programming tools

Example:
```python
nums = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x**2, nums))
evens = list(filter(lambda x: x % 2 == 0, nums))

print("Squares:", squares)
print("Evens:", evens)
```
