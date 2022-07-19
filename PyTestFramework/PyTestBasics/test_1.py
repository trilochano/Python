import pytest


def test_login_m1():
    a = 10
    b = 11
    assert a + 1 == b, 'Test Passes'
    assert a == b, 'Test Failed a is not equal b'


def test_login_m2():
    name = 'Trilochan'
    assert name.upper() == 'TRILOCHAN'


def test_m3():
    assert True



