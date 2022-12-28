ar = [0 for _ in range(10)]
n = 10
front = - 1
rear = - 1
def enqueue(item):
    global n
    global rear
    global front
    if rear == n - 1:
        print("Overflow!", end = '')
        print()
        return
    else:
        if front == - 1 and rear == -1:
            front = 0
            rear = 0
        else:
            rear += 1
        ar[rear] = item
        print("Element inserted")
def dequeue():
    global n
    global rear
    global front
    if front == - 1 or front > rear:
        print("Underflow!", end = '')
        return
    else:
        item = ar[front]
        print("Element deleted from queue is : ", end = '')
        print(item, end = '')
        print()
        if rear == front:
            rear = -1
            front = -1
        else:
            front = front + 1
        front += 1
def display():
    global n
    global rear
    global front
    if front == - 1:
        print("Queue is empty", end = '')
        print()
        return
    else:
        print("Elements are : ", end = ' ')
        i = front
        while i <= rear:
            print(ar[i], end = '')
            print(" ", end = '')
            i += 1
        print()
ch = None
print("1: enqueue", end = '')
print()
print("2: dequeue", end = '')
print()
print("3: Display front element of queue", end = '')
print()
print("4: Display all the elements of queue", end = '')
print()
print("5: Exit", end = '')
print()
condition = True
while condition:
    ch = int(input("Enter your choice:"))
    if ch == 1:
        item = int(input("enter element to be inserted:"))
        enqueue(item)
    elif ch == 2:
        dequeue()
    elif ch == 3:
        display()
    elif ch == 4:
        print("Exit", end = '')
        print("\n", end = '')
    else:
        print("Invalid choice", end = '')
        print()
    condition = ch!=4

