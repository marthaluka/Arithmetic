# Arithmetic

Just a package to demonstrate proper project stucturing in python.


Project structure:
---

```
$ pwd
~/src/python/Arithmetic/arithmetic

$ tree
.
├── divide.py
├── __init__.py
├── __main__.py
├── multiply.py
└── tests
    ├── __init__.py
    ├── __main__.py
    ├── test_divide.py
    └── test_multiply.py

```

### Running modules individually.

- Arithmetic: `python -m arithmetic`  
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
