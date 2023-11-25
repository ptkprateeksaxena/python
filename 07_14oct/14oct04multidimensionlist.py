A = [45, 8, 5, 4, 5, 4, 45, 5, 5, ]                       # single list
B = [[45, 25, 78], [12, 45, 78], [2, 4], [5]]        # multi-list

print(len(B[0]))
print(B)

#commonly

for row in B:
    print(row)

# in matrix format

for i in range(len(B)):
    for j in range(len(B[i])):
        print(B[i][j], end=" ")
    print()