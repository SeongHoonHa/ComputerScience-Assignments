import a9
import pytest
import math
from pytest import approx

def test_pop():
    # replace with your tests
    assert type(a9.pop(60)) == float
    assert a9.pop(60) == 3298.428492408121
    assert a9.pop(70) == 3788.545163434662

def test_error():
    # replace with your tests
    data_one = [[0,1650],[10,1750],[20,1860],[30,2070],[40,2300],[50,2560],[60,3040],[70,3710],[80,4450],[90,5280],[100,6080],[110,6870]]
    data_two = [[0,1650],[10,1750],[20,1860],[30,2070],[40,2300],[50,2560],[60,3040],[70,3710],[80,4450],[90,5280],[100,6080]]
    assert type(a9.error(data_one)) == float
    assert a9.error(data_one) == 6.196115261019246
    assert a9.error(data_two) == 6.393874976115099

def test_get_data():
    # replace with your tests
    data = [[0,1650],[10,1750],[20,1860],[30,2070],[40,2300],[50,2560],[60,3040],[70,3710],[80,4450],[90,5280],[100,6080],[110,6870]]
    assert type(a9.get_data(".", "pop.txt")) == list
    assert a9.get_data(".", "pop.txt") == data
    assert a9.get_data(".","pop.txt")[3] == [30,2070]

def test_get_dic():
    # replace with your tests
    assert type(a9.get_dic("us-counties.csv")) == dict
    assert a9.get_dic("us-counties.csv")[('Alabama','Autauga')] == [5557, 85]
    assert a9.get_dic("us-counties.csv")[('Arkansas','Crawford')] == [5611, 92]

def test_get_state_pop():
    # replace with your tests
    assert type(a9.get_state_pop("sp.csv")) == dict
    assert a9.get_state_pop("sp.csv")['Arizona'] == 7278717
    assert a9.get_state_pop("sp.csv")['Kansas'] == 2913314
def test_covid():
    # no additional tests required
    dic = a9.get_dic("us-counties.csv")
    state_pop = a9.get_state_pop("sp.csv")
    assert a9.ccc(dic,(0,2))[(0,2)] == 896
    assert a9.scd("Alabama", dic) == 8166
    assert a9.usdd(dic,state_pop)["Texas"] == 0.103

@pytest.mark.parametrize("test_input,expected", 
    [   
        ((lambda x: 1           ,0,10,100), 10),
        ((lambda x: x           ,0,10,100), 50),
        ((lambda x: 3*x*x + 1   ,0,6,100),6**3+6),
    ])
def test_simpson(test_input,expected):
    # no additional tests required
    assert a9.simpson(*test_input) == approx(expected)
