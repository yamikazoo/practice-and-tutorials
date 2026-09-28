import time
# Q1
# a list comprehension is a way to apply a transformation to every element in a list
# for example, say you have list of ints called nums, and you want to square every number in the list
# you would write [x**2 for x in nums]
# its syntax is inspired from set notation in math: {x^2: x E X}
# could also parse it as {transformation separator meaning conditional}

# q2
# all numbers from 1 to 100 that are multiples of 5
string_list = ["dog","cat","cot","popsicle","decision"]
some_list = [1, 2, 3, 4, 0, 8]
third_list = [1, 3, 5, 6, 9, 10]
q2a = [x for x in range(1, 101) if x % 5 == 0]
q2b = [x for x in string_list if len(x) % 2 != 0]
q2c = [x + 1 if x < 0 else x - 1 for x in some_list if x != 0]
q2d = [(w, x, y, z) for w in (0,1) for x in (0,1) for y in (0,1) for z in (0,1)]
q2e = [(a, b, c) for a in string_list for b in some_list for c in third_list if a != b and b!= c and a != c]
q2f = [(a, b, c) for a in range(1, 101) for b in range(1, 101) for c in range(1, 101) if a**2 + b**2 == c**2]

# q3
# walrus operator or assignment expression allows you to create and define variables directly inside loops and if statements
# it is used for storing the result of particularly computationally expensive operations that get referenced repeatedly
# and since python is not lazy, those operations will get evaluated everytime. a walrus operator removes the need for that redundant computation
# example
#for i in range(n := len(some_list)):
#    break
# n now holds len of list, saving a line of code and as well reducing the need to check len() every loop

# q4a 
def my_zip2(A, B):
    res = []
    i = 0
    while i < min(len(A), len(B)):
        res.append((A[i], B[i]))
        i += 1
    return res

#q4b
def dot_product(A, B):
    total = []
    zipped = my_zip2(A, B)
    for x, y in zipped:
        total.append(x * y)

    return sum(total)

#q4c
def my_zip(*lists):
    if len(lists) < 2:
        raise ValueError("Less than 2 lists")
    else:
        res = []
        # size of one list
        list_len = len(lists[0])

        for i in range(list_len):
            the_tuple = ()
            for j in lists:
                the_tuple = (*the_tuple, j[i])
            res.append(the_tuple)

    return res

#q4d
def add_lists(*lists):
    # when *lists for N lists, arguments becomes tuple of lists
    res = []
    # unpack the tuple of lists into individual lists
    tuples = my_zip(*lists)
    for i in tuples:
        res.append(sum(i))

    return res

#q5 
def make_numbered_list(lst):
    res = ""
    for i, value in enumerate(lst):
        count = i + 1
        res.append(count + ". " + value + "\n")
    return res

def make_numbered_list2(lst):
    res = "\n".join([f"{i}. {item}" for i, item in enumerate(lst, start = 1)])
    # list comprehension with enumerate as the loop in the comprehension
    return res

#q6
# return the largest value in the list
def get_max(lst):
    max_value = lst[0]

    for _, value in enumerate(lst):
        if value > max_value:
            max_value = value

    return max_value

# iterator prac
class my_reversed:
    def __init__(self, lst):
        self.list = lst
        self.index = len(lst) - 1

    def __iter__(self):
        return self

    def __next__(self):
        # if not at end, decrement to new end and then return the current value (technically previous)
        if self.index >= 0:
            self.index -= 1
            return self.lst[self.index + 1]
        # otherwise at end
        else: 
            raise StopIteration

#q7 Python's iterator protocol is essentially a set of rules or behavior that take effect
# when you define a class that implement the __iter__ and __next__ methods. 
# the protocol essentially allows you to iterate over an iterable by loading one element from the iterable
# into memory at one time, instead of loading in the entire iterable into memory that python does because it is not lazy
# when there is no more data to iterate over, the protocol states it should raise the StopIteration exception

#q8 
# iterator class that iterates over a string in reverse order
class My_reversed:
    def __init__(self, s):
        self.s = s
        self.index = len(s) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= 0:
            # reduce index count
            self.index -= 1
            # return the prev (techinically current) letter
            return self.s[self.index + 1]
        else:
            raise StopIteration

#for i in My_reversed("cat"):
 #   print(i)

#q9 python strings are iterable, meaning they can be iterated over because they implement __iter__,
# but they are not iterators as the backend implementation of the string class does not implement
# __next__

#q10
# enumerate class using iterator protocol
class My_enumerate:
    def __init__(self, lst):
        self.lst = lst
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.lst):
            # store val in temp
            res = (self.index, self.lst[self.index])
            
            # increment index
            self.index += 1

            # return temp
            return res
        else:
            raise StopIteration
    
#q11 generator funcs
def my_range_gen(a, b):
    ptr = a
    while ptr < b:
        yield ptr
        ptr += 1

def my_zip2_gen(A, B):
    index = 0
    while index < len(A):
        yield(A[index], B[index])
        index += 1

#q12 - gens all the strings longer than n in lst
def longer_than_gen(n, lst):
    for s in lst:
        if len(s) > n:
            yield(s)

#q13
def lines_of_file_gen(filename):
    # 'with' automatically handles closing the file when the generator finishes
    with open(filename, 'r') as f:
        # We can use enumerate to automatically track the index starting at 0
        for i, line in enumerate(f):
            # line.strip('\n') removes the hidden newline character from the file
            # so that your print() statement doesn't cause double-spacing
            yield i, line.strip('\n')

#q14 closure
# rules: there must be a nested function, the inner function must reference a variable in the outer scoper
# the outer function must return the inner function
def make_bounds_checker(min, max):
    def bounds_checker(val):
        return val >= min and val <= max
    return bounds_checker

#q15 decorator
# a decorator in simple terms is a function that wraps another function and provides additional funcitonality to it
# without editing the source code of the original function
# use one when you want to add some functionality to a function, but creating a decorator function
# that takes a function as input and using @decorator_name above the function you want to wrap
# The Decorator
def my_logger(func):
    def wrapper():
        print("Starting the function...")
        func()  # Calls the original function
        print("Finished the function!")
    return wrapper

# Using the Decorator
@my_logger
def say_hello():
    print("Hello, world!")
    
# Calling it
# say_hello()

# q16
def always_return_str(f):
    def return_str(*args, **kwargs):
        res = f(*args, **kwargs)
        return str(res)
    return return_str

# q17 context manager
class LoggedTimer:
    def __init__(self, filename):
        self.filename = filename
        self.start_time = 0
        # We will store the file object here so all methods can use it
        self.file = None 

    def __enter__(self):
        # 1. Open the file in write mode ('w')
        self.file = open(self.filename, 'w')
        
        # 2. Record the exact start time
        self.start_time = time.time()
        
        # 3. Write the starting timestamp to the file
        self.file.write(f"Started at {self.start_time}\n")
        
        # 4. Return self so it gets assigned to 't' in the 'with' block
        return self

    def log(self, message):
        # Write the custom message to the file with a newline
        self.file.write(f"{message}\n")

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 1. Record the exact stop time
        stop_time = time.time()
        
        # 2. Calculate the difference
        elapsed = stop_time - self.start_time
        
        # 3. Write the final stats to the file
        self.file.write(f"Stopped at {stop_time}\n")
        self.file.write(f"Elapsed: {elapsed:.3f} seconds\n")
        
        # 4. Safely close the file
        self.file.close()
        
        # 5. Print the confirmation to the console
        print(f"Logged to {self.filename}")
    



  
    






