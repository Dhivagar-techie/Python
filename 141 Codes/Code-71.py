from collections import OrderedDict

od = OrderedDict()

od['b'] = 2
od['c'] = 3

print("Before insertion:")
print(od)

od.update({'a': 1})

od.move_to_end('a', last=False)

print("After insertion at beginning:")
print(od)