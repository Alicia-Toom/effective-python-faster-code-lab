import timeit

def list_function():
    list = []
    for i in range(1, 11):
        list.append(i)

def tuple_function():
    tuple = ()
    for i in range(1, 11):
        tuple = tuple + (i,)

timer_list = timeit.Timer(lambda: list_function)
print(f"List timer: {timer_list.timeit(number=1)}")

timer_tuple = timeit.Timer(lambda: tuple_function)
print(f"Tuple timer: {timer_tuple.timeit(number=1)}")

