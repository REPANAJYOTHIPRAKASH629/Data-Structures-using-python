# Data-Structures-using-python

BREADTH FIRST SEARCH

![image](https://user-images.githubusercontent.com/98946604/209763645-b3a51d2b-36d7-45b7-906f-c9e30c23304f.png)


Breadth-First Search (BFS) is an algorithm used for traversing graphs or trees. 
Traversing means visiting each node of the graph. 
Breadth-First Search is a recursive algorithm to search all the vertices of a graph or a tree. 
BFS in python can be implemented by using data structures like a dictionary and lists. 
Breadth-First Search in tree and graph is almost the same. 
The only difference is that the graph may contain cycles, so we may traverse to the same node again.

BFS Algorithm

Before learning the python code for Breadth-First and its output, let us go through the algorithm it follows for the same. 
We can take the example of Rubik’s Cube for the instance. 
Rubik’s Cube is seen as searching for a path to convert it from a full mess of colors to a single color. 
So comparing the Rubik’s Cube to the graph, we can say that the possible state of the cube is corresponding to the nodes of the graph and the possible actions of the cube is corresponding to the edges of the graph.

As breadth-first search is the process of traversing each node of the graph, a standard BFS algorithm traverses each vertex of the graph into two parts: 1) Visited 2) Not Visited. So, the purpose of the algorithm is to visit all the vertex while avoiding cycles.

BFS starts from a node, then it checks all the nodes at distance one from the beginning node, then it checks all the nodes at distance two, and so on. So as to recollect the nodes to be visited, BFS uses a queue.

The steps of the algorithm work as follow:

 Start by putting any one of the graph’s vertices at the back of the queue.
 Now take the front item of the queue and add it to the visited list.
 Create a list of that vertex's adjacent nodes. Add those which are not within the visited list to the rear of the queue.
 Keep continuing steps two and three till the queue is empty.
Many times, a graph may contain two different disconnected parts and therefore to make sure that we have visited every vertex, we can also run the BFS algorithm at every node.

DEPTH FIRST SEARCH

![image](https://user-images.githubusercontent.com/98946604/209763688-21455d58-5bcf-42b0-88b7-de33b6648087.png)


The Depth-First Search is a recursive algorithm that uses the concept of backtracking. 
It involves thorough searches of all the nodes by going ahead if potential, else by backtracking. 
Here, the word backtrack means once you are moving forward and there are not any more nodes along the present path, you progress backward on an equivalent path to seek out nodes to traverse. 
All the nodes are progressing to be visited on the current path until all the unvisited nodes are traversed after which subsequent paths are going to be selected.

DFS Algorithm

Before learning the python code for Depth-First and its output, let us go through the algorithm it follows for the same. The recursive method of the Depth-First Search algorithm is implemented using stack. A standard Depth-First Search implementation puts every vertex of the graph into one in all 2 categories: 1) Visited 2) Not Visited. The only purpose of this algorithm is to visit all the vertex of the graph avoiding cycles.

The DSF algorithm follows as:

We will start by putting any one of the graph's vertex on top of the stack.
After that take the top item of the stack and add it to the visited list of the vertex.
Next, create a list of that adjacent node of the vertex. Add the ones which aren't in the visited list of vertexes to the top of the stack.
Lastly, keep repeating steps 2 and 3 until the stack is empty.



DOUBLY LINKED LIST


