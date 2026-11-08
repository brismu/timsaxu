import json, os, sys

files = os.listdir(sys.argv[1])
base = sys.argv[2]
if not base.endswith("/"): base += "/"

d = {f.rsplit(".", 1)[0]: [base + f] for f in files}
json.dump(d, sys.stdout)
