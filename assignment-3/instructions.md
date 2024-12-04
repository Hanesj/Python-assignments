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
