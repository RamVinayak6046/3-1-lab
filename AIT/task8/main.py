def solve_n_queens(n=4):
    solutions = []
    cols = set()
    diag1 = set()
    diag2 = set()
    board = [-1] * n

    def backtrack(r=0):
        if r == n:
            solutions.append(board.copy())
            return
        for c in range(n):
            if c in cols or (r + c) in diag1 or (r - c) in diag2:
                continue
            cols.add(c)
            diag1.add(r + c)
            diag2.add(r - c)
            board[r] = c
            backtrack(r + 1)
            cols.remove(c)
            diag1.remove(r + c)
            diag2.remove(r - c)
            board[r] = -1

    backtrack()
    return solutions

def format_solutions(sol):
    n = len(sol[0])
    results = []
    for s in sol:
        rows = []
        for r in range(n):
            row = ['.'] * n
            row[s[r]] = 'Q'
            rows.append(''.join(row))
        results.append('\n'.join(rows))
    return '\n\n'.join(results)

if __name__ == "__main__":
    sols = solve_n_queens(4)
    for i, s in enumerate(sols, 1):
        print(f"Solution #{i}:")
        print(format_solutions([s]))
        print()
