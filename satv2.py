#!/usr/bin/env python3

"""satv2 - version 2 of the SAT tester.

This program quizzes people on SAT vocabulary.
"""
import json
import satjson
import pprint

def main():
    """The main function, runs everything"""
    vs = satjson.marshal_ugly_file()
    pprint.pprint(vs[:5])

if '__main__' == __name__:
    main()

def marshal_json_text(text):
    """Marshal json text into dict"""
    defs_dicts = json.loads(text)
    return defs_dicts

def read_ugly_file():
    """Read the defs-ugly.json file."""
    ugly_handle = open("defs-ugly.json", "r")
    ugly_text = ugly_handle.read()
    ugly_handle.close()
    return ugly_text

def marshal_ugly_file():
    """Read the defs-ugly.json file, marshal it into a bunch dicts."""
    return marshal_json_text(read_ugly_file())

# So, here's the function to make the word map.
def mk_word_map(vocabs):
    """Takes a bunch of `Vocab` objects, marshals them into the Python equivalent
    of `WordMap`."""
    wordmap = { v.word: v
                for v in vocabs }
    return wordmap

# We'll also want a function that makes a definition map
def mk_def_map(vocabs):
    """Takes a bunch of `Vocab` objects, marshals them into the Python equivalent
    of a `DefMap`."""
    defmap = { v.definition: v
               for v in vocabs }
    return defmap

