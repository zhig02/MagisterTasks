

"""
Дан массив целых чисел А[0..n-1]. Известно, 
что на интервале [0, m] значения массива строго возрастают, 
а на интервале [m, n-1] строго убывают. Найти m за O( log m ).
2 ≤ n ≤ 10000.


Пример
Ввод	                            Вывод
10
1 2 3 4 5 6 7 6 5 4                 6

"""

# n = int(input())
# A = list(map(int, input().split()))
n = 10
A = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4]

def find_m(A : list, n : int) -> int:
    start = 0
    end = n
    while start < end:
        m = (end + start) // 2
        if A[m-1] < A[m] and A[m] > A[m+1]:
            return m
        elif (A[m-1] < A[m]):
            start = m
        elif A[m-1] > A[m]:
            end = m
    return m


print(find_m(A, n))