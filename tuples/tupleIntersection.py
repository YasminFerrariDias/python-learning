# Encontra e exibe os elementos em comum entre duas tuplas.
A = (1, 2, 3, 4, 5)
B = (4, 5, 6, 7, 8)
C = ()
C = tuple(set(A) & set(B))

print(C)
