import takehomemidterm
import pytest
import random as rn
from pytest import approx

# Feel free to add more test cases as you see fit
x1_str = ""
e1_unique = []
e1_transmat = []

xlist2 = []
per2 = 3
e2_runavg = []

def test_Problem1():

    assert e1_unique == takehomemidterm.unique_words(x1_str)
    assert e1_transmat == takehomemidterm.get_transition_matrix(x1_str)

def test_Problem2():

    assert e2_runavg ==  takehomemidterm.running_average(xlist2,per2)
