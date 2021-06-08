def doubleStuff(a_list):
    new_list = []
    for value in a_list:
        new_elem = 2 * value
        new_list.append(new_elem)
    return new_list


things = [2, 5, 9]
print(things)
things = doubleStuff(things)
print(things)
