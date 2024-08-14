from functools import reduce

def find_max_float(numbers):
    return reduce(lambda x,y: x if x>y else y, numbers)

print(find_max_float([3.5, 2.7, 8.9, 4.6]))
print(find_max_float([3.5]))