# Tiling

The problem my friend suggested to me was the following: 
Suppose you have a rectangle of dimensions (m x n), where m and n are both integers. How many ways are there to break this rectangle into smaller "tiles", all of which are rectangles of the integer dimensions?
Note that for the purpose of this problem, we do not count two tilings to be distinct if we can obtain one from the other through a series of reflections and rotations.

## Usage
### 1xn Files
The 1xn files are used to calculate the number of tilings for a (1 x n) rectangle. 

#### 1xn.py
1xn.py prints out the total number of tilings for rectangles of length (1 x i), where i takes on all values from 1 to n (inclusive).

To use `1xn.py`, run:

```
$ python3 1xn.py n
```
Alternatively, running just `$ python3 1xn.py` will prompt you to enter an n, and then output the same result as with the command line arguments.

#### 1xnVisual.py
`1xnVisual.py` prints out all the tilings of rectangles of length (1 x n), for any inputted n. There are two ways to do this:

```
$ python3 1xnVisual.py n
```
will print all tilings of rectangles of length (1 x n), for whatever integer n you input, where n is some number. 

```
$ python3 1xnVisual.py
```
will prompt you to enter an n, and then print all tilings for that n.

### 2xn Files
#### 2xn.py
This file is extremely diverse, in theory. It will print out the total number of possible tilings for a (2 x n) grid. It takes up to 2 command line arguments:

* The first argument is a number n, and the program will consider all tilings of a (2 x n) grid. If there are no arguments, the command line will simply prompt you to enter an n
* The second argument, if present, is a json file consisting of a number of settings. This allows a great deal of flexibility in using the file. If no argument is given, `default.json` will be used. This option is still a work in progress, and once it is fleshed out, this file will have accompanying documentation on the various files.

#### 2xnFormulae.py
This file is to be used exactly like to `1xn.py` (either via command line arguments, or by being promptes), and inputting any n will output the number of possible tiling configurations for a (2 x n) grid. This is currently counts the total number of tilings, counting reflections and rotations of the same tiling as distinct. As we flesh out the mathematical approach to it, we will be able to make these formulae account for rotations and reflections, and hopefully answer some subproblems (for example: the number of symmetric tilings of a (2 x n) board).
