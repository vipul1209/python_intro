## Learning Python:
Following the tutorial here:
https://docs.python.org/3/tutorial/index.html


### Week 1 -
Read and walk through sections 1-3
1. Whetting Your Appetite
2. Using the Python Interpreter
2.1. Invoking the Interpreter
2.1.1. Argument Passing
2.1.2. Interactive Mode
2.2. The Interpreter and Its Environment
2.2.1. Source Code Encoding
3. An Informal Introduction to Python
3.1. Using Python as a Calculator
3.1.1. Numbers
3.1.2. Strings
3.1.3. Lists
3.2. First Steps Towards Programming

#### Excercise Week 1 -
Create a simple script that prints the paragraph below removing the letter s if it is at the end of a word. For example 'implementations' should be replaced by 'implementation'. The output should be the entire paragraph as a whole.

Extra Challenges:
- Incorporate a way to look for punctuation
- Print out the number of words that were altered

```python
paragraph = """
Python is an interpreted, high-level programming language for general-purpose programming. Created by Guido van Rossum 
and first released in 1991, Python has a design philosophy that emphasizes code readability, notably using significant 
whitespace. It provides constructs that enable clear programming on both small and large scales.[26] In July 2018, 
Van Rossum stepped down as the leader in the language community.[27][28]
Python features a dynamic type system and automatic memory management. It supports multiple programming paradigms, 
including object-oriented, imperative, functional and procedural, and has a large and comprehensive standard library.[29]
Python interpreters are available for many operating systems. CPython, the reference implementation of Python, 
is open source software[30] and has a community-based development model, as do nearly all of Python's other implementations. 
Python and CPython are managed by the non-profit Python Software Foundation.
"""

#This is the unchanged paragraph
print(paragraph)
```

The final output should be something like this:
```shell
****************************** - Before Change - ******************************

Python is an interpreted, high-level programming language for general-purpose programming. Created by Guido van Rossum
and first released in 1991, Python has a design philosophy that emphasizes code readability, notably using significant
whitespace. It provides constructs that enable clear programming on both small and large scales.[26] In July 2018,
Van Rossum stepped down as the leader in the language community.[27][28]
Python features a dynamic type system and automatic memory management. It supports multiple programming paradigms,
including object-oriented, imperative, functional and procedural, and has a large and comprehensive standard library.[29]
Python interpreters are available for many operating systems. CPython, the reference implementation of Python,
is open source software[30] and has a community-based development model, as do nearly all of Python's other implementations.
Python and CPython are managed by the non-profit Python Software Foundation.

------------------------------ - After Change - ------------------------------

Python i an interpreted, high-level programming language for general-purpose programming. Created by Guido van Rossum
and first released in 1991, Python ha a design philosophy that emphasize code readability, notably using significant
whitespace. It provide construct that enable clear programming on both small and large scales.[26] In July 2018,
Van Rossum stepped down a the leader in the language community.[27][28]
Python feature a dynamic type system and automatic memory management. It support multiple programming paradigms,
including object-oriented, imperative, functional and procedural, and ha a large and comprehensive standard library.[29]
Python interpreter are available for many operating system. CPython, the reference implementation of Python,
i open source software[30] and ha a community-based development model, a do nearly all of Python' other implementation.
Python and CPython are managed by the non-profit Python Software Foundation.

### There were a total of xx words altered ###

```
