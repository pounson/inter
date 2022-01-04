nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    [1, 2, None],
]

def flat_generator(a: list) -> list:
    return [x for sublist in a for x in sublist]

for item in  flat_generator(nested_list):
    print(item)


nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    [1, 2, None],
    [45.5,'e']
]
for i in nested_list[:]:
    for x in i: nested_list.append(x)
    nested_list.remove(i)
print(nested_list)