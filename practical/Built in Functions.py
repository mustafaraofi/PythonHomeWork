# 1. abs()
# Returns the absolute value of a number.
# Example:
# print(abs(-5))  # Output: 5

# 2. all()
# Returns True if all elements in an iterable are true (or if the iterable is empty).
# Example:
# print(all([True, True, False]))  # Output: False

# 3. any()
# Returns True if any element in an iterable is true. If the iterable is empty, returns False.
# Example:
# print(any([False, False, True]))  # Output: True

# 4. ascii()
# Returns a string containing a printable representation of an object. Non-ASCII characters are escaped.
# Example:
# print(ascii('äöü'))  # Output: '\xe4\xf6\xfc'

# 5. bin()
# Converts an integer number to a binary string prefixed with "0b".
# Example:
# print(bin(10))  # Output: '0b1010'

# 6. bool()
# Converts a value to a Boolean, using the standard truth testing procedure.
# Example:
# print(bool(0))  # Output: False

# 7. bytearray()
# Returns a bytearray object, which is a mutable sequence of bytes.
# Example:
# ba = bytearray('hello', 'utf-8')
# print(ba)  # Output: bytearray(b'hello')

# 8. bytes()
# Returns a new "bytes" object, which is an immutable sequence of bytes.
# Example:
# b = bytes('hello', 'utf-8')
# print(b)  # Output: b'hello'

# 9. callable()
# Returns True if the object appears callable, False if not.
# Example:
# def func():
#     pass
# print(callable(func))  # Output: True

# 10. chr()
# Returns the string representing a character whose Unicode code point is the integer passed.
# Example:
# print(chr(97))  # Output: 'a'

# 11. classmethod()
# Returns a class method for the given function.
# Example:
# class MyClass:
#     @classmethod
#     def my_class_method(cls):
#         return "This is a class method."
# print(MyClass.my_class_method())  # Output: 'This is a class method.'

# 12. compile()
# Compiles source into a code or AST object that can be executed by exec() or eval().
# Example:
# code = compile('a + b', '', 'eval')
# print(eval(code, {'a': 1, 'b': 2}))  # Output: 3

# 13. complex()
# Creates a complex number or converts a string or number to a complex number.
# Example:
# print(complex(2, 3))  # Output: (2+3j)

# 14. delattr()
# Deletes the named attribute from an object.
# Example:
# class MyClass:
#     a = 10
# obj = MyClass()
# delattr(obj, 'a')

# 15. dict()
# Creates a new dictionary.
# Example:
# d = dict(a=1, b=2)
# print(d)  # Output: {'a': 1, 'b': 2}

# 16. dir()
# Returns a list of valid attributes for the object.
# Example:
# print(dir([]))  # Output: List of methods/attributes for list objects

# 17. divmod()
# Takes two numbers and returns a pair of numbers (a tuple), consisting of their quotient and remainder.
# Example:
# print(divmod(7, 3))  # Output: (2, 1)

# 18. enumerate()
# Adds a counter to an iterable and returns it in the form of an enumerate object.
# Example:
# for i, value in enumerate(['a', 'b', 'c']):
#     print(i, value)
# Output:
# 0 a
# 1 b
# 2 c

# 19. eval()
# Parses the expression passed to it and runs Python expression (code) within the program.
# Example:
# x = 1
# print(eval('x + 1'))  # Output: 2

# 20. exec()
# Executes the Python code within the provided string or object.
# Example:
# code = """
# def greet():
#     print('Hello, World!')
# """
# exec(code)
# greet()  # Output: 'Hello, World!'

# 21. filter()
# Constructs an iterator from elements of an iterable for which a function returns true.
# Example:
# nums = [0, 1, 2, 3, 4]
# result = filter(lambda x: x > 2, nums)
# print(list(result))  # Output: [3, 4]

# 22. float()
# Returns a floating-point number from a number or string.
# Example:
# print(float('3.14'))  # Output: 3.14

# 23. format()
# Returns a formatted representation of a value controlled by format specifiers.
# Example:
# print(format(1234, ',d'))  # Output: '1,234'

# 24. frozenset()
# Returns a new frozenset object, which is an immutable set.
# Example:
# fs = frozenset([1, 2, 3])
# print(fs)  # Output: frozenset({1, 2, 3})

