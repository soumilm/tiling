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

The following way will print all tilings of rectangles of length (1 x n), for whatever integer n you input via command-line arguments.
```
$ python3 1xnVisual.py n
```

On the other hand, omitting the command-line argument will make python prompt you for your value of `n`.
```
$ python3 1xnVisual.py
```

### 2xn Files
#### 2xn.py
This file is extremely diverse, in theory. It will print out the total number of possible tilings for a (2 x n) grid. It also prints out the total number of configurations it is brute forcing when it starts, and gives periodic updates every 100,000 configurations, when the total number of configurations exceeds that number.

The file takes up to 2 command line arguments:

* The first argument is a number n, and the program will consider all tilings of a (2 x n) grid. If there are no arguments, the command line will simply prompt you to enter an n
* The second argument, if present, is a json file consisting of a number of settings. This allows a great deal of flexibility in using the file. If no argument is given, `default.json` will be used. This option is still a work in progress, and once it is fleshed out, this file will have accompanying documentation on the various files.

##### Configurations file

There are a few attributes you can set. Your configuration file need not define all of these - for each attribute not defined, the default value (as defined in `default.json`) will be used.

* `display` (type: `bool`; default: `false`): Setting this value to `true` will print out all possible configurations. Note that this substantially slows down the code.
* `rotate` (type: `bool`; default: `true`): This value determins whether to count vavrious rotations/reflections of a tiling as distinct. In particular, setting it to `true` will count them as the same configuration, whereas setting it to `false` will count each rotation as distinct.
* `selectiveCounting` (type: `object`; default: see subpoints): This object allows you to count just a subset of all possible tiling configurations, based on the degrees of symmetry.
  * `leftRightSymmetric` (type: `bool`; default: `true`): Setting this to `true` will include all configurations that are symmetric upon reflecting along the central vertical axis (aka y-axis). Setting this to `false` will exclude all such configurations.
  * `topBottomSymmetric` (type: `bool`; default: `true`): Setting this to `true` will include all configurations that are symmetric upon reflecting along the central horizontal axis (aka x-axis). Setting this to `false` will exclude all such configurations.
  * `rotationallySymmetric` (type: `bool`; default: `true`): Setting this to `true` will include all configurations that are symmetric upon a 180-degree rotation. Setting this to `false` will exclude all such configurations.
  * `asymmetric` (type: `bool`; default: `true`): Setting this to `true` will include all configurations that are not symmetric by any of the above three definitions. Setting this to `false` will exclude all such configurations.

#### 2xnFormulae.py
This file is to be used exactly like to `1xn.py` (either via command line arguments, or by being promptes), and inputting any n will output the number of possible tiling configurations for a (2 x n) grid. This is currently counts the total number of tilings, counting reflections and rotations of the same tiling as distinct. As we flesh out the mathematical approach to it, we will be able to make these formulae account for rotations and reflections, and hopefully answer some subproblems (for example: the number of symmetric tilings of a (2 x n) board).
