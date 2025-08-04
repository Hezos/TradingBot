# X is the variable, which is worth buying on
def DollarCostAveraging(low, high, buy1, buy2):
    X = 0
    X = low * high * ( buy2 + buy1 ) / ( high * buy2 + buy1 * low )
    return X

#This function expects a very long price fall
def DollarCostAveragingRepeat(low:[], high, buy1, buy2):
    X = 0
    High = high
    for i in range(0, len(low) - 1):
        High = DollarCostAveraging(low[i], High,buy1, buy2)
        X = DollarCostAveraging(low[i+1], High,buy1, buy2)
    return X 

print(DollarCostAveraging(1.1, DollarCostAveraging(1.09, 1.36, 50000, 100000),50000,100000) )
print(DollarCostAveragingRepeat([0.7,0.6,0.5,0.4,0.3],1.36, 50000, 100000))