# 25. getattr()
# Returns the value of the named attribute of an object. If not found, it returns the default value provided.
# Example:
# class MyClass:
#     x = 10
# obj = MyClass()
# print(getattr(obj, 'x'))  # Output: 10

# 26. globals()
# Returns a dictionary representing the current global symbol table.
# Example:
# print(globals())  # Output: Global variables in the current context

# 27. hasattr()
# Returns True if the object has the named attribute, otherwise False.
# Example:
# class MyClass:
#     x = 10
# obj = MyClass()
# print(hasattr(obj, 'x'))  # Output: True

# 28. hash()
# Returns the hash value of an object if it has one.
# Example:
# print(hash('test'))  # Output: A hash value for the string 'test'

# 29. help()
# Invokes the built-in help system.
# Example:
# help(print)  # Output: Help information about the print function

# 30. hex()
# Converts an integer number to a lowercase hexadecimal string prefixed with "0x".
# Example:
# print(hex(255))  # Output: '0xff'

# 31. id()
# Returns the identity of an object. This is a unique integer for the object during its lifetime.
# Example:
# x = 5
# print(id(x))  # Output: An integer representing the identity of the object

# 32. input()
# Reads a line from input, converts it to a string, and returns it.
# Example:
# name = input('Enter your name: ')
# print('Hello, ' + name)

# 33. int()
# Converts a number or string to an integer, or returns 0 if no arguments are given.
# Example:
# print(int('10'))  # Output: 10

# 34. isinstance()
# Returns True if the object is an instance of the specified class(es) or their subclass.
# Example:
# print(isinstance(5, int))  # Output: True

# 35. issubclass()
# Returns True if a class is a subclass (direct, indirect or virtual) of a class or a tuple of classes.
# Example:
# class A:
#     pass
# class B(A):
#     pass
# print(issubclass(B, A))  # Output: True

# 36. iter()
# Returns an iterator object for the given object.
# Example:
# nums = [1, 2, 3]
# it = iter(nums)
# print(next(it))  # Output: 1

# 37. len()
# Returns the number of items in an object.
# Example:
# print(len('hello'))  # Output: 5

# 38. list()
# Creates a new list.
# Example:
# l = list([1, 2, 3])

# 39. locals()
# Returns a dictionary representing the current local symbol table. This dictionary updates automatically to reflect changes in the local variables.
# Example:
# def func():
#     a = 10
#     b = 20
#     print(locals())
# func()
# Output: {'a': 10, 'b': 20}

# 40. map()
# Applies a given function to all items in an iterable (e.g., list) and returns a map object (which is an iterator).

# Example:
# nums = [1, 2, 3, 4]
# result = map(lambda x: x * 2, nums)
# print(list(result))  # Output: [2, 4, 6, 8]

# 41. max()
# Returns the largest item in an iterable or the largest of two or more arguments.

# Example:
# print(max(1, 5, 3))  # Output: 5

# 42. memoryview()
# Returns a memory view object from an object that supports the buffer protocol (like bytes and bytearray). This allows Python code to access the internal data of an object that supports the buffer protocol without copying it.

# Example:
# b = bytearray('ABC', 'utf-8')
# mv = memoryview(b)
# print(mv[0])  # Output: 65 (ASCII value of 'A')

# 43. min()
# Returns the smallest item in an iterable or the smallest of two or more arguments.

# Example:
# print(min(1, 5, 3))  # Output: 1
# 44. next()
# Retrieves the next item from an iterator. If a second argument is provided, it returns that value if the iterator is exhausted; otherwise, it raises a StopIteration exception.

# Example:
# nums = iter([1, 2, 3])
# print(next(nums))  # Output: 1
# print(next(nums))  # Output: 2

# 45. object()
# Returns a new featureless object. object is a base for all classes, and all classes in Python inherit from object.

# Example:
# obj = object()
# print(obj)  # Output: <object object at 0x...>

# 46. oct()
# Converts an integer to an octal string prefixed with "0o".

# Example:
# print(oct(8))  # Output: '0o10'

# 47. open()
# Opens a file and returns a file object, which can be used to read, write, and perform other file operations.

# Example:
# with open('example.txt', 'w') as file:
#     file.write('Hello, World!')

# 48. ord()
# Returns an integer representing the Unicode code point of the given Unicode character.

