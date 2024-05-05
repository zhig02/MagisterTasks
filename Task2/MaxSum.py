n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

i0 = j0 = 0
max_sum = A[0] + B[0]
max_i = A[0]
max_i_index = 0

for i in range(1, n):
    if max_i + B[i] > max_sum:
        max_sum = max_i + B[i]
        i0 = max_i_index
        j0 = i
    if A[i] > max_i:
        max_i = A[i]
        #i0 = i
        max_i_index = i

print(i0, j0)