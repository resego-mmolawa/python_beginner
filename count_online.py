def online_count(status):
    count = 0
    for val in status.items():
        if 'online' in val:
            count += 1
    return count

statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
    }
obj3 = online_count(statuses)
print('The number of online is', obj3)