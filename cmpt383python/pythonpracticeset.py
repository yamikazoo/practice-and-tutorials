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
for i in range(n := len(some_list)):
    break
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







