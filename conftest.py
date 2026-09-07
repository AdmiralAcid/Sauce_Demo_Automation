import pytest
from selenium import webdriver


@pytest.fixture()
def set_up():
    print("start test")
    yield
    print("finish test")

@pytest.fixture(scope = "module")
def set_group():
    print("enter the system")
    yield
    print("exit the system")