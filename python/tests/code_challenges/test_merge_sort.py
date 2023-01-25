import pytest
from python.code_challenges.merge_sort import merge, merge_sort


# @pytest.mark.skip("TODO")
def test_exists_merge_sort():
    assert merge_sort([1, 2, 4, 6])


# @pytest.mark.skip("TODO")
def test_merge_sort():
    a = [2, 1, 4, 3]
    expected = [1, 2, 3, 4]
    actual = merge_sort(a)
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_merge_sort_list_b():
    b = [2, 14, 124, 3, 18, 21, 0]
    expected = [0, 2, 3, 14, 18, 21, 124]
    actual = merge_sort(b)
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_exists_merge():
    assert merge([1, 2], [4, 6])


# @pytest.mark.skip("TODO")
def test_merge():
    a = [2, 1]
    b = [4, 3]
    expected = [2, 1, 4, 3]
    actual = merge(a, b)
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_merge_lists_b():
    a = [2, 14, 124]
    b = [3, 18, 21]
    expected = [2, 3, 14, 18, 21, 124]
    actual = merge(a, b)
    assert actual == expected
