import a4
import pytest
from pytest import approx

def assertEqual(a,b):
    assert a == b

def assertAlmostEqual(a,b,c):
    assert a == approx(b,c)

def assertFalse(a):
    assert not a

def assertTrue(a):
    assert a

er_msg = ["Data Error: 0 values", "Data Error: 0 in data"]

x1 = []
x2 = [1,0,0,1]
x3 = [1,2,3,4,0]
x4 = [5]
x5 = [-1,0,2,2,0,-1]

x = [x1,x2,x3,x4,x5]
y = [(), (0, 2), (0, 1), (5, 1), (-1, 2)]
p = {'Act': 63746.04999999999, 'gold': 4, 'silver': 20, 'platinum': 5, 'paladium': 10}

def test_Problem1_block():
    assert a4.block(0)  == ""
    assert a4.block(1)  == "*\n"
    assert a4.block(3)  == "***\n***\n***\n"

def test_Problem1_square():
    assert a4.square(0) == ""
    assert a4.square(1) == "*\n"
    assert a4.square(3) == "***\n* *\n***\n"
    assert a4.square(5) == "*****\n*   *\n*   *\n*   *\n*****\n"

def test_Problem2():
    p1 = {'act': 8166.85, 'holdings': {'gold': (1, 1833.15), 'silver': (0, 0), 'platinum': (0, 0), 'paladium': (0, 0)}}
    p2 = {'act': 1867.3200000000002, 'holdings': {'gold': (3, 5499.450000000001), 'silver': (3, 82.83), 'platinum': (2, 2550.4), 'paladium': (0, 0)}} 
    assert a4.purchase(a4.portfolio,a4.Au, 1)
    assert not a4.purchase(a4.portfolio,a4.Au, 1000)
    assert a4.portfolio == p1
    a4.purchase(a4.portfolio,a4.Au, 2)
    a4.purchase(a4.portfolio,a4.Ag,3)
    a4.purchase(a4.portfolio,a4.Pt,2)
    assert a4.portfolio == p2
    assert a4.how_much(a4.portfolio, a4.Pd) == 0.0
    

def test_Problem3():
    
    x1 = []
    x2 = [1,0,0,1]
    x3 = [1,2,3,4,0]
    x4 = [5]
    x5 = [-1,0,2,2,0,-1]
    x = [x1,x2,x3,x4,x5]
    y = [(),(0, 2),(0, 1),(5, 1),(-1, 2)]
    for i,j in zip(x,y):
       assert a4.find_num_min(i) == j

x1 = [0,1,2,2,3,1,2,3,1,1,0,1]
x2 = [1,2,3,4,5,0,1,1,1,1,1,1,1,1]
x3 = [1,2,3,4,5,1]
x4 = [5,4,3,2,1]
xlst = [x1,x2,x3,x4, []]
ylst = [4,8,4,0,0]
@pytest.mark.parametrize("test_input,expected",tuple(zip(xlst,ylst)))
def test_Problem5(test_input, expected):
    assert a4.increase(test_input) == expected
    
def test_Problem6():
    f ="Two roads diverged in a yellow wood,\
        And sorry I could not travel both\
        And be one traveler, long I stood\
        And looked down one as far as I could\
        To where it bent in the undergrowth"
    g = "the quick brown fox jumped over the lazy dog"  
    fd = {'t': 11, 'w': 6, 'o': 20, 'r': 11, 'a': 10, 'd': 13, 's': 5, 'i': 7, 'v': 3, 'e': 15, 'g': 3, 'n': 12, 'y': 2, 'l': 8, 'c': 2, 'u': 3, 'b': 3, 'h': 4, 'k': 1, 'f': 1}
    gd = {'t': 2, 'h': 2, 'e': 4, 'q': 1, 'u': 2, 'i': 1, 'c': 1, 'k': 1, 'b': 1, 'r': 2, 'o': 4, 'w': 1, 'n': 1, 'f': 1, 'x': 1, 'j': 1, 'm': 1, 'p': 1, 'd': 2, 'v': 1, 'l': 1, 'a': 1, 'z': 1, 'y': 1, 'g': 1}
    assert a4.letter_count(f) == fd
    assert a4.letter_count(g) == gd

def test_Problem7():

    x = [4,3]
    y = [3,5]
    assert a4.vec_op(x,y,"+") == [7, 8]
    assert a4.vec_op(x,y,"-") == [1, -2]
    assert a4.dot_prod(x,y) == 27
    xa,xb = a4.scalar_vec(x,1/5)
    assert approx(xb) == 0.6
    assert xa == .8
    assert a4.euc_len(x) == 5.0
    assert approx(a4.euc_len(y),2) ==  5.83      
    assert approx(a4.ang_vec(x,y),2) == 22.17
    xa,xb = a4.unit_vec(x)
    assert approx(xb,1) == 0.6
    assert xa == .8
    assert approx(a4.euc_len(a4.unit_vec(x)),1) == 1.0

