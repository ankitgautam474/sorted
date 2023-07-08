def get_last_element(tuple):
    return tuple[-1]

def sort_tuples(lst):
    sorted_list = sorted(lst, key=get_last_element)
    return sorted_list

# Test the function with the sample list
sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
sorted_list = sort_tuples(sample_list)
print(sorted_list)
