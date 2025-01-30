def single_number(nums):
    count = {} #if more than one count becomes only more than one if there is a nuique value count remains one, return value where count = 1
    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    for num in count:
        if count[num] == 1:
            return num
print(single_number([2, 2, 1]))     
print(single_number([4, 1, 2, 1, 2])) 
