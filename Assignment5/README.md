# Assignment5

Username: hase
Commit hash used for grading: 65fc7ab942e8fe6a61110c0b3f043eab3f9fc0f9

Rubric (see Canvas page):

| Criterion           | Total Points |
| ------------------- | ------------ |
| Code Tests   | 50           |
| Docstrings and Comments  | 20           |
| Code Review & style   | 30           |

## Total Score: 48/100
Please double-check that your Canvas score reflects what is shown here.

Your total score should be subtraction of violation points(see TA Comments in Code Review & style  ) from sum of the sections.


## Code Tests (0/50 pts)

- `log_2`: 0/1
- `makeProbability`: 0/3
- `entropy`: 0/3
- `magick`: 0/4
- `is_magic_square`: 0/4
- `generate_3_square`: 0/3
- `encrypt`: 0/3
- `decrypt`: 0/3
- `encrypt_sentence`: 0/3
- `decrypt_sentence`: 0/3
- `make_number`: 0/2
- `convert`: 0/2
- `mul_`: 0/3
- `add_`: 0/3
- `get_amino_acids`: 0/3
- `get_DNA`: 0/3
- `translate`: 0/4

## Docstrings and Comments (20/20 pts)

- Student's functions all have properly formatted docstrings in the right place: 17/17 pts

Note: -0.5 for each missing or obviously incomplete docstring.

- Student uses inline comments to explain major blocks, if necessary: 3/3 pts


TA Comments: 


## Code Review & style (28/30 pts)
Your code is reviewed for proper style and legibility.
If your code passes the autograder, but you violated the specifications (for example using forbidden python features/functions), you will lose the autograder points as well!

- Code Review `Problem 1`: 3/3
- Code Review `Problem 2`: 3/3
- Code Review `Problem 3`: 6/6
- Code Review `Problem 4`: 6/6
- Code Review `Problem 5`: 6/6
- Code Review `Problem 6`: 4/6

TA Comments: 

- The violations (If any): _
- Subtractions from code test section (If any): _



## Pytest Results
Traceback (most recent call last):
  File "2.5-RunAutograder.py", line 76, in <module>
    grader = reload(grader)
  File "/home/kbub/anaconda3/lib/python3.8/importlib/__init__.py", line 169, in reload
    _bootstrap._exec(spec, module)
  File "<frozen importlib._bootstrap>", line 604, in _exec
  File "<frozen importlib._bootstrap_external>", line 783, in exec_module
  File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
  File "./a5_grader.py", line 9, in <module>
    a5.init_data("./amino_acids.txt", "./DNA.txt")
  File "./a5.py", line 400, in init_data
    aa_d = get_amino_acids(amino_acids_file)
  File "./a5.py", line 332, in get_amino_acids
    content = content.split(sep=',')
AttributeError: 'list' object has no attribute 'split'
