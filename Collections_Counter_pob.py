from collections import Counter

numShoes = int(input())
# Counter function is used since the shop owner has multiple shoes of same size
# and it should be tracked using the size:quantity dictionary
shoes = Counter(map(int, input().split()))
numCust = int(input())
income = 0

for i in range(numCust):
    size, price = map(int, input().split())
    if shoes[size]:# if the quantity of the shoe is not 0
        income += price # Add the amount to the income
        shoes[size] -= 1 # Decrement the quantity of the particular shoe
print(income)