# Example:
# print(ord('a'))  # Output: 97

# 49. pow()
# Returns the value of x raised to the power y (x**y). If z is present, returns x**y % z.

# Example:
# print(pow(2, 3))  # Output: 8
# print(pow(2, 3, 5))  # Output: 3

# 50. print()
# Prints the given object(s) to the standard output device (e.g., the console).

# Example:
# print('Hello, World!')  # Output: Hello, World!

# 51. property()
# Returns a property attribute that can be used to manage the access to instance variables.

# Example:
# class MyClass:
#     def __init__(self, value):
#         self._value = value

#     @property
#     def value(self):
#         return self._value

#     @value.setter
#     def value(self, new_value):
#         self._value = new_value

# obj = MyClass(10)
# print(obj.value)  # Output: 10
# obj.value = 20
# print(obj.value)  # Output: 20

# 52. range()
# Returns an immutable sequence of numbers, commonly used in loops.

# Example:
# for i in range(5):
#     print(i)
# Output:
# 0
# 1
# 2
# 3
# 4

# 53. repr()
# Returns a string containing a printable representation of an object. Often used for debugging.

# Example:
# print(repr('Hello'))  # Output: "'Hello'"

# 54. reversed()
# Returns a reverse iterator for a given sequence.

# Example:
# nums = [1, 2, 3]
# print(list(reversed(nums)))  # Output: [3, 2, 1]

# 55. round()
# Rounds a number to a specified number of decimal places. If no decimal places are specified, it rounds to the nearest integer.

# Example:
# print(round(3.14159, 2))  # Output: 3.14

# 56. set()
# Creates a new set object, which is an unordered collection of unique elements.

# Example:
# s = set([1, 2, 3, 3])
# print(s)  # Output: {1, 2, 3}

# 57. setattr()
# Sets the value of the named attribute of an object.

# Example:
# class MyClass:
#     x = 10

# obj = MyClass()
# setattr(obj, 'x', 20)
# print(obj.x)  # Output: 20

# 58. slice()
# Returns a slice object, which can be used to slice sequences such as lists, strings, etc.

# Example:
# lst = [0, 1, 2, 3, 4]
# s = slice(1, 3)
# print(lst[s])  # Output: [1, 2]

# 59. sorted()
# Returns a new sorted list from the elements of any iterable.

# Example:
# nums = [3, 1, 2]
# print(sorted(nums))  # Output: [1, 2, 3]

# 60. staticmethod()
# Returns a static method for the given function. A static method does not receive an implicit first argument.

# Example:
# class MyClass:
#     @staticmethod
#     def greet():
#         print("Hello, World!")

# MyClass.greet()  # Output: 'Hello, World!'

# 61. str()
# Returns a string version of an object.

# Example:
# print(str(123))  # Output: '123'

# 62. sum()
# Sums the items of an iterable and returns the total.

# Example:
# print(sum([1, 2, 3]))  # Output: 6

# 63. super()
# Returns a proxy object that delegates method calls to a parent or sibling class of type.

# Example:
# class Parent:
#     def greet(self):
#         print("Hello from Parent")

# class Child(Parent):
#     def greet(self):
#         super().greet()
#         print("Hello from Child")

# c = Child()
# c.greet()
# Output:
# Hello from Parent
# Hello from Child

# 64. tuple()
# Creates a new tuple, which is an immutable sequence.

# Example:
# t = tuple([1, 2, 3])
# print(t)  # Output: (1, 2, 3)

# 65. type()
# Returns the type of an object. It can also be used to create a new class.

# Example:

# python
# Copy code
# print(type(123))  # Output: <class 'int'>

# 66. vars()
# Returns the __dict__ attribute of an object, which is a dictionary representing the object’s (writable) symbol table.

# Example:
# class MyClass:
#     def __init__(self):
#         self.a = 10
#         self.b = 20

# obj = MyClass()
# print(vars(obj))  # Output: {'a': 10, 'b': 20}

# 67. zip()
# Returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences.

# Example:
# a = [1, 2, 3]
# b = ['a', 'b', 'c']
# print(list(zip(a, b)))  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]

# 68. __import__()
# This function is used by the import statement and is called by it to import a module. Normally, you won’t need to use it directly.

# Example:
# math = __import__('math')
# print(math.sqrt(4))  # Output: 2.0