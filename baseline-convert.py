import json, sys

with open(sys.argv[1]) as handle: gismu = handle.read().split("\n")
with open(sys.argv[2]) as handle: cmavo = handle.read().split("\n")
with open(sys.argv[3]) as handle: rafsi = handle.read().split("\n")

d = {
    "cmene": "baseline",
    "valsi": [],
}

for record in gismu[1:]:
    velcki = record[62:159].strip()
    extra = record[169:].strip()
    if extra: velcki += " " + extra
    d["valsi"].append({
        "klesi": "gismu",
        "valsi": record[1:6].strip(),
        "velcki": velcki,
        "xelfanva": [
            {"valsi": record[20:41].strip()},
            {"valsi": record[41:62].strip()},
        ],
    })

for record in cmavo[1:]:
    d["valsi"].append({
        "klesi": "cmavo",
        "selma'o": record[11:20].strip(),
        "valsi": record[1:11].strip(),
        "velcki": record[62:].strip(),
        "xelfanva": [{"valsi": record[20:62].strip()}],
    })

for record in rafsi[1:]:
    selbri = record[5:12].strip()
    gloss = record[12:].strip()
    d["valsi"].append({
        "klesi": "rafsi",
        "valsi": record[:5].strip(),
        "velcki": f"{gloss} (rafsi for {selbri})",
        "xelfanva": [{"valsi": selbri}, {"valsi": gloss}],
    })

with open(f"baseline.json", "w") as handle: json.dump(d, handle)
