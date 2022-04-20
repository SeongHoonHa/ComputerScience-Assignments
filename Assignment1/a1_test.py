import assignment1_1
import assignment1_2

import random as rn
import math 
import pytest

input = [0,1]

def test_myAnd():
    for i in input:
        for j in input:
            assert assignment1_1.myAnd(i,j) == (i and j)
    
def test_myOr():
    for i in input:
        for j in input:
            assert assignment1_1.myOr(i,j) == (i or j)

def test_myNot():
    for i in input:
        assert assignment1_1.myNot(i) == (not i)

def test_myNand():
    for i in input:
        for j in input:
            assert assignment1_1.myNand(i,j) == (not (i and j))

def test_myNor():
    for i in input:
        for j in input:
            assert assignment1_1.myNor(i,j) == (not (i or j))

def test_myImplication():
    for i in input:
        for j in input:
            assert assignment1_1.myImplication(i,j) == (not i) or j

def test_DeMorganNand():
    for i in input:
        for j in input:
            assert assignment1_1.DeMorganNand(i,j) == (not (not i and not j))

def test_myPlus():
    for i in range(10):
        x,y = rn.randint(-50,50), rn.randint(-50,50)
        assert assignment1_2.myPlus(x,y) == x + y

def test_myMinus():
    for i in range(10):
        x,y = rn.randint(-50,50), rn.randint(-50,50)
        assert assignment1_2.myMinus(x,y) == x - y

def test_myDivide():
    for i in range(10):
        x,y = rn.randint(-50,50), rn.randint(1,50)
        assert assignment1_2.myDivide(x,y) == x/y

def test_myProduct():
    for i in range(10):
        x,y = rn.randint(-50,50), rn.randint(-50,50)
        assert assignment1_2.myProduct(x,y) == x*y

def test_myExponent():
    for i in range(10):
        x,y = rn.randint(-50,50), rn.randint(-50,50)
        assert assignment1_2.myExponent(x,y) == x**y

def test_myRoot():
    for i in range(10):
        x,y = rn.randint(-50,50), rn.randint(1,50)
        assert assignment1_2.myRoot(x,y) == x**(1/y)

def test_myLog():
    #make sure don't ask math.log(1,1)
    for i in range(10):
        x,y = rn.randint(1,50), rn.randint(2,50)
        assert assignment1_2.myLog(x,y) == math.log(x,y)

def test_myAbs():
    for i in range(10):
        x = rn.randint(-50,50)
        assert assignment1_2.myAbs(x) == abs(x) 

def test_myExp():
    for i in range(10):
        x = rn.randint(-50,50)
        assert assignment1_2.myExp(x) == math.exp(x)

def test_myFloor():
    for i in range(10):
        x,y = rn.randint(-50,50),  rn.randint(1,50)
        assert assignment1_2.myFloor(x/y) == math.floor(x/y)


