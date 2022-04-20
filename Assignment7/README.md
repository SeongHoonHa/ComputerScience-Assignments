# Assignment 7

Username: hase
Commit hash used for grading: 05368c45706db19740b3c92467885f0ff9edd39d

Rubric (see Canvas page):

| Criterion           | Total Points |
| ------------------- | ------------ |
| Lab checkoff  | 10                 |
| Code Tests   | 30                  |
| Docstrings  | 20                   |
| Code Review & style   | 30         |
| Student Tests | 10                 |

## Total Score: 98.5/100
Please double-check that your Canvas score reflects what is shown here. 


## Lab checkoff (10/10 pts)
The lab checkoff was waived for HW7 so all students get full points for lab check-off.


## Code Tests (28.5/30 pts)
 
- `process`: 4.5/6
- `read_ppm`: 6/6
- `write_ppm`: 3/3
- Written file has correct header:3/3
- `scale`: 12/12



## Docstrings and Comments (20/20 pts)
Student's functions all have properly formatted docstrings in the right place.
- `process`: 5/5
- `read_ppm`: 5/5
- `write_ppm`: 5/5
- `scale`: 5/5


TA Comments: 



## Code Review & style (30/30 pts)
Your code is reviewed for proper style and legibility.
If your code passes the autograder, but you violated the specifications (for example using forbidden python features/functions), you will lose the autograder points as well!
- `process`: 6/6
- `read_ppm`: 6/6
- `write_ppm`: 6/6
- `scale`: 6/6
- `main` (the function ask the user for row_scale and col_scale (i.e. input), checked that user entered an integer): 6/6

TA Comments: 

- Forbidden functions used (if any): _


## Student Tests (10/10 pts)
We check that you added reasonably comprehensive test cases to your `test_ppm_process.py` file.
- `test_process`: 5/5
- `test_scale`: 5/5



## Pytest Results
- Test test_process threw error:
Traceback (most recent call last):
  File "2.5-RunAutograder.py", line 178, in <module>
    for x, y, y_actual, result in f():
  File "./a7_grader.py", line 114, in test_process
    y_actual = ppm_process.process(x, 2, 2)
  File "./ppm_process.py", line 33, in process
    small_list.append(int(line[col]))       #appending column elements and making the elements as integer
IndexError: list index out of range



