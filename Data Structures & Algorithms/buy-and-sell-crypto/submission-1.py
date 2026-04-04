class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l = 0
        r =  1
        max_gain = 0

        for i in range(len(prices)-1):
            gain = prices[r] - prices[l]
            if prices[l] > prices[r]:
                l = r
            elif gain > max_gain:
                max_gain = gain
            
            r+=1
            
        return max_gain