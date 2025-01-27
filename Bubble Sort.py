def bubbleSort(nlist): # so here we use nested for loop, the first for is for the first number and the other one is for the rest of the numbers
    for i in range(len(nlist)-1,0,-1): # it compares values right of it and then swaps if its larger
        for j in range(i):
            if nlist[j]>nlist[j+1]:
                temp = nlist[j]
                nlist[j] = nlist[j+1]
                nlist[j+1] = temp

nlist = [14,46,43,27,57,41,45,21,70]
bubbleSort(nlist)
print(nlist)