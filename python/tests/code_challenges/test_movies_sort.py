import pytest
try:
    from python.code_challenges.movies_sort import movies, title_sort, year_sort
except:
    from code_challenges.movies_sort import movies, title_sort, year_sort


# Expected test output of test #1
expected1 = ["The Intouchables", "Valkyrie", "Stardust", "Ratatouille", "City of God", "Memento", "The Shawshank Redemption", "Beetlejuice", "Crocodile Dundee", "The Cotton Club"]

# Expected test output of test #2
expected2 = ["Beetlejuice", "City of God", "The Cotton Club", "Crocodile Dundee", "The Intouchables", "Memento", "Ratatouille", "The Shawshank Redemption", "Stardust", "Valkyrie"];


# @pytest.mark.skip("TODO")
def test_year_sort():
    expected = expected1
    actual = year_sort(movies)
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_title_sort():
    expected = expected2
    actual = title_sort(movies)
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_exists_year_sort():
    assert year_sort([])


# @pytest.mark.skip("TODO")
def test_exists_title_sort():
    assert title_sort([])
