def gcd(n, m):
    if any(i < 1 for i in (n, m)): return None
    if n == m: return n
    else:
        n, m = max(n, m) - min(n, m), min(n, m)
        return gcd(n, m)
