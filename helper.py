import json
import car
import helper
import sys
import functools


def load_json(filename):
    json_file = filename
    with open(json_file, 'r') as file:
        car_config = json.load(file)
    return car_config


def func_3(lst, index):
    return lst[index]+1


def func_2(lst, index):
    try:

        print(func_3(lst, index), end=" ")
    except IndexError:
        print("Error A", end=" ")

    except TypeError:

        print("error B", end=" ")


def func_1():

    lst = [0, 1, "2", 3]
    for i in range(len(lst)+1):
        func_2(lst, i)


def get_even_func():
    def inner(a):
        return a % 2 == 0
    return inner


def my_pow(x):
    def pow(y):
        if y == 0:
            return 1
        return x*pow(y-1)
    return pow


def dont_run_twice(f):
    cache = {}

    def isit(*args):
        if args in cache:
            if cache[args] == 0:
                cache[args] = 1
                return f(*args)
            return None
        cache[args] = 1
        if len(cache) > 1:
            for element in cache:
                if element != args:
                    cache[element] = 0
        return f(*args)
    return isit


def equal_trees(x, y):
    if x == y:
        return (x.left == y.left or x.left == y.right) and (y.left == x.left or y.left == x.right)\
            and (equal_trees(x.left, y.left) or equal_trees(x.left, y.right)) and (equal_trees(y.left, x.left) or equal_trees(y.left, x.right))

    return False
