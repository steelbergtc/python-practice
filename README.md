# Python Practice
Code for Python Basics classes.

## Writing and Running Python
You need a place to write your Python code, and a place to run it.

To start off, we will write and run our code online from the web using https://trinket.io/python. But this only works in the short term, with quick and easy programs.

When you are ready to write and run things from your computer, follow the instructions at https://www.pythonlearn.com/install.php. There are recommendations and links for downloading a text editor (to write code) and an environment in which to run your Python code.
PythonLearn recommends TextWrangler as a text editor - but Sublime is another good one, as it color codes your code for you. You can download it here: https://www.sublimetext.com/download

## Some Terminology
- a **variable** is information given an identifier and stored for reuse by the program (ex: x = 5 -> x is the variable)
- a **conditional statement** tells the program perform different actions depending on whether specified conditions evaluate to true or false
- a **comment** is a line of code that is not read by the computer - it exists as information for humans reading the code (for example, to explain the purpose of sections of code). In Python, a comment must start with #

### Python Data Types
You can work with a variety of data types in Python: they each have their own context and limitations for use. Here are the Python data types, from Dive into Python 3:

Basic data types:

1. **Booleans** are either True or False.
2. **Numbers** can be **integers** (1 and 2), **floats** (1.1 and 1.2), **fractions** (1/2 and 2/3), or even **complex numbers**.
3. **Strings** are sequences of Unicode characters, e.g. a sentence or an html document.

More complex data types:

4. **Lists** are ordered sequences of values.
6. **Tuples** are ordered, immutable sequences of values.
7. **Sets** are unordered bags of values.
8. **Dictionaries** are unordered bags of key-value pairs.

See this helpful page from Dive into Python 3 for more: http://www.diveintopython3.net/native-datatypes.html

## Rock Paper Scissors Game
random is a module that we are importing to use in our program, in order to generate random numbers for the computer

**raw_input()** is a function that displays information (such as a question) and then gets input from the user - you can store this input it in an assigned variable

**.lower()** is a function that turns a string into lowercase

**while** is a conditional statement that means “as long as” - as long as a certain condition evaluates to true, the computer will continue to perform the desired action

**print()** prints the contents of the parentheses to the console

**if**, **elif**, and **else** form a conditional statement, which operate like branches from a tree of options, each with their own consequence depending on which branch is chosen

Once you have written and run the program, think about these questions:
- How might you make this code even better? What kind of improvements or adjustments might you want to make to this game?
- Now that you have programmed a rock, paper, scissors game, what do you think you would want to program next?

## Learn More
For free Python basics, check out:
- the interactive Python courses at Codecademy - https://www.codecademy.com/learn/python
- the readings and course materials at PythonLearn - https://www.pythonlearn.com/
- the readings and coding activities at Dive into Python 3: http://www.diveintopython3.net/index.html
