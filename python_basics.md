# Python Tutorial


## Numbers and Math

Integers numbers have type `int`.
Fractional numbers have type `float`.

Python uses the basic arithmetic operators
> \+ - / *

Also uses special operators

> ** Exponential

> % Modulo > gives the remainder

>// Integer Division > Return an integer. By default division returns floats in python

## Variables and Strings

Variables hold a value in memory, and have a specific name. 
In Python variables can hold string, numbers, boolean values.

```python
x = 100
```
Variables can be assigned at the same time as other variables
```python
al, at, once = 5, 10, 15
```

### Naming Restrictions

1. Variables must start with a letter or underscore
2. The rest of the name must consist of letters, numbers os underscores.
3. Name are case-sensitive

### Naming Conventions
1. Use snake_case 
2. Use lowercase 
  CAPITAL_SNAKE_CASE usually refers to constants (PI = 3.14)
  UpperCamelCase refers to a class
  \_\_dunder__ or double underscores on both ends are supposed to be private or left alone 

### Data Types
|data type| description|
|---------| -----------|
|bool     | True or False|
|int| an integer number (1, 2, 3)|
|str| sequence of Unicode characters|
|list| an ordered sequence of values of other data types [1,2,3] (array)|
|dict|collection of key: values {"first_name":"Rene"} (object)|
|none| value null|


##### To check the type
```python
  some_string = 'hey'
  type(some_string) #class 'str'
```

---

### Strings

String literals can be declared using single or double quotes. We can use either one, but is good to stick with one of those.


#### String Escape Characters 

In Python there are also "escape characters", which are "metacharacters" - they get interpreted to do something special.

\n => insert new line
\' => insert single quotes
\" => insert double quotes
\\ => insert Backslash
