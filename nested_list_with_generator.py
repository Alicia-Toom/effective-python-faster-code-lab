import itertools
import memory_profiler


my_nest_list = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10,
                    11, 12, 13, 14]]
my_nest_tuple = ((0, 1, 2, 3, 4), (5, 6, 7, 8, 9), (10,
                11, 12, 13, 14))

@memory_profiler.profile
def nested_list():
    """a. Using generator Let’s create my_nest_list that
    has 3 numbers of list from 0-4 ,5-9 and 10-14. output:
    [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10,
    11, 12, 13, 14]]

    """
    for i in my_nest_list:
        yield i

@memory_profiler.profile
def double_nested_list():
    """b. Using list comprehension create a list of double value of
    even numbers in my_nest_list. output:
    [[0, 4, 8], [12, 16], [20, 24, 28]]

    """
    return [[j * 2 for j in i if j % 2 == 0] for i in my_nest_list]

@memory_profiler.profile
def double_value_nested_list():
    """c. Using list comprehension create a list of double value of
    even numbers in my_list also the number itself if it was
    odds in the same order. output :
    [[0, 1, 4, 3, 8], [5, 12, 7, 16, 9],
    [20, 11, 24, 13, 28]]

    """
    return [[j * 2 if j % 2 == 0 else j for j in i] for i in my_nest_list]

@memory_profiler.profile
def flaten_nested_list():
    """e. Using list comprehension flat the nested list my_nest_list

    """
    return [j for i in my_nest_list for j in i]

@memory_profiler.profile
def itertools_nested_list(): 
    """f. Using itertools /chain to flat the same list."""
    return itertools.chain.from_iterable(my_nest_list)

#d. Repeat a,b,c with tuples
@memory_profiler.profile
def nested_tuple():
    """d(a). Using generator Let’s create my_nest_tuple that
    has 3 numbers of list from 0-4 ,5-9 and 10-14.
    Expected output: ((0, 1, 2, 3, 4), (5, 6, 7, 8, 9), (10,
    11, 12, 13, 14)

    """
    for i in my_nest_tuple:
        yield i

@memory_profiler.profile
def double_nested_tuple():
    """d(b). Using tuple comprehension create a tuple of double value of
    even numbers in my_nest_tuple.
    Expected output: ((0, 4, 8), (12, 16), (20, 24, 28))

    """
    return tuple(tuple(j * 2 for j in i if j % 2 == 0) for i in my_nest_tuple)

@memory_profiler.profile
def double_value_nested_tuple():
    """d(c). double value for tuple comprehension.
    Expected output:
    ((0, 1, 4, 3, 8), (5, 12, 7, 16, 9),
    (20, 11, 24, 13, 28))

    """
    return tuple(tuple(j * 2 if j % 2 == 0 else j for j in i) for i in my_nest_tuple)

if __name__ == "__main__":
    print(list(nested_list()))
    print(double_nested_list())
    print(double_value_nested_list())
    print(tuple(nested_tuple()))
    print(double_nested_tuple())
    print(double_value_nested_tuple())
    print(flaten_nested_list())
    print(list(itertools_nested_list()))

