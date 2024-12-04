# Assignment 1:
# I Love Lance & Janice

You've caught two of your fellow minions passing coded notes back and forth -- while they're on duty, no less! Worse, you're pretty sure it's not job-related -- they're both huge fans of the space soap opera ""Lance & Janice"". You know how much Commander Lambda hates waste, so if you can prove that these minions are wasting time passing non-job-related notes, it'll put you that much closer to a promotion. 

Fortunately for you, the minions aren't exactly advanced cryptographers. In their code, every lowercase letter [a..z] is replaced with the corresponding one in [z..a], while every other character (including uppercase letters and punctuation) is left untouched.  That is, 'a' becomes 'z', 'b' becomes 'y', 'c' becomes 'x', etc.  For instance, the word ""vmxibkgrlm"", when decoded, would become ""encryption"".

Write a function called solution(s) which takes in a string and returns the deciphered string so you can show the commander proof that these minions are talking about ""Lance & Janice"" instead of doing their jobs.


## Task

To provide a Python solution, edit the file solution.py until your code passes the test case:s below


## Test cases

Your code MUST pass the following test cases, but you are encouraged to expand the tests to ensure you cover all possible scenarios.

Code input: 
    solution.solution("wrw blf hvv ozhg mrtsg'h vkrhlwv?")
Output:
    did you see last night's episode?

Code input:
    solution.solution("Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!")
Output:
    Yeah! I can't believe Lance lost his job at the colony!!


## Verification script

To test your code you can run the helper verification script by running

```python
python3 verification.py
```


## Hints and help

If you import the python standard library module "string" you can find the entire alphabet in that module as a variable

# Assignment 2:
As you walk through the door, commander Lambda yells in your direction. "You there! Your state appears to be idle. Come help us repair the corruption in this spreadsheet - if we take another millisecond, we'll have to display an hourglass cursor!"

The spreadsheet consists of rows of apparently-random numbers. To make sure the recovery process is on the right track, they need you to calculate the spreadsheet's checksum. For each row, determine the difference between the largest value and the smallest value; the checksum is the sum of all of these differences.

For example, given the following CSV spreadsheet:

5 1 9 5
7 5 3
2 4 6 8

The first row's largest and smallest values are 9 and 1, and their difference is 8

The second row's largest and smallest values are 7 and 3, and their difference is 4

The third row's difference is 6

In this example, the spreadsheet's checksum would be 8 + 4 + 6 = 18

---

Given the file "puzzle-file-2.csv", open it with CSV, read the file content and calculate the the checksum for the spreadsheet and print it to the terminal

# Assignment 3:
# Indexing texts

Commander Lambda wanted to know which one of his minions that had the best knowledge of the english language and who had the best communication skills. He collected all chatt logs from his minions and have asked you to make a script that do some basic analysis on the text files commander Lambda have collected. We don't really know why Commander Lambda wants this information, but i am sure he has his reasons...

To verify each text file so that Lambda can decide who needs to work on their writing skills, you need to write a program for him that will read the entire contents of each file in a folder and calculate a few different things from each submission.

Write a function `solution(filename)` that will open the given file path, read all the content from this file and start to process all content and figure out the following things

1. What is the shortest word used in the text? If there is more then 1 different word with the same lenght, print all of them
2. Count each occurence of each different letter, number, symbol in the entire text file and print them out. Lower case and upper case letters count as different letters. Print each letter/symbol on a new line with the counter saying how many times. Important here that you sort everything in alphabeitcal order.
3. The longest word used in the text. If there is multiple words with the same lenght, then print all of them
4. How many words and how many lines the submission was

All of this data should also be put into a dict object and returned from your function so commander Lambda can look at the data himself.

You are free to design your return data and your prints however you like, as long as commander Lambda can easily understand the output and the data he will be recieving back.

The verification.py script is intentionally broken due to this. You need to update that script once you have decided how your returned data structure will look like.


## Solution

To provide a Python solution, edit solution.py so that your code works with the following test scenarios

Input:
    solution.solution("minion-1.txt")
Output:
    Shortest word: ...

    a: 1
    b: 5
    c: 18
    ...
    z: 0
    A: 7
    ...
    !: 9
    -: 5
    .: 3
    
    Longest word: Pneumonoultramicroscopicsilicovolcanoconiosis

    How many words: 3781

    How many lines: 20

Input:
    solution.solution("minion-2.txt)
Output:
    Shortest word: ...

    a: 1
    b: 5
    c: 18
    ...
    z: 0
    A: 7
    ...
    !: 9
    -: 5
    .: 3
    
    Longest word: Pneumonoultramicroscopicsilicovolcanoconiosis

    How many words: 1753

    How many lines: 19
    

Input:
    solution.solution("minion-3.txt)
Output:
    Shortest word: ...

    a: 4
    b: 8
    c: 13
    ...
    z: 1
    A: 5
    ...
    !: 2
    -: 4
    .: 8
    
    Longest word: Pneumonoultramicroscopicsilicovolcanoconiosis

    How many words: 2938

    How many lines: 18


## Verification script

To test your code you can run the helper verification script by running

```python
python3 verification.py
```
# Assignment 4:
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


