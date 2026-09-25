"""3301: ใส่กล่อง"""
def main():
    """Working Place"""
    W, L, M, N = map(int, input().split())
    best = float('inf')
    for A in range(M, N + 1):
        waste = (W % A) * (L % A)
        if waste < best:
            best = waste
    print(best)

main()
