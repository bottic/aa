nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    [1, 2, None],
]


def flat_generator(list):
    for items in list:
        for item in items:
            yield item




for item in flat_generator(nested_list):
    print(item)
