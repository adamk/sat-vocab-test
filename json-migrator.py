def_handle = open("definitions.txt", "r")
def_text = def_handle.read()
def_handle.close()

def_lines = def_text.splitlines()
def_words = [line.split() for line in def_lines]

def_groups = [(g[0], g[1][:-1], " ".join(g[2:])) for g in def_words]

keys = ("word", "pos", "def")
def_dicts = [dict(zip(keys, vals)) for vals in def_groups]

import json
pretty_encoder = json.JSONEncoder(indent=2)
ugly_encoder = json.JSONEncoder(separators=(",", ":"))

pretty_encoded = pretty_encoder.encode(def_dicts)
ugly_encoded = ugly_encoder.encode(def_dicts)

pretty_handle = open("defs-pretty.json", "w")
pretty_handle.write(pretty_encoded)
pretty_handle.close()

ugly_handle = open("defs-ugly.json", "w")
ugly_handle.write(ugly_encoded)
ugly_handle.close()
