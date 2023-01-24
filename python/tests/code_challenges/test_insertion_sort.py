import pytest
from python.code_challenges.insertion_sort import insert_sort


# @pytest.mark.skip("TODO")
def test_exists():
    assert insert_sort([1, 2, 4, 6])


# @pytest.mark.skip("TODO")
def test_insert_sort():
    a = [2, 1, 4, 3]
    expected = [1, 2, 3, 4]
    actual = insert_sort(a)
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_insert_sort_list_b():
    b = [2, 14, 124, 3, 18, 21, 0]
    expected = [0, 2, 3, 14, 18, 21, 124]
    actual = insert_sort(b)
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_insert_sort_none():
    a = None
    expected = None
    actual = insert_sort(a)
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_insert_sort_empty():
    a = []
    expected = []
    actual = insert_sort(a)
    assert actual == expected
