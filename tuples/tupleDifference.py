# Exibe os elementos da primeira tupla que não estão presentes na segunda.
A = (1, 2, 3, 4, 5)
B = (4, 5, 6, 7, 8)
C = ()
C = tuple(set(A) - set(B))

print(C)
