def power(base, exp):
    if exp == 0:
        return 1
    if exp < 0:
        return 1 / power(base, -exp)
    return base * power(base, exp - 1)

print(power(2, 5))
print(power(2, 0))
print(power(2, -3))

# Output:
# 32
# 1
# 0.125
