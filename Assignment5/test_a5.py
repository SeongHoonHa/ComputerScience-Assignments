import a5
import pytest
import random as rn
from pytest import approx

a5.init_data("./amino_acids.txt", "./DNA.txt")

s1 = ['a', 'b', 'a', 'b', 'a', 'b', 'b', 'b']
s2 = [(1), (2), (3), (4)]
s3 = [1]
s4 = [1, 2]
xlst = [s1, s2, s3, s4]
elst = [0.9544340029249649, 2.0, -0.0, 1.0]

ms1 = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
ms2 = [[4, 9, 2], [3, 5, 7], [8, 2, 6]]


@pytest.mark.parametrize("test_input,expected", list(zip(xlst, elst)))
def test_Problem1(test_input, expected):
    assert a5.entropy(a5.makeProbability(test_input)) == approx(expected,1)


s1 = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]  # True
s2 = [[8, 1, 6], [3, 5, 7], [4, 9, 2]]  # True
s3 = [[8, 6, 1], [3, 6, 7], [4, 9, 2]]  # False
s4 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]  # False
s = [s1, s2, s3, s4]
an = [True, True, False, False]


@pytest.mark.parametrize("test_input,expected", list(zip(s, an)))
def test_Problem3(test_input, expected):
    assert a5.is_magic_square(test_input) == expected


@pytest.mark.parametrize("test_input", list(range(1, 9)))
def test_Problem4(test_input):
    xs = "the quick brown fox jumps over the lazy dog"
    ys = "two roads diverged in a yellow wood"
    shift = rn.randint(1, 10)
    assert a5.decrypt_sentence(a5.encrypt_sentence(
        xs, test_input), test_input) == xs
    assert a5.decrypt_sentence(a5.encrypt_sentence(
        ys, test_input), test_input) == ys


def test_Problem5():
    n1, n2, n3, n4 = 5, 4, 3, 4
    base2, base10, base3, base4 = 2, 10, 3, 4

    x1 = a5.make_number(n1, base2)
    y1 = a5.make_number(n2, base2)
    zz = a5.make_number(4, base3)
    yy = a5.make_number(3, base4)
    assert x1 == ['101', 2]
    assert y1 == ['100', 2]
    assert a5.convert(x1, base10) == ['5', 10]
    assert a5.add_(x1, y1, base10) == ['9', 10]
    assert a5.mul_(zz, yy, 10) ==  ['12', 10]


def test_Problem6():
    tiny_FASTA0 = ["nothing", "CCACTGCACTCA"]
    tiny_protein0 = "PLHS"
    tiny_FASTA1 = ["nothing", "GACTAA"]
    tiny_protein1 = "D-"
    actual = "PLHSPHPANFCVFSRD-IPYSEHLRRGALDPGRFRGPRSELSEIERARSRDLRRGPGPPGGEAAARRPLEAAGPLAGPRRRSGVAGRGGFQRGDGAVRGGPGAGARPVEEAGQQRRRLHDRGPGKVRQAGRPRPQGPSLPKPPGRASPTFLSQDLPGFPRHEDLLLPPGPEPRLLTSQSPRPEGGGRAEPRRGAPGRPTPRAVRAEPPARVPAASGPGQLPGERLPCWAPVPGRAPAGWVRGACGAGAGE-ALSARRSSWATACW-PSPGTTPETSAPRCRRRWTSS-ATLSRRWFPSTAELWVGGRGIPRRPSPCLSKASPRSSLLAVLSRGQDARGRR"

    assert a5.translate(tiny_FASTA0) ==  tiny_protein0
    assert a5.translate(tiny_FASTA1) == tiny_protein1
    assert a5.protein ==  actual
