def mergesort(array):
    if len(array)>1:
        middle = len(array)//2
        left = array[:middle]
        right = array[middle:]
        mergesort(left)
        mergesort(right)
        i = j = k = 0
        while i<len(left) and j<len(right):
            if left[i] < right[j]:
                array[k]=left[i]
                i+=1
            else:
                array[k] = right[j]
                j+=1
            k+=1
        while i<len(left):
            array[k] = left[i]
            i+=1
            k+=1
        while j<len(right):
            array[k] = right[j]
            j+=1
            k+=1
def printlist(array):
    for i in range(len(array)):
        print(array[i],end=' ')
    print()
if __name__=="__main__":
    array = eval(input('Enter your list : '))
    print('Given list is : ')
    print(array)
    mergesort(array)
    print('Sorted list is : ')
    print(array)
