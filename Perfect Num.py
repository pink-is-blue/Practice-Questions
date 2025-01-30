def is_perfect_number(n):
    if n <= 1:
        return False
    sum_of_divisors = 0
    for i in range(1, n):
        if n % i == 0:
            sum_of_divisors += i
    return sum_of_divisors == n

print(is_perfect_number(28)) 
print(is_perfect_number(12))  
