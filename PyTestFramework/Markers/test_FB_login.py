import pytest


@pytest.mark.login
def test_homePage():
    print("hello homepage")


def test_loginPage():
    print("Welcome login page")


@pytest.mark.login
def test_dealsPage():
    print("welcome to deals page")
