import extracredit as ex
import pytest
import random as rn
from pytest import approx

print("__________________")
print("KEY")
print(". passed")
print("F,0,E did not pass")
print("__________________")



def test_q():
    assert ex.q(1, 3, -4) == (1.0, -4.0)
    assert ex.q(2, -4, 3) == ((1+0.7071067811865476j), (1-0.7071067811865476j))
    assert ex.q(3, 4, 2)  == ((-0.6666666666666666+0.47140452079103173j), (-0.6666666666666666-0.47140452079103173j))
    
def test_checkout():
    x1 = [[1, 1.45, 1],[3, 4.24, 1], [2, 14.00, 0], [4, 1.25, 1]]
    x2 = [[3, 2.05, 1],[1, 4.74, 0], [2, 4.00, 1], [5, 4.25, 1]]
    x3 = [[1, 2.05, 0],[1, 4.74, 1], [2, 4.00, 0], [5, 4.25, 0]]

    assert ex.checkout(x1) == approx(48.5119)
    assert ex.checkout(x2) == approx(42.618)
    assert ex.checkout(x3) == approx(36.3718)

def test_open_seat_count():
    s1 = [[1,0,0],[1,1,1],[1,1,0]]
    s2 = [[1]]
    s3 = [[1,1,0,1],[0,1,0,0],[0,0,0,1],[0,1,0,1]]
    
    assert ex.open_seat_count(s1) == 3
    assert ex.open_seat_count(s2) == 0
    assert ex.open_seat_count(s3) == 9


xlist = [2500, 2700, 2400, 2300, 2550, 2650, 2750, 2450, 2600, 2400]
def test_arithmetic_mean():
    assert ex.arithmetic_mean(xlist) == approx(2530.0)

def test_geo_mean():
    assert ex.geo_mean(xlist) == approx(2526.2203383616925)

def test_har_mean():
    assert ex.har_mean(xlist) == approx(2522.439190687068)

def test_RMS_mean():
    assert ex.RMS_mean(xlist) == approx(2533.7718918639853)
    

def test_ISBN():
    assert ex.valid_ISBN("0-691-11321-1") == True
    assert ex.valid_ISBN("0-691-12797-2") == True
    assert ex.valid_ISBN("0-324-33333-8") == False

