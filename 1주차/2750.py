A = int(input())
A_list = []

for i in range(A):
    num = int(input())
    A_list.append(num)

for i in range(A):
    min_index = i
    for j in range(i+1, A):
        if A_list[j] < A_list[min_index]:
            min_index = j
    A_list[i], A_list[min_index] = A_list[min_index], A_list[i]

for i in A_list:
    print(i)
