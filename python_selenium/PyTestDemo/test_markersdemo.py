import pytest

@pytest.mark.smoke
def test_login():
    print("Login done");

@pytest.mark.amar
def test_addProduct():
    print("Adding Products");

@pytest.mark.regression
def test_logout():
    print("logout done");