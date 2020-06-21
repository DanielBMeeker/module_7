import array as arr


def sort_array(a_array):
    pass


def search_array(a_array, value):
    a_array = arr.array('i', a_array)  # explicitly convert to array in case it comes in as a list
    if value not in a_array:
        return -1
    else:
        return a_array.index(value)
    pass
