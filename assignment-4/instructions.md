# Bunny Worker Locations

Keeping track of Commander Lambda's many bunny workers is starting to get tricky. You've been tasked with writing a program to match bunny worker IDs to cell locations.

The LAMBCHOP doomsday device takes up much of the interior of Commander Lambda's space station, and as a result the work areas have an unusual layout. They are stacked in a triangular shape, and the bunny workers are given numerical IDs starting from the corner, as follows:

  | 92
  | 79  93
  | 67  80  94
  | 56  68  81  95
  | 46  57  69  82  96
  | 37  47  58  70  83  97
  | 29  38  48  59  71  84  98 
  | 22  30  39  49  60  72  85  99
  | 16  23  31  40  50  61  73  86  100
  | 11  17  24  32  41  51  62  74  87  101
  | 7   12  18  25  33  42  52  63  75  88  102
  | 4   8   13  19  26  34  43  53  64  76  89  103
  | 2   5   9   14  20  27  35  44  54  65  77  90  104
  | 1   3   6   10  15  21  28  36  45  55  66  78  91  105

Each cell can be represented as points (x, y), with x being the distance from the vertical wall, and y being the height from the ground. 

For example, the bunny worker at (1, 1) has ID 1, the bunny worker at (3, 2) has ID 9, and the bunny worker at (2,3) has ID 8. This pattern of numbering continues indefinitely (Commander Lambda has been adding a LOT of workers). 

Write a function solution(x, y) which returns the worker ID of the bunny at location (x, y). Each value of x and y will be at least 1 and no greater than 100,000. Since the worker ID can be very large, return your solution as a string representation of the number.


## Solution

To provide a Python solution, edit solution.py so that your code works with the following test scenarios

Your code MUST work for all numbers between 1 to 100,000 in both the x and y axis.

Examples to test, additional tests is always good to include in your solution.py file

Input:
    solution.solution(1, 1)
Output:
    1

Input:
    solution.solution(5, 10)
Output:
    96

Input:
    solution.solution(3, 2)
Output:
    9


## Verification script

To test your code you can run the helper verification script by running

```python
python3 verification.py
```


## Extra task requirements

Your code MUST contain code comments in short describing how your code works if it is not totally obvious what is happening. This do not mean to put code comments on each line, but you should put it on the most important places so that Commander Lambda understands your code if he would choose to read it.

Install the code linting software flake8 https://flake8.pycqa.org/en/latest/ and ensure that your code has no errors or validation warnings. The one deviation that you are allowed when using flake8 is your max line length can be 160 characters.

To really validate your solution, additional random inputs will be tested between the numbers 1 to 100,000 to ensure your code works in all case:s according to the task description.
