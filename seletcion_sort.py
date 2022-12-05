def swap(A,i,j):
    s = len(A)
    if (i in range(s) and (j in range(s))):
        t = A[i]
        A[i] = A[j]
        A[j] = t
    else:
        raise NameError('Array index out of bound')
def selectionsort(A):
    def fiom(A,i,n):
        m = i
        k = i
        while k < n:
            if A[k] < A[m]:
                m=k
            k+=1
        return m
    n = len(A)
    p = q =0
    while p < n:
        q = fiom(A,p,n)
        swap(A,q,p)
        p+=1
A = eval(input('Enter your list : '))
print(A)
selectionsort(A)
print(A)
