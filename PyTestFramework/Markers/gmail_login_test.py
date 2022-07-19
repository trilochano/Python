import pytest


@pytest.mark.login
def homePage():
    print("hello homepage")


def loginPage():
    print("Welcome login page")


@pytest.mark.login
def dealsPage():
    print("welcome to deals page")
