import memory_profiler
import itertools
import timeit

@memory_profiler.profile
def string_perm_list(my_string):
    return list(itertools.permutations(my_string))

@memory_profiler.profile
def string_perm_tuple(my_string):
    return tuple(itertools.permutations(my_string))


if __name__ == "__main__":
    print(string_perm_list("ABCD"))
    
    input_test_string = "01234567"
    # input_test_string = "01234567890" # too slow
    
    timer_list = timeit.Timer(lambda: string_perm_list(input_test_string))
    print(f"List timer: {timer_list.timeit(number=1)}")

    timer_tuple = timeit.Timer(lambda: string_perm_tuple(input_test_string))
    print(f"Tuple timer: {timer_list.timeit(number=1)}")
