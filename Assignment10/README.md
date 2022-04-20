# Assignment 10

- Username: hase
- Commit hash used for grading: ccd79e37502859ba4248371536b84a7fb0f8f6ea

Rubric (see Canvas page):

| Criterion           | Total Points |
| ------------------- | ------------ |
| Code Tests   | 50                  |
| Code Review & style   | 40         |
| Docstrings  | 10                   |


## Total Score: 96/100
Please double-check that your Canvas score reflects what is shown here. 


## Code Tests (47/50 pts)
 
- `sel_sqrt`: 1/4
- `inchtomtuple_lc`: 3/3
- `intomtuple_map`: 3/3

- `bmi_lc`: 3/3
- `bmi_map`: 3/3
- `bmi_cat`: 4/4

- `wbubble_sort`: 15/15
- `rsel_sort`: 15/15



## Code Review & style (39/40 pts)
Your code is reviewed for proper style and legibility.
If your code passes the autograder, but you violated the specifications (for example using forbidden python features/functions), you will lose the autograder points as well!

- Problem 1:
    - `sel_sqrt`: 2/2
    - `inchtomtuple_lc`: 5/5
    - `intomtuple_map`: 5/5
    - TA Comments: 

- Problem 2:
    - `bmi_calc`: 3/3
    - `bmi_lc`: 5/5
    - `bmi_map`: 5/5
    - `bmi_cat`: 5/5
    - TA Comments: 

- Problem 3:
    - `wbubble_sort`: 5/5
    - TA Comments: 

- Problem 4:
    - `rsel_sort`: 5/5
    - TA Comments:

- Forbidden functions used (if any): _



## Docstrings and Comments (10/10 pts)
Student's functions all have properly formatted docstrings in the right place. You loose 1-5 point for each function that doesn't have proper docstrings or comment.

- Problem 1: 3/3
- Problem 2: 4/4
- Problem 3: 1/1
- Problem 4: 2/2


TA Comments: 




## Pytest Results
- Test test_sel_sqrt on input (0, 10) should result in [0, 1.0, 4, 1.73, 8, 2.24, 12, 2.65, 16, 3.0, 20]
  but your code gave [0, 1.0, 4, 1.7320508075688772, 8, 2.23606797749979, 12, 2.6457513110645907, 16, 3.0, 20]
- Test test_sel_sqrt on input (10, 15) should result in [20, 3.32, 24, 3.61, 28, 3.87]
  but your code gave [20, 3.3166247903554, 24, 3.605551275463989, 28, 3.872983346207417]
- Test test_sel_sqrt on input (15, 20) should result in [3.87, 32, 4.12, 36, 4.36, 40]
  but your code gave [3.872983346207417, 32, 4.123105625617661, 36, 4.358898943540674, 40]

