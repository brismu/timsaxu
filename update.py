import json, os.path, shutil, subprocess

with open("en.json", "r") as handle: d = json.load(handle)

for name, urls in d.items():
    old = f"dicts/{name}.json"
    new = f"dicts/{name}.json.new"
    args = ["curl", "-R", "-o", new]
    if os.path.exists(old): args.extend(["-z", old])
    for url in urls:
        print(f"[{name}] Trying", url)
        try: subprocess.run(args + [url], check=True)
        except subprocess.CalledProcessError: continue
        shutil.move(new, old)
        break
