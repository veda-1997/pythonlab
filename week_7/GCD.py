def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

print("GCD:", gcd(12, 18))
print("LCM:", lcm(12, 18))

# Output:
# GCD: 6
# LCM: 36
