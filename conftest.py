import pytest
from utilities.logger import Logger


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

@pytest.fixture(autouse=True)
def auto_log(request):
    Logger.add_start_step(test_name=request.node.name)
    yield
    Logger.add_end_step()
