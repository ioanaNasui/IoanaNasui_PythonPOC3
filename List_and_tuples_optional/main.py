def remove_an_element_from_tuple(tuple_to_change):
    # Write a python code to remove an element from a tuple.
    some_list = list(tuple_to_change)  # = [element for element in tuple_to_change]
    some_list.pop()
    tuple_changed = tuple(some_list)  # nu merge cu (element for element in some_list)!!!
    return tuple_changed


def replace_last_element(a_list):
    # Replace the last element in the list with the string 'last'
    # using list comprehension and tuples
    # b_list = ['last' if element[len(a_list) - 1] else element for element in a_list]
    # list_last_element = []
    # for element in a_list:
    #    if element[len(a_list) - 1] != 'last':

    # return b_list
    pass


def extract_only_strings(s_list):
    # Extract only the strings from the following list using list comprehension :
    # s_list = ['I', 'am', 1, 'list', 'of', 5, 'strings']
    only_strings = [element for element in s_list if isinstance(element, str)]
    return only_strings


def three_by_three_matrix(matrix_size):
    # Generate a 3 by 3 matrix that contains 'X' on the main diagonal and '_' in the rest.
    matrix = []
    for i in range(matrix_size):
        row = []
        for j in range(matrix_size):
            if i == j:
                row.append('X')  # nu trebuie sa fie row=row.append() deoarece returneaza "None"
            else:
                row.append('_')
        matrix.append(row)
    return matrix


if __name__ == '__main__':
    tuple_example = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
    print(f'Initial tuple: {tuple_example}')
    print(f'Tuple with last element removed: {remove_an_element_from_tuple(tuple_example)}')
    simple_list = ['I', 'am', 1, 'list', 'of', 5, 'strings']
    print(replace_last_element(simple_list))
    simple_list = ['I', 'am', 1, 'list', 'of', 5, 'strings']
    print(f'Initial list: {simple_list}')
    print(f'List containing only strings: {extract_only_strings(simple_list)}')
    print(three_by_three_matrix(3))
