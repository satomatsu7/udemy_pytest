# 実行方法:pytest test_assert2.py

def test_addition():
    sum = 1 + 1
    assert sum == 2

def test_concatenation():
    result = "Hello" + " " + "World"
    assert result == "Hello World"

def test_list_append():
    items = []
    items.append("Python")
    assert items == ["Python"]
