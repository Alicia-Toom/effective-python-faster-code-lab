# TODO

def nested_list():
    """a. Using generator Let’s create my_nest_list that
    has 3 numbers of list from 0-4 ,5-9 and 10-14. output:
    [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10,
    11, 12, 13, 14]]

    """
    my_nest_list = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10,
                    11, 12, 13, 14]]

    my_nest_list_gen = iter(my_nest_list)
    for i in my_nest_list_gen:
        yield i

if __name__ == "__main__":
    print(next(nested_list()))

    try:
        print(next(nested_list))
    except Exception as e:
        print(e)

    list_iterator = nested_list()
    while True:
        list_character = next(list_iterator, None)
        if list_character is None:
            break

        print(list_character)
