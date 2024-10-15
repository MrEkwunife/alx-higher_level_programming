#!/usr/bin/python3
"""Contains a function that that copies command line args and adds
them to a python list before passing them to json file"""
import sys

save_json = __import__('5-save_to_json_file').save_to_json_file
load_json = __import__('6-load_from_json_file').load_from_json_file
filename = "add_item.json"

try:
    items = load_json(filename)
except FileNotFoundError:
    items = []

items.extend(sys.argv[1:])
save_json(items, filename)
