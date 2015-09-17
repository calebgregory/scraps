stock_prices_yesterday = {1: 500, 2: 1000, 3: 25, 4: 1025}

def best_profit(prices):
    buy, sell = 0, 0

    for p in prices:
        for q in prices:
            if not prices[buy] or not prices[sell]:
                prices[buy], prices[sell] = 0, 0
            elif prices[q] - prices[p] > prices[buy] - prices[sell]:
                buy = p
                sell = q

    return prices[sell] - prices[buy]

print best_profit(stock_prices_yesterday)
