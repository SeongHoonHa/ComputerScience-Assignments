import pytest
from ppm_process import *

def test_process():
    assert process(['255 0 0 0 255 0\n', '255 255 255 0 0 0\n'],2,2) == [[255,0,0,0,255,0],[255,255,255, 0, 0, 0]]
    assert process(['255 0 0 0 255 0\n', '255 255 255 0 0 0\n', '255 255 255 0 154 154\n'],3,2) == [[255,0,0,0,255,0],[255,255,255,0,0,0],[255,255,255,0,154,154]]

small_ppm = [[255,0,0,0,255,0,0,0,255,255,255,255],[0,0,0,255,0,0,0,255,0,0,0,255],[255,0,255,0,0,0,255,0,0,0,255,0],[0,255,255,255,0,255,0,0,0,255,0,0],[255,0,0,0,255,0,0,0,255,255,255,255],[0,0,0,255,0,0,0,255,0,0,0,255]]
def test_scale():
    assert scale(small_ppm,3,1) == [[255, 0, 0, 0, 255, 0, 0, 0, 255, 255, 255, 255],[0, 255, 255, 255, 0, 255, 0, 0, 0, 255, 0, 0]]
    assert scale(small_ppm,3,2) == [[255, 0, 0, 0, 0, 255], [0, 255, 255, 0, 0, 0]]