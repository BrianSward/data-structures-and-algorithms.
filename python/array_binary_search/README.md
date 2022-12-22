# Binary Search of Sorted Array
<!-- Description of the challenge -->

Write a function called BinarySearch which takes in 2 parameters: a sorted array
and the search key. Without utilizing any of the built-in methods available to your
language, return the index of the array’s element that is equal to the value of the
search key, or -1 if the element is not in the array.

## Whiteboard Process
<!-- Embedded whiteboard image -->
![whiteboard_class_03](whiteboard_class03.jpg)


## Approach & Efficiency
<!-- What approach did you take? Discuss Why. What is the Big O space/time for this approach? -->

I had to read about binary search quite a bit and the understanding i got was you had to find the beg and the end
and then find the middle. Once there do a quick check around and see if you have what you need.
If not repeat the process after throwing out the unwanted portion of the list.

I answered these like the description on the whiteboard, but i think time is linear - O(N) because as the length of
the list grows so will the number of steps to find the item. I think space is constant - O(1).
