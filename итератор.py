nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]


class FlatIterator:
    def __init__(self, items_list):
        self.items_list = items_list

    def __iter__(self):
        self.main_list_cursor = 0
        self.nested_list_cursor = 0-1
        return self


    def __next__(self):
        self.nested_list_cursor += 1

        if self.nested_list_cursor == len(self.items_list[self.main_list_cursor]):
            self.main_list_cursor += 1
            self.nested_list_cursor = 0
        if self.main_list_cursor == len(self.items_list):
            raise StopIteration


        return self.items_list[self.main_list_cursor][self.nested_list_cursor]

for item in FlatIterator(nested_list):
    print(item)
