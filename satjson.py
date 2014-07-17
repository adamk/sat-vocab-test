"""JSON interface for satv2"""

import json

def marshal_json_text(text):
    """Marshal json text into a dict"""
    return json.loads(text)

def read_ugly_file():
    """Read the defs-ugly.json file."""
    ugly_handle = open("defs-ugly.json", "r")
    ugly_text = ugly_handle.read()
    ugly_handle.close()
    return ugly_text

def marshal_ugly_file():
    """Read the defs-ugly.json file, marshal it into a bunch of dicts."""
    return marshal_json_text(read_ugly_file())
