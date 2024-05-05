#n = int(input())
n = 24
import math
def is_prime(num):

    i = start = 2
    end = int(math.sqrt(num)) + 1
    prime = []

    while i < end:
        if num % i == 0:
            if i not in prime:
                prime.append(i)
            num = int(num/ i)
            end =  int(math.sqrt(num)) + 1
        else:
            i += 1
    if num not in prime:
        prime.append(num)

    return prime

strong_prime = []
for i in range(2, n):
    if(len(is_prime(i)) >= 3):
        strong_prime.append(i)
print(strong_prime)
