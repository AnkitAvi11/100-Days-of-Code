# Array Data Structure
An array is a collection of items stored at contiguous memomory locations. The idea is to store multiple items of the same type together. This makes it easier to calculate the position of each element by simply adding an offset to the base value, i.e., the main memory location of the first element of the array (generally denoted by the name of the array)


### Strengths :
- Fast Lookup : Retrieving the element at the given index takes O(1) time, regardless of the length of the array.
- Fast appends : Adding a new element at the end of the array takes O(1) time, if the array has space.


### Weaknesses : 
- Fixed Size : You need to specify how many elements you're going to store in the array ahead of time. (unless you are using a fancy dynamic array)

- Costly inserts and deletes : You have to "scoot over" the other elements to fill in or close gaps, which takes worst-case O(n) time.