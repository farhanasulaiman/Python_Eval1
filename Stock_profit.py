stock = [44, 30, 24, 32, 35, 30, 40, 38, 15]
profit = []
max = 0
for i in stock:
    for j in stock:
        if i < j and stock.index(j) > stock.index(i):
            max = j - i
            profit.append(max)
print(stock)
print(profit)
profit.sort()
print("max profit : ", profit[-1])
