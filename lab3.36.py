"""3.36 Построить список списков по схеме:
1-й элемент:	0	0	0	1	0	0	0
2-й элемент:	0	0	1	1	1	0	0
3-й элемент:	0	1	1	1	1	1	0
4-й элемент:	1	1	1	1	1	1	1
5-й элемент:	0	1	1	1	1	1	0
6-й элемент:	0	0	1	1	1	0	0
7-й элемент:	0	0	0	1	0	0	0
"""

list_size = 7
pivot = list_size // 2

matrix = [[0 for i in range(list_size)] for j in range(list_size)]

for i in range(0, pivot+1):

    for j in range(pivot - i, pivot + i + 1):
        matrix[i][j] = 1
    for j in range(pivot - i, pivot + 1 + i):
        matrix[list_size - i - 1][j] = 1

print(*matrix, sep='\n')