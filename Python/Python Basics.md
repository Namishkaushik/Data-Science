# 🐍 Python Introduction:

Python is a **high-level, interpreted programming language** developed by ***Guido van Rossum in 1991***. It is widely used in Data Science because of its simplicity and powerful libraries.

---

## 1️⃣ Python Setup:
- Install **Python** from [python.org](https://www.python.org/) or use **Anaconda** for data science.  
- Use **Jupyter Notebook** or **Google Colab** for interactive coding.

---

## 2️⃣ Python Syntax:

### 🖨 Print & Comments:
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
Operators are special symbols in Python that perform operations on values or variables.
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
#### Addition (+):
It adds 'a' and 'b'
```python
print(a + b) 
```
👆 It basically means:
```python
print(10 + 3) # Assigned the values of 'a' and 'b'.
  # Answer - 13
```
#### Subtraction (-):
It subtracts 'b' from 'a'.
```python
print(a - b)
```
Now, it will assign the values of 'a' and 'b'.
```python
print(10 - 3)
  # Answer - 7
```
print(a * b)  # Multiplication - It multilies 'a' and 'b'.
print(a / b)  # Division - It divides 'a' from 'b'.
print(a // b) # Floor Division - It divides 'a' from 'b' and rounds the answer (towards negative infinity) to the nearest whole number.
print(a % b)  # Modulus - It returns the remainder after dividing 'a' by 'b'.
print(a ** b) # Exponential - It means 'raise to the power of', it multiplies 'a' by itself ,'b' number of times
```
In the above code bloc, we can see that we **assigned values** to **'a' and 'b'**. Then, we performed the **arithmetic operations on 'a' and 'b'**. 
So, basically this is what we are trying to do:
```python
print(10+3) # 
