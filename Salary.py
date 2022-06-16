line = input().split(" ")  # 21
line = [int(num) for num in line]
print(max(line) - min(line))
