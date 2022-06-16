import re

line = input()
if len(re.findall(r'^[a-z]', line)) == 0 or line.__contains__("__") or line.endswith("_"):
    print("Error!")
    exit()

if line.__contains__("_"):
    if len(re.findall(r'[A-Z]', line)) > 0:
        print("Error!")
        exit()

    words = re.findall(r'[a-z]+', line)
    for i in range(1, len(words)):
        s = list(words[i])
        s[0] = s[0].upper()
        words[i] = "".join(s)
    print(''.join(words))
elif len(re.findall(r'[A-Z]', line)) > 0:
    for i in re.findall(r'[A-Z]', line):
        line = line.replace(i, f"_{i.lower()}")
    print(line)
else:
    print(line)