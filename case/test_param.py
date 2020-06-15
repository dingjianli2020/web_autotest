import pytest


@pytest.fixture(scope="session")
def login_first():
    print("\n前置操作，先登录")
    yield
    print("\n后置操作，清理数据")


def add(a, b):
    return a+b


@pytest.mark.parametrize("test_input,expected",
                         [
                             [{"a": 1, "b": 2}, 3],
                             [{"a": "1", "b": "2"}, "12"]
                         ])
def test_add(test_input, expected):
    result = add(test_input["a"], test_input["b"])
    expect = expected
    assert result == expect


@pytest.mark.parametrize("a, b, expected",
                         [
                             [1, 2, 3],
                             ["1", "2", "12"]
                         ])
def test_add2(login_first, a, b, expected):
    result = add(a, b)
    expect = expected
    assert result == expect

