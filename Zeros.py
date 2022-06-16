import re
zeros = re.findall(r"[0]*", input())
zeros = [len(num) for num in zeros]
print(max(zeros))