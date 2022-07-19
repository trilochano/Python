import pytest


def test_m1():
    a = 10
    b = 11
    assert a + 1 == b, 'Test Passes'
    assert a == b, 'Test Failed a is not equal b'


def test_m2():
    name = 'Trilochan'
    assert name.upper() == 'TRILOCHAN'


def test_m3():
    assert True


def test_m4():
    assert False


def test_m5():
    assert 1 == 1


def m6_test():
    assert 'Trilochan' == 'tRILOCHAN'
