import memory_profiler
import timeit 

@memory_profiler.profile
def power2(n):
    """a. Create a function power2(n) that return list of power
2(like 3**2) of list from 0-(n-1)?
"""
    square_list = []
    for i in range(1,n+1):
        square_list.append(2 ** i)
    return square_list

@memory_profiler.profile
def power2_generator(n):
    """b. Then create a function power2_generator(n) that do the
same thing as power2(n) but as generator! Hint here
"""
    for i in range(1,n+1):
        yield i ** 2

if __name__ == "__main__": 
    """c. Write needed code to print the list elements in both
cases!
"""
    print(power2(4))
    print(power2_generator(4))


"""d. Check timeit and memory profile for both functions
power2(n) and power2_generator(n) for n=10000
"""
n = 10000

timer_power2 = timeit.Timer(lambda: power2(n))
print(f"Power2 timer: {timer_power2.timeit(number=1)}")

timer_power2_generator = timeit.Timer(lambda: power2_generator(n))
print(f"Power2 Generator timer: {timer_power2_generator.timeit(number=1)}")
