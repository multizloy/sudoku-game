from itertools import islice

WIDTH, HEIGHT = 450, 450
N_CELLS = 9
CELL_SIZE = (WIDTH // N_CELLS, HEIGHT // N_CELLS)


def convert_list(lst, var_lst):
    """
    Converts a list into a list of lists, where the length of each sublist
    is determined by the values in var_lst.

    :param lst: The list to be converted
    :param var_lst: A list of ints, where the length of each sublist is the
        value at the corresponding index
    :return: A list of lists, where the length of each sublist is determined
        by the values in var_lst
    """
    it = iter(lst)
    return [list(islice(it, i)) for i in var_lst]
