keys = "qwertyuiopasdfghjklzxcvbnm"
key = input()
key = keys.index(key)
key += 1
if key == len(keys):
    key = 0
print(keys[key])