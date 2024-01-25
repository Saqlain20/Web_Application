from app import sum_something, sub_something

#"test_" is a fixed syntax for naming test file(pytest)

def test_sum_something():
    a, b = 1, 2 

    assert sum_something(a, b) == 3


def test_sub_something():
    a, b = 1, 2

    assert sub_something(a, b) == -1