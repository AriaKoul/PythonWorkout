def my_chain(*args):
    for arg in args:
        for item in arg:
            yield item

for one_item in my_chain('abc', [1,2,3], {'a':1, 'b':2}):
    print(one_item)