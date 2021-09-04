def powerSum(x):
    if x==0 or x==1:
        return x
    else: 
        somaPotencias = powerSum(x) + powerSum(x-1)
        x = x - 1
        return somaDePotencias;

powerSum(2)