![image](https://user-images.githubusercontent.com/98946604/209760945-6d679d0d-177b-4b3c-945e-cd81e77a6e18.png)

Another list-like data structure you may come across or need to use is the doubly linked list. This is a list structure in which each cell in the list has a pointer to the cell before it and also a pointer to the cell behind it. For example:


Normal linked lists have the links going one way, so if we want to run a pointer through the elements of a list we have to start at one end and move to the other one element at a time. We have seen the case of a list structure with an extra pointer to the last element in the list which makes it easier to add new items to the back of a list. A doubly-linked list structure is useful where we might want to run both ways in a list with equal convenience.

One abstract data type where we might want to use a doubly-linked list for implementation is a list with an insertion point (which is also known as a "sequence"). In the abstract, we can think of this as something like [a,b^,c,d] where the ^ symbol represents the insertion point. The operations on the structure are:

Return the current element which is the element at the insertion point, in the above case, b.

Insert a new element. If the element we are inserting is e then the state from the above after the operation would be [a,b,e^,c,d]. The element is inserted following the insertion point, and this point becomes the new insertion point.

Move the insertion point forward. If we follow from after the previous insert operation, the state becomes [a,b,e,c^,d].

Delete the current element. This deletes the element which is the current insertion point.
Following on from the situation above after the forward operation, we get [a,b,e,d^]. 
Note the insertion point becomes the element which was after the deleted element.

Move the insertion point backwards. Applying this operation next gives us [a,b,e^,d].

We also have an operation which says whether the list is empty, one which says whether the insertion point is the first element and one which says whether the insertion point is the last element. 
If the list is empty, neither the forward, backward or delete operations can work. 
If the current position is the first element, the backward operation cannot work, if the current position is the last element, the forward operation won't work.

The data structure representing this has a double linked list, with a pointer pointing to the cell of the current position as the field of an object:

Inserting a new element involves creating a new cell, and rearranging the pointers so they correctly reflect a doubly linked list with the current position pointer pointing to the new cell:

Moving the insertion point forward or backwards simply involves following one link in the appropriate direction down the chain, for example, forward from the above gives:

Deleting involves more rearrangement of pointers:

When dealing with inserting or deleting, special account needs to be taken of inserting or deleting at the end of ths list, or inserting into an empty list. 
When the last element in the list is deleted, the insertion point becomes the new last element since it cannot move forward to the next element.



 LINKED LIST
 
 A linked list is a dynamic data structure, which means that the size of the list can change at run time. You can imagine a linked list as a chain where each link is connected to the next one to form a sequence with a start and an end.

Each element in a linked list is called a node. Each node stores:

The data relating to the element
A pointer to the next node
There is also a separate pointer that indicates the first element in the list (the head of the list). This has a null value when the list is empty. The next node pointer of the last element in the list always points to a null value to mark the end of the list.

A linked list with four nodes (each containing a number) can be depicted with the following diagram:

![image](https://user-images.githubusercontent.com/98946604/209761254-302d5b01-d8f5-4215-9ec7-16a58ade4e71.png)

 INFIX TO POSTFIX CONVERSTION
 
 Algorithm to convert an Infix expression to a Postfix expression. 
 
 Check below example.

Step 0. Tokenize the infix expression. i.e Store each element i.e ( operator / operand / parentheses ) of an infix expression into a list / queue.

Step 1. Push “(” onto a stack and append “)” to the tokenized infix expression list / queue.

Step 2. For each element ( operator / operand / parentheses ) of the tokenized infix expression stored in the list/queue repeat steps 3 up to 6.

Step 3. If the token equals “(”, push it onto the top of the stack.

Step 4. If the token equals “)”, pop out all the operators from the stack and append them to the postfix expression till an opening bracket i.e “(” is found.

Step 5. If the token equals “*” or “/” or “+” or “-” or “^”, pop out operators with higher precedence at the top of the stack and append them to the postfix
expression. Push current token onto the stack.

Step 6. If the token is an operand, append it to the postfix expression. (Positions of the operands do not change in the postfix expression so append an operand as it is.)

![image](https://user-images.githubusercontent.com/98946604/209765223-c6ffcbe6-beda-40d8-93a6-e50f644bc89b.png)

 
 
INSERTION SORT


Insertion sort is the first sort I’m going to cover. 
There are some simpler sorting algorithms (like bubble sort) but insertion sort is simple to explain.
You likely use a method similar to insertion sort when you sort things in every day life. Additionally, it performs well enough on small data sets and you don’t have to have all the items up front. 
You can put new items in the correct place as they become available. This makes it an online sorting algorithm.

The setup for insertion sort is simple. 

You have two collections. 

One contains the unsorted items. 

The other contains the items that are sorted. 

If this is confusing, think about ordering a deck of cards. 

The shuffled (unsorted) cards are in the deck and the ones you’ve put in order are spread out on the table. 

Picture of cards laid out on a table

![image](https://user-images.githubusercontent.com/98946604/209761794-ca29db55-86cf-4ccb-ae16-773f39110412.png)

When you start, the collection of sorted items is empty. 

To sort you look at the first item in the unsorted collection and put it in the proper place in the sorted collection. 

Then you put the next item in place. Repeat until sorted.

![image](https://user-images.githubusercontent.com/98946604/209765055-1735fcfc-3311-4a72-adbb-5d23d0a408c0.png)


MERGE SORT 
merge sort is an efficient algorithm, and one of Divide and Conquer algorithms that splits the giving array into two halves, and then merge them in a sorted manner.

Approach : 

-> We will be creating 2 functions mergeSort() and merge()

-> In mergeSort(), we will divide the array around the middle element by making the recursive call :

1.mergeSort(arr,l,mid)   2. mergeSort(arr,mid+1,r)    

 where l = leftmost index of array, r = rightmost index of array , mid = middle index of array

-> In merge(),  we will use a temporary array named temp. This will be used to store elements in sorted order from both the arrays which we divided.

->From the temporary array, we will return back the elements in the original array.

-> Now , let   i = leftmost index of array, j = mid+1 index of array , f = leftmost index of array ( this index will be used to store elements in the original array ) 

-> While i<= mid && j <= r , we will store elements from both the parts in temporary array in sorted manner 

-> Finally will transfer all elements from the temporary array to the original array.

-> The red number shows an order of the steps in recursion calls

![image](https://user-images.githubusercontent.com/98946604/209764184-b79121f1-f4b3-44e8-9586-2351863548cf.png)



QUICK SORT

Quick Sort is one of the most popular and efficient sorting algorithms. It is generally the default sorting algorithms in many programming languages (including C++ and Java).

Even though the worst case time complexity of Quick Sort is O(n^2), it works at O(n log n) in most cases and is generally much faster than merge sort if implemented properly.

Quicksort is a divide-and-conquer algorithm. It works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. The sub-arrays are then sorted recursively.

Algorithm
Pick an element, called a pivot, from the array.
Partitioning: reorder the array so that all elements with values less than the pivot come before the pivot, while all elements with values greater than the pivot come after it (equal values can go either way). After this partitioning, the pivot is in its final position. This is called the partition operation.
Recursively apply the above steps to the sub-array of elements with smaller values and separately to the sub-array of elements with greater values.
The base case of the recursion is arrays of size zero or one, which are in order by definition, so they never need to be sorted.

There are multiple variants of quick sort depending on the choice of pivot. Some popular choices of pivots being:

First element of the unsorted array

Last element of the unsorted array

Middle element of the unsorted array

Random element from the unsorted array

The choice of pivot determines the chances of the algorithm hitting the worst case for the given array.

![image](https://user-images.githubusercontent.com/98946604/209764505-b6c264b1-5340-4b87-86ca-d1d300e50c5c.png)


SELECETION SORT

Selection sorting is conceptually the simplest sorting algorithm. It is an in-place (i.e. not

needing any auxiliary storage), comparison-based sorting technique.

This algorithm first finds the smallest element in the array and exchanges it with the element

in the first position, then find the second smallest element and exchange it with the element in

the second position, and continues in this way until the entire array is sorted. Basically it means

that the list is divided into two parts, the sorted part at the left end and the unsorted part at the

right end. Initially, the sorted part is empty and the unsorted part is the entire list. The smallest

element is selected from the unsorted array and swapped with the leftmost element, and that

element becomes a part of the sorted array. This process continues moving unsorted array

boundary by one element to the right.

![image](https://user-images.githubusercontent.com/98946604/209764985-96d12eeb-ec18-49e8-a38f-21ba4b3bdabb.png)


