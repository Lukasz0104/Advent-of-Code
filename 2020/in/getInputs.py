import urllib.request as req
from pathlib import Path


cookie = ""
for i in range(1,26):
    print(i)
    rq = req.Request(f"https://adventofcode.com/2020/day/{i}/input")
    rq.add_header("cookie",cookie)
    res = req.urlopen(rq)
    p = Path(__file__).parent
    with open(f"{p}\\{0 if i<10 else ''}{i}.txt",'w') as f:
        f.write(res.read().decode('utf-8'))
    print(f"day {i} done")

