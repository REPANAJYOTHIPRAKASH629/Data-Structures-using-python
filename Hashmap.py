class HashTable:
    def __init__(self):
        self.MAX=15
        self.arr=[[] for i in range(self.MAX)]

    def gethash(self,key):
        h=0
        for char in key:
            h+=ord(char)
        return h % self.MAX

    def setitem(self,key,val):
        h=self.gethash(key)
        found=False
        for idx, element in enumerate(self.arr[h]):
            if len(element)==2 and element[0]==key:
               self.arr[h][idx]=(key,val)
               found=True
               break
        if not found:
               self.arr[h].append((key,val))

    def getitem(self,key):
        h=self.gethash(key)
        return self.arr[h]

    def delitem(self,key):
        h=self.get_hash(key)
        self.arr[h]=None

    def display(self):
        for i in self.arr:
            print(i,end="")
        print()
        
t=HashTable()

while True:
	ch=int(input("Enter your choice 1.Insert 2.Delete 3.Get value of key 4.Display 5.Exit"))
	
	if ch==1:
		print("Enter the key and value")
		key=input()
		value=int(input())
		t.setitem(key,value)
	elif ch==2:
		print("Enter the key to delete")
		key=input()
		t. delitem(key)
	elif ch==3:
		print("Enter key to know its value")
		key=input()
		print(t.getitem(key))
	elif ch==4:
		t.display()
	elif ch==5:
		break
	else:
	 	print("Invalid choice")
		
		
