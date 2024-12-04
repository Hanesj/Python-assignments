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
