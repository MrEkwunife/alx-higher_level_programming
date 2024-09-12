#!/usr/bin/python3
if __name__ = '__main__':
    import hidden_4

    for item in dir(hidden_4):
        if not item.startswith('__'):
            print(item)
