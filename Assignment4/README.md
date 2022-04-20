# Assignment4

Username: hase
Commit hash used for grading: 34157040d48299f56773fc7e0a681a93de36e8a2

Rubric (see Canvas page):

| Criterion           | Total Points |
| ------------------- | ------------ |
| Passes Tests    | 40           |
| Code Review   | 40           |
| Docstrings and Comments   | 20         |

## Lab Checkoff
There was no assignment credit for lab checkoff this week.

## Total Score: 91/100
Please double-check that your Canvas score reflects what is shown here.

## Code Tests (32/40 pts)
- `block`: 1/1
- `square`: 0/2
- `purchase`: 2/2
- `how_much`: 1/1
- `find_num_min`: 2/2
- `search_me_me_bee`: 0/1
- `search_go_to_out`: 0/2
- `increase`: 2/2
- `letter_count`: 0/2
- `dot_prod`: 1/1
- `scalar_vec`: 1/1
- `euc_len`: 1/1
- `ang_vec`: 1/1
- `unit_vec`: 1/1
- `vec_op`: 2/2
- `tree_age`: 1/1
- `noninvasive_tree_age`: 1/1
- `make_unique`: 1/1
- `partition`: 2/2
- `occurs_at_index`: 1/1
- `intersect`: 1/1
- `optimum`: 2/2
- `sigma`: 1/1
- `sigma_square`: 1/1
- `sigma_product`: 1/1
- `separate`: 1/1
- `linear_model`: 1/1
- `make_linear`: 0/1
- `reverse`: 1/1
- `palindrome`: 2/2

## Code Review (39/40 pts)
Your code is reviewed for proper style.  For each problem, the TA who grades you will verify that you
- did not use functions or types that shortcut the work (e.g. `set` for `make_unique`)
- wrote legible code
- put your test code in `if __name__ == "__main__"` or in a pytest file

Breakdown:
- `Problem 1`: 4/4
- `Problem 2`: 4/4
- `Problem 3`: 4/4
- `Problem 4`: 4/4
- `Problem 5`: 4/4
- `Problem 6`: 4/4
- `Problem 7`: 4/4
- `Problem 8`: 4/3
- `Problem 9`: 2/3
- `Problem 10`: 3/3
- `Problem 11`: 3/3

TA Comments: `list` is a python keyword and should not be used as a variable name
Regrade for comments 

## Part 1 Docstrings and Comments (20/20 pts)
- Student's functions all have properly formatted docstrings: 0/15 pts

Note: -0.5 for each missing or obviously incomplete docstring.

- Student uses inline comments to explain major blocks, if necessary: 5/5 pts

TA Comments: 

## Pytest Results
Expected square(1) ==> *

Expected square(5) ==> *****
*   *
*   *
*   *
*****


Expected search_me_me_bee() ==> [[['M', 5], ['B', 1], ['E', 0]]]

Expected search_go_to_out() ==> at least is a list containing a list
Expected search_go_to_out() ==> [[['T', 2], ['O', 1], ['U', 0], ['G', 8]]]

Expected letter_count(the quick brown fox jumped over the lazy dog) ==> {'t': 2, 'h': 2, 'e': 4, 'q': 1, 'u': 2, 'i': 1, 'c': 1, 'k': 1, 'b': 1, 'r': 2, 'o': 4, 'w': 1, 'n': 1, 'f': 1, 'x': 1, 'j': 1, 'm': 1, 'p': 1, 'd': 2, 'v': 1, 'l': 1, 'a': 1, 'z': 1, 'y': 1, 'g': 1}
Expected letter_count(Two roads diverged in a yellow wood,                And sorry I could not travel both                And be one traveler, long I stood                And looked down one as far as I could                To where it bent in the undergrowth) ==> {'t': 11, 'w': 6, 'o': 20, 'r': 11, 'a': 10, 'd': 13, 's': 5, 'i': 7, 'v': 3, 'e': 15, 'g': 3, 'n': 12, 'y': 2, 'l': 8, 'c': 2, 'u': 3, 'b': 3, 'h': 4, 'k': 1, 'f': 1}

Function make_linear threw error: 'NoneType' object is not subscriptable

