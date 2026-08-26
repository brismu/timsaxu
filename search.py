import glob, json, sys

q = sys.argv[1]
full = q == "--full"
if full: q = sys.argv[2]

dicts = [json.load(open(f, "r")) for f in glob.iglob("dicts/*.json")]

def printRecord(v, cmene):
    if "selma'o" in v: kls = f"({v["klesi"]}, {v["selma'o"]})"
    else: kls = f"({v["klesi"]})"
    print("-", v["valsi"], kls, v["velcki"], f"({cmene})")

def search(label, test):
    first = True
    for d in dicts:
        cmene = d.get("cmene", None)
        for v in d["valsi"]:
            if test(q, v):
                if first:
                    print(f"{label}:")
                    first = False
                printRecord(v, cmene)

search("Exact matches", lambda q, v: q == v["valsi"])
search("Inexact matches", lambda q, v: q in v["valsi"] and q != v["valsi"])
search("Gloss matches", lambda q, v: any(q in x["valsi"] for x in v["xelfanva"]))
if full:
    search("Full-text definition matches", lambda q, v: q in v["velcki"])
