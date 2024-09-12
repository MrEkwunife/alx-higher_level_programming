#!/usr/bin/python3
if __name__ == '__main__':
    import sys

    count = len(sys.argv) - 1
    if not count:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print(f"{count} arguments:")

    for i, args in enumerate(sys.argv[1:]):
        print(f"{i + 1}: {args}")
