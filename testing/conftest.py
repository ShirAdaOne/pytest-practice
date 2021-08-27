import pytest


@pytest.fixture
def login():
    # setup 操作
    print("登陆操作")
    # yield 相当于 return 操作
    yield ['tom','123456']
    # teardown 操作
    print("登出操作")


@pytest.fixture(autouse=True, scope="function")
def connect_db():
    print("### function lever ###")
    print("second fixture")
    yield
    print("### function END ###")


@pytest.fixture(scope="session",autouse=True)
def session_lev():
    print("### Session Lever ###")
    yield
    print("### END ###")