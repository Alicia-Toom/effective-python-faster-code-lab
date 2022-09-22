# Faster Code:

## 1. Tuples Vs Lists:

Create Tuple from 0-10 and list from 0-10 (not range) and time
both operation, which is faster and why?

Answer to this : see tuples_vs_list-py

Execution time for Tuple: 
Execution time for list: 

The reason for this is because tuples are stored in a single block of memory. As Tuples are immutable, it doesn't require extra space to store new objects.
Lists are allocated in two blocks: the fixed one with all the Python object information and a variable sized block for the data.

To support this claim: please see their size in tuples_vs_list-py

size of a list is :  136
size of a tuple is :  104

Beside the memory advantage, We can use tuples in a dictionary as a key but it's not possible with lists

However, tuple cant be sorted but in a list we can sort by calling "list.sort()" method.
Removing, adding, and replacing an element in tuple is not allowed while we can do in list. 


## TODO Add comment 2-6 