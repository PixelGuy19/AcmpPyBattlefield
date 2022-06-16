n = int(input())

friends = []
for i in range(0, n):
    friends.append(input())

n = int(input())
inFriends = []
for i in range(0, n):
    inFriends.append(input())

mutual = []
also = []
for i in inFriends:
    if friends.__contains__(i):
        mutual.append(i)
    else:
        also.append(i)

friends.sort()
print("Friends: " + str.join(", ", friends))

mutual.sort()
print("Mutual Friends: " + str.join(", ", mutual))

also.sort()
print("Also Friend of: " + str.join(", ", also))