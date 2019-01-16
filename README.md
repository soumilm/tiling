# tiling

The problem my friend suggested to me was the following: 
Suppose you have a rectangle of dimensions (m x n), where m and n are both integers. How many ways are there to break this rectangle into smaller "tiles", all of which are rectangles of the integer dimensions?
Note that for the purpose of this problem, reflections and rotations of the same tiling are not considered to be distinct.

## usage

The 1xn files are used to calculate the number of tilings for a (1 x n) rectangle. 

* 1xn.py prints out the total number of tilings for rectangles of length (1 x n), where n takes on values from 2 to 12 (inclusive)
* 1xnVisual.py prints out all the tilings of rectangles of length (1 x n), for any inputted n. There are two ways to do this:

```
$ python3 1xnVisual.py n
```
will print all tilings of rectangles of length (1 x n), for whatever integer n you input

```
$ python3 1xnVisual.py
```
will prompt you to enter an n, and then print all tilings for that n

Both 2xn files are used exactly the same way as the 1xn file, but 2xnFast is and 2xnVisual is not
