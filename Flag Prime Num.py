n = int(input("Enter a number: "))
flag = True #using flag to check prime or not
for i in range(n - 1, 1, -1):
    if n % i == 0: #is any iterated number is divisible flag false
        flag = False
        break
if flag:
    print("The number is prime")
else:
     print("The number isn't prime")
