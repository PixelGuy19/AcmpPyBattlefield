import re

try:
    line = input()
    c = re.findall(r'^\-?\d*[+\-*\/]\-?\d*=\-?\d*$' , line)
    if c is None or len(c) == 0:
        raise Exception()
    if line.__contains__(" "):
        raise Exception()

    for t in re.findall(r'\d*', line):
        if not t.startswith("0"):
            continue
        for c in re.findall(r'[0]\d*' , t):
            if c.replace("0","") == "":
                continue
            line = line.replace(c , c.lstrip("0"))

    if line.__contains__("/0"):
        print("NO")
        exit()
    line = line.split("=")
    l = eval(line[0])
    r = eval(line[1])
    if l == r:
        print("YES")
    else:
        print("NO")
except Exception as e:
    print("ERROR")
