# Assignment 9

- Username: hase
- Commit hash used for grading: 715c9dfa026d097a4d7858cdd0863b5ab787588f

Rubric (see Canvas page):

| Criterion           | Total Points |
| ------------------- | ------------ |
| Code Tests   | 50                  |
| Docstrings  | 15                   |
| Code Review & style   | 20         |
| Student Tests | 15                 |  


## Total Score: 94/100
Please double-check that your Canvas score reflects what is shown here. 



## Code Tests (44.0/50 pts)
 
- `pop`: 2/2
- `error`: 0/6


- `get_dic`: 5/5
- `get_state_pop`: 5/5
- `scd`: 4/4
- `ccc`: 5/6
- `sdd`: 6/5
- `usdd`: 5/5


- `simpson`: 12.0/12


## Docstrings and Comments (_/15 pts)
Student's functions all have properly formatted docstrings in the right place. You loose 1,5 point for each function that doesn't have proper docstrings or comment.

- Problem 1: 3/3
- Problem 2: 10/10
- Problem 3: 2/2


TA Comments: 



## Code Review & style (_/20 pts)
Your code is reviewed for proper style and legibility.
If your code passes the autograder, but you violated the specifications (for example using forbidden python features/functions), you will lose the autograder points as well!

- Problem 1:
    - `pop`: 2/2
    - `error`: 2/2
    - TA Comments: 

- Problem 2:
    - `scd`: 2/2
    - `ccc`: 2/2
    - `sdd`: 2/2
    - `usdd`: 2/2
    - `get_dic`: 2/2
    - `get_state_pop`: 2/2
    - TA Comments: 

- Problem 3:
    - `simpson`: 4/4
    - TA Comments: 


- Forbidden functions used (if any): _


## Student Tests (_/15 pts)
We check that you added reasonably comprehensive test cases to your `test_a9.py` file. 

- `test_pop`: 4/4
- `test_error`: 4/4
- `test_get_data`: 3/3
- `test_simpson`: 4/4



## Pytest Results
- Test test_error threw error:
Traceback (most recent call last):
  File "a9_RunAutograder.py", line 126, in <module>
    for x, y, y_actual, result in f():
  File "./a9_grader.py", line 29, in test_error
    yield x, y, (a9.error(x)), (round(a9.error(x), 2) == round(y, 2))
  File "./a9.py", line 55, in error
    return (100/len(data))*sum                  #returning result that is the average of the summation in percentage
ZeroDivisionError: division by zero



