def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def pollard_rho(n):
    def f(x):
        return (x**2 + 1) % n
    
    x = y = 2
    d = 1
    
    while d == 1:
        x = f(x)
        y = f(f(y))
        d = gcd(abs(x - y), n)
        
        if d == n:
            return None
    
    return d

def smallest_prime_factor(n):
    factor = pollard_rho(n)
    
    while factor is None:
        n += 1
        factor = pollard_rho(n)
    
    return factor

# Example usage
number = 1718944270642558716715
smallest_factor = smallest_prime_factor(number)
print("Smallest Prime Factor of", number, "is", smallest_factor)
