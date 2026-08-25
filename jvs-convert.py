from collections import defaultdict
import json, sys
from xml.etree import ElementTree as et

doc = et.parse(sys.argv[1])

def gloss(tag):
    rv = {"valsi": tag.get("word")}
    if "sense" in tag.keys(): rv["notci"] = tag.get("sense")
    return rv

dicts = defaultdict(list)
realnames = {}
for tag in doc.findall(".//valsi"):
    try:
        u = tag.find(".//user/username").text
        rn = tag.find(".//user/realname")
        if rn is not None and u not in realnames: realnames[u] = rn.text
        d = {
            "klesi": tag.get("type"),
            "valsi": tag.get("word"),
            "velcki": tag.find(".//definition").text,
            "xelfanva": list(map(gloss, tag.findall(".//glossword"))),
        }
        selmaho = tag.find(".//selmaho")
        if selmaho is not None: d["selma'o"] = selmaho.text
        dicts[u].append(d)
    except Exception as e:
        print("Bummer:", e)
        print("Tag:", tag, tag.attrib)
        raise

for u, l in dicts.items():
    d = {"valsi": l}
    if u in realnames: d["cmene"] = realnames[u]
    with open(f"jvs/{u}.json", "w") as handle: json.dump(d, handle)
