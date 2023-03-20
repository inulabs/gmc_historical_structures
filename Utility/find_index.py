
def find_index(key, my_list, value):
    for i in range(len(my_list)):
        if my_list[i].as_dict()[key] == value:
            return i
    return -1
