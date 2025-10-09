# import itertools

# def is_valid(positions):
#     for i in range(len(positions)):
#         for j in range(i + 1, len(positions)):
#             if abs(positions[i] - positions[j]) == j - i:
#                 return False
#     return True

# def count_n_queens_bf(N):
#     count = 0
#     for perm in itertools.permutations(range(N)):
#         if is_valid(perm):
#             count += 1
#     return count
#N = 4  # пример для N=8
#print(count_n_queens_bf(N))




def is_safe(queens, row, col):
    for r, c in enumerate(queens):
        if c == col or abs(r - row) == abs(c - col):
            return False
    return True

def backtrack(row, queens, N):
    if row == N:
        return 1
    count = 0
    for col in range(N):
        if is_safe(queens, row, col):
            count += backtrack(row + 1, queens + [col], N)
    return count

def count_n_queens_bt(N):
    return backtrack(0, [], N)

N = 4
print(count_n_queens_bt(N))


N = 4
print(count_n_queens_bit(N))