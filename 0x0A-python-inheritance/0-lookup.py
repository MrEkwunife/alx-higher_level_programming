#!/usr/bin/python3

""" function that returns the list of available attributes
and methods of an object
"""


def lookup(obj):
    """this returns the list of all attributes and methods
    of the object.
        Args:
            obj.
    """
    return dir(obj)


if __name__ == "__main__":
    """this is for testing"""
    class MyClass1(object):
        pass

    class MyClass2(object):
        my_attr1 = 3

        def my_meth(self):
            pass

    print(lookup(MyClass1))
    print(lookup(MyClass2))
    print(lookup(int))