def test_Problem8():
    assert a4.tree_age([12,10], .5, .2) == 120
    assert a4.tree_age([1,1],0,.3) == 6
    assert a4.noninvasive_tree_age([12,10], "White Oak") == 123
    assert a4.noninvasive_tree_age([5, 5], "Red Oak") == 42

def test_Problem9():
    x1 = [1,0,1,0,"dog", "cat", "cat", (1,),(1,),(2,)]
    x2 = [[],[],"","",(),()]
    x3 = []
    x1s = [str(i) for i in a4.make_unique(x1)]
    x1a = list([str(i) for i in set(x1)])
    assert sorted(x1s) == sorted(x1a)
    x2s = [str(i) for i in a4.make_unique(x2)]
    assert sorted(x2s) == sorted(["[]", '', "()"])
    assertFalse(a4.make_unique(x3))

    assertEqual(a4.partition([1,2,3,4],0),[])
    assertEqual(sorted(a4.partition([1,2,3,4],2)),sorted([[1, 2], [3, 4]]) )
    assertEqual(sorted(a4.partition([1,2,3,4],1)),sorted([[1], [2], [3], [4]]))
    assertEqual(sorted(a4.partition([1,2,3,4],3)),sorted([[1, 2, 3], [4]]))
    assertEqual(sorted(a4.partition([1,2,3,4],4)),sorted([[1, 2, 3, 4]]))
    assertEqual(sorted(a4.partition([1,2,3,4],5)),sorted([[1, 2, 3, 4]]))

    assertEqual(sorted(a4.occurs_at_index([0,1,0,1,1],1)), sorted([1,3,4]))
    assertFalse(a4.occurs_at_index([0,1,0,1,1],2))
    assertEqual(sorted(a4.occurs_at_index([0,1,0,1,1],0)), sorted([0,2]))

    assertFalse(a4.intersect([],[1]))
    assertFalse(a4.intersect([2],[]))
    assertEqual(a4.intersect([1,1],[1,1,2]),[1])
    assertEqual(sorted(a4.intersect([2,1,2,3],[3,1,3])), sorted([3,1]))

    assertEqual(a4.optimum([],0),[])
    assertEqual(a4.optimum([],1),[])
    assertEqual(a4.optimum([1],1),1)
    assertEqual(a4.optimum([1],0),1)
    assertEqual(a4.optimum([1,1,-1,100,-100],0),-100)
    assertEqual(a4.optimum([1,1,-1,100,-100],1),100)

def test_Problem10():

    assertEqual(a4.sigma([]),[])
    assertEqual(a4.sigma([1,2,-3,3]),3)
    assertEqual(a4.sigma([100,10,1]),111)
    assertEqual(a4.sigma_square([]),[])
    assertEqual(a4.sigma_square([-1,1,1]),3)
    assertEqual(a4.sigma_square([10,2,3]),113)
    assertEqual(a4.sigma_product([1,2,3],[1,10,100]),321)
    assertEqual(a4.sigma_product([-1,-2,3],[9,0,3]),0)
    assertEqual(a4.sigma_product([],[]),[])

    assertEqual(a4.separate([]), [])
    assertEqual(a4.separate([[1],[2],[3],[4],[5]]),[[1, 2, 3, 4, 5]]) 
    assertEqual(a4.separate([[1,10],[2,20]]),[[1, 2], [10, 20]])
    assertEqual(a4.separate([[1,10,100],[2,20,200],[3,30,300]]), [[1, 2, 3], [10, 20, 30], [100, 200, 300]])
    assertEqual(a4.separate([[1,1],[2,3],[4,3],[3,2],[5,5]]), [[1, 2, 4, 3, 5], [1, 3, 3, 2, 5]])

    d1 = [[43,99],[21,65],[25,79],[42,75],[57,87],[59,81]]
    d2 = [[1,1],[2,3],[4,3],[3,2],[5,5]]

    a,b = a4.make_linear(d1)
    assertAlmostEqual(a,0.385,3)
    assertAlmostEqual(b,65.14,2)

    a,b = a4.make_linear(d2)
    assertAlmostEqual(a,0.8,1)
    assertAlmostEqual(b,0.4,1)
    
def test_Problem11():

    xtest = ["abc", 120, (1,2,3), [1,2,3]]
    ysolution = ["cba", 21, (3, 2, 1), [3, 2, 1]]
    for i,j in zip(xtest,ysolution):
        assertEqual(a4.reverse(i),j)

    xlst = ["Step on no pets.", "Was it a cat I saw?", "A",\
            "Eva, can I see bees in a cave?", "Uhh...", "Oreos yum!"]
    ylst = [True, True, True, True, False, False]

    for i,j in zip(xlst,ylst):
        assertEqual(a4.palindrome(i),j)

