import math
chislo = int(input())

prime_factors = []
start = 2
end = int(math.sqrt(chislo)) + 1
i = start
while(i < end):
    if(chislo % i == 0):
        prime_factors.append(i)
        chislo /= i
        end = int(math.sqrt(chislo)) + 1
    else:
        i+=1
prime_factors.append(int(chislo))
print(prime_factors)