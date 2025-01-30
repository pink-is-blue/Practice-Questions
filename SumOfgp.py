def sum_of_gp(a, r, n):
    return a * (1 - r**n) / (1 - r) #sum of nth term formula
a = 3  # First term
r = 2  # Common ratio
n = 5  # Number of terms
gp_sum = sum_of_gp(a, r, n)
print(gp_sum)

