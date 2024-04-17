class Solution(object):
    def maxProfit(self, prices):
        max_profit = 0
        buy_index = 0

        for sell_index in range(len(prices)):
            sell_price = prices[sell_index]
            buy_price = prices[buy_index]
            profit = sell_price - buy_price
            if ( profit > max_profit):
                max_profit = profit
            if ( profit < 0):
                buy_index = sell_index
        return max_profit
        