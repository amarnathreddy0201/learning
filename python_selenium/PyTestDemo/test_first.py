import pytest

def test_1():
    x=4
    y=4
    assert x==y

def test_2():
    name="Selenium"
    strin="I am learning Selenium"
    assert name in strin

def test_3():
    name="Jenkenis"
    title="Jenkenis in CI server"
    assert name is title ,"Title doesn't match"
