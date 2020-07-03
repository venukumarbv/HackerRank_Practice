nA = int(input())
sA = set(map(int, input().split()))
other_sets = int(input())

for i in range(0,2 * other_sets,2): # Jump 2 iterations at a time
    com, num_digits = input().split()
    setX = set(map(int, input().split()))
    if com == 'intersection_update':
        sA.intersection_update(setX)
    elif com == 'update':
        sA.update(setX)
    elif com == 'symmetric_difference_update':
        sA.symmetric_difference_update(setX)
    elif com == 'difference_update':
        sA.difference_update(setX)

print(sum(sA))
