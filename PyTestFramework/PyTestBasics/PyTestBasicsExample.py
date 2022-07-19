import pytest

#Start with test
#End with test


def m1():
    a = 10
    b = 11
    assert a + 1 == b, 'Test Passes'
    assert a == b, 'Test Failed a is not equal b'