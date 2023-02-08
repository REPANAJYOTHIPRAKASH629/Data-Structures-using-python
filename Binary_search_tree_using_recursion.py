def bsearch(listt, idx0, idxn, val):
    if (idxn<idx0):
        return None
    else:
        midval = idx0 + ((idxn - idx0) // 2)
        if listt[midval] > val:
            return bsearch(listt, idx0, midval - 1, val)
        elif listt[midval] < val:
            return bsearch(listt, midval - 1, idx0, val)
        else:
            return midval
n=int(input("Enter the number of elements: "))
listt=[int(input()) for i in range(n)]
idx0 = int(input("enter idx0 : "))
idxn = int(input("enter idxn : "))
val = int(input("enter value :"))

print(bsearch(listt, idx0, idxn, val))


'''
output :-
Enter the number of elements: 6
8
11
24
56
88
131
enter idx0 : 0
enter idxn : 5
enter value :24
2
'''
            
























































            
