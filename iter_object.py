"""
## 3. Iter Object :

a. Converting data types like string to iter object is very
useful. Read documentation about iter() and next() here
and then answer these questions:
b. Let’s say my_string = “I’m not iterator object” try
command next(my_string) what you get?
c. Create function that convert a string to iterator and print
each character in single line using next().
"""

def string_to_iterator(str):
    return str.__iter__()

if __name__ == "__main__":
    my_string = "I'm not iterator object"

    try:
        print(next(my_string))
    except Exception as e:
        print(e)
    
    str_iterator = string_to_iterator(my_string)
    while True:
        str_character = next(str_iterator, None)
        if str_character is None:
            break
        
        print(str_character)
