def fizz_buzz(n): 
    answer = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            answer.append("FizzBuzz") #both 3 and 4 if that its fizzbuzz
        elif i % 3 == 0:
            answer.append("Fizz")
        elif i % 5 == 0:
            answer.append("Buzz")
        else:
            answer.append(str(i))
    return answer
print(fizz_buzz(3))  
print(fizz_buzz(5))  
print(fizz_buzz(15)) 
