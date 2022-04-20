import pytest
from ppm_modify import *

def test_color_translate():
    assert type(color_translate("11 200 124 13 142 144 111 124 90")) == str
    assert color_translate("11 200 124 13 142 144 111 124 90") == "255 255 153 153 153 0 0 153 0"

def test_grey_scale():
    assert type(grey_scale("11 200 124 13 142 144 111 124 90")) == str
    assert grey_scale("11 200 124 13 142 144 111 124 90") == "235 235 235 202 202 202 189 189 189"