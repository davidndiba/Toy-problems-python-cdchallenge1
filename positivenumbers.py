def positivity (a, b, c):
    positive_count = 0

    if a > 0:
        positive_count += 1
    if b > 0:
        positive_count += 1
    if c > 0:
        positive_count += 1

    return positive_count == 2


print(positivity(2, 4, -3))  
print(positivity(-4, 6, 8))  
print(positivity(4, -6, 9))  
print(positivity(-4, 6, 0))  
print(positivity(4, 6, 10))  
print(positivity(-14, -3, -4))  
