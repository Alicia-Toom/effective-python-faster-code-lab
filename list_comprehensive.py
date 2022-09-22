import memory_profiler
import timeit

@memory_profiler.profile
def list_comprehension_farenheit(values):
    return [(value - 32) * 0.5556 for value in values]

@memory_profiler.profile
def tuple_comprehension_farenheit(values):
    return tuple(((value - 32) * 0.5556 for value in values))

if __name__ == "__main__":
    farenheit_values = [0, 10, 20.1, 34,5]

    print(list_comprehension_farenheit(farenheit_values))
    print(tuple_comprehension_farenheit(farenheit_values))

    timer_list = timeit.Timer(lambda: list_comprehension_farenheit(farenheit_values))
    print(f"List timer: {timer_list.timeit(number=1)}")

    timer_tuple = timeit.Timer(lambda: tuple_comprehension_farenheit(farenheit_values))
    print(f"Tuple timer: {timer_tuple.timeit(number=1)}")
