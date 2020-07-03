from collections import Counter

n = int(input())
room_numbers = list(map(int, input().split()))
m = Counter(room_numbers)
number_of_rooms = len(room_numbers)

for room,quantity in m.items():
    if m[room] == 1 :
        print(room)


