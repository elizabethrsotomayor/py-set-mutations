# Enter your code here. Read input from STDIN. Print output to STDOUT
num = int(input())
i = input().split()
A = set([int(k) for k in i])
n = int(input())

for x in range(0, n):
    operation = input().split()
    p = input().split()
    B = set([int(o) for o in p])

    if (operation[0] == "intersection_update"):
        A.intersection_update(B)
    elif (operation[0] == "update"):
        A.update(B)
    elif (operation[0] == "symmetric_difference_update"):
        A.symmetric_difference_update(B)
    elif (operation[0] == "difference_update"):
        A.difference_update(B)

print(sum(A))
