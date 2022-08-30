#Buy and Sell Stocks Problem 1


prices = [7,1,5,3,8,4]
'''maxprofit,minstock = float('-inf'),prices[0]
for p in prices:
    maxprofit = max(maxprofit,p-minstock)
    minstock = min(p,minstock)
print(maxprofit)'''


#method 2 
max_diff = prices[1]-prices[0]
min_elem = prices[0]
for i in range(1,len(prices)):
    if(prices[i]-min_elem>max_diff):
        max_diff = prices[i]-min_elem
    if(prices[i]<min_elem):
        min_elem= prices[i]
print(max_diff)


