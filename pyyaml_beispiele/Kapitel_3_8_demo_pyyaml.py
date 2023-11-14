from yaml import load, dump, load_all
from pprint import pprint
import os

fname = "network_devices.yml"
outfname, sfname = "output.yml", "schema.yml"
d1 = {"a": 2, "b": [3,4,5], "c": {"s1": "v1"}}

def get_items_type(struct):
    if isinstance(struct, dict):
        for key, value in struct.items():
            yield "Key", key, type(key)
            yield from get_items_type(value)
    elif isinstance(struct, (list, tuple)):
        for item in struct:
            yield from get_items_type(item)
    else:
        yield "Val/item", struct, type(struct)

with open(fname, "r") as fid:
    contents = load(fid)
print(contents, type(contents))

pprint(list(get_items_type(contents)))

print(dump(d1))
with open(outfname, "w") as fid:
    dump(d1, stream=fid)

cmd = f"pykwalify -d {fname} -s {sfname}"
print("kontrolle:")
os.system(cmd)
