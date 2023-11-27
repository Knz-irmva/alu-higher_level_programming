#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0

    try:
        for i in range(x):
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                count += 1
        print()
        return count

    except (IndexError, TypeError):
        pass

# Example usage:
my_list = [1, 2, 'a', 3, 'b', 4, 5]
num_integers = safe_print_list_integers(my_list, 7)
print("Number of integers printed:", num_integers)
