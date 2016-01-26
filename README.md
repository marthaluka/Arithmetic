# Arithmetic

Just a package to demonstrate proper project stucturing in python.


Project structure:
---

```
$ pwd
~/src/python/Arithmetic/arithmetic

$ tree
.
├── arithmetic
│   ├── division
│   │   ├── divide.py
│   │   ├── __init__.py
│   │   ├── __main__.py
│   │   └── __pycache__
│   ├── __init__.py
│   ├── __main__.py
│   ├── multiplication
│   │   ├── __init__.py
│   │   ├── __main__.py
│   │   ├── multiply.py
│   │   └── __pycache__
│   └── tests
│       ├── division
│       │   └── test_divide.py
│       ├── __init__.py
│       ├── __main__.py
│       └── multiplication
│           └── test_multiply.py

```

### Running modules individually.

- Arithmetic: `python -m arithmetic`  
- Division: `python -m arithmetic.division`  
- Multiplication: `python -m arithmetic.multiplication`  
- Tests: `python -m arithmetic.tests`  

However the following for example fails.
How can I make them work and is it necessary?  
``` bash
$ python arithmetic/tests/test_divide.py 
Traceback (most recent call last):
  File "arithmetic/tests/test_divide.py", line 2, in <module>
    import arithmetic.divide as divide
ImportError: No module named 'arithmetic'


$ python arithmetic/tests/test_multiply.py 
Traceback (most recent call last):
  File "arithmetic/tests/test_multiply.py", line 1, in <module>
    import arithmetic.multiply as multiply
ImportError: No module named 'arithmetic'
```
