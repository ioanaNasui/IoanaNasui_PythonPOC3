def sets_operations(first_set, second_set):
    print(f'------------> Union')
    union_set = first_set.union(second_set)
    print(f'Union on two sets: {union_set}')
    print(f'------------> Intersection')
    intersection_set = first_set.intersection(second_set)
    print(f'Intersection on two sets: {intersection_set}')
    print(f'------------> Difference')
    difference_set = first_set.difference(second_set)
    print(f'Difference on two sets: {difference_set}')
    print(f'------------> Symmetric Difference')
    symmetric_difference_set = first_set.symmetric_difference(second_set)
    print(f'Symmetric Difference on two sets: {symmetric_difference_set}')


if __name__ == '__main__':
    # Create two sets with 10 numbers each (some of the numbers should be present in both sets).
    # With these two sets, exemplify the following basic sets operations:
    # union, intersection, difference and symmetric difference.
    set_one = {19, 10, 2, 20, 15, 8, 7, 17, 14, 13}
    set_two = {6, 1, 7, 9, 5, 20, 12, 18, 8, 19}
    print(f'First set is: {set_one}')
    print(f'Second set is: {set_two}')
    sets_operations(set_one, set_two)
