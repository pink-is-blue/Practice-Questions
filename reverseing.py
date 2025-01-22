i = 1234 
#looping till i becomes 0 and getting the remainder of it and adding it to rev num
while(i > 0):
    rem = i%10
    revnum = revnum *10 + rem
    i = i//10
print(i)