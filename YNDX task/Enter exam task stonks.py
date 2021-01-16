fin = open("new.txt", "r")

def checkCurrentStrategy(gap, costPerDay, costs, N):
    #рассмотрим на примере покупки-продажи одной акции
    days = len(costPerDay)
    day = 2
    portfolio = 0
    transactions = 0
    while day + gap + 1 <= days:
        if (costPerDay[day] >= costPerDay[day-1]) and (costPerDay[day-1] <= costPerDay[day-2]):
            portfolio -= costs[day * N + 100]
            portfolio += costs[(day + gap) * N + 300]
            day += gap
            transactions += 1
        else:
            day += 1
    return portfolio, transactions

def strategyAdvice(finances, transactions, cost, profit):
    finalProfit = (finances // cost) * transactions * profit
    return finalProfit

def strategy(gap):
    print("\nWinning strategy: You should look at the average values ​​of the stock price for the day, and if this value is just beginning to rise, then at the beginning of the day you should buy as many shares as possible and sell them after", gap, "days in evening")

N = 359 #примерное количество строк данных за один день

dates, costs = [], []
for line in fin:
    data = [s for s in line.split(',')]
    dates.append(data[1])
    costs.append(float(data[3]))

count, summPerDay = 0, 0
costPerDay = []
for cost in costs:
    if count <= N:
        summPerDay += cost
        count += 1
    else:
        costPerDay.append(float("%0.2f" % (summPerDay / N)))
        summPerDay = 0
        count = 0

#Стратегия предполагает, что возрастания и убывания средних цен за день не сменяются
#часто, поэтому мы можем рассчитывать на возрастание в среднем несколько дней подряд
print("Find optimal gap for satrategy:\n")
maxResult = 0
for gap in range(1, 10):
    result, transactions = checkCurrentStrategy(gap, costPerDay, costs, N)
    totalProfit = (((costPerDay[1] + result) / costPerDay[1]) - 1) * 100
    if maxResult <= result:
        maxResult = result
        maxResultGap = gap
        maxTotalProfit = totalProfit
        maxResultTransaction = transactions
    print("If gap =", gap, "then you can earn", "%0.2f" % (totalProfit), "%, and made", transactions, "transactions")
print("\nI think, that optimal gap is:", maxResultGap)
results = [int(res) for res in input("\nEnter your finances and quantity of transactions: ").split()]

finances, transactionsQuantity = results[0], results[1]
currentCost = costs[len(costs) - 1]
profit = maxTotalProfit / maxResultTransaction
answer = strategyAdvice(finances, transactionsQuantity, currentCost, profit)

strategy(maxResultGap)
print("You earn about", "%0.2f" % (answer))

fin.close()
    

