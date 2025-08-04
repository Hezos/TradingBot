# X is the variable, which is worth buying on
def DollarCostAveraging(low, high, buy1, buy2):
    X = 0
    X = low * high * ( buy2 + buy1 ) / ( high * buy2 + buy1 * low )
    return X

print(DollarCostAveraging(1.1, DollarCostAveraging(1.09, 1.36, 50000, 100000),50000,100000) )