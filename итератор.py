nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]


class FlatIterator:
    def __init__(self, items_list):
        self.items_list = items_list

    def __iter__(self):
        return self

    def __next__(self):
        for items in self.items_list:
            for item in items:
                return item


for item in FlatIterator(nested_list):
    print(item)